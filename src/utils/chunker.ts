import type { ChunkToken, SplitMode } from '../types';

// 常见高频语块 / 连词 / 介词短语库（用于语块模式智能识别）
const COMMON_CHUNKS = [
  'a lot of', 'lots of', 'in front of', 'as well as', 'look forward to',
  'at the same time', 'on the other hand', 'in the morning', 'in the afternoon',
  'in the evening', 'at night', 'have a good time', 'take care of', 'wake up',
  'get up', 'sit down', 'stand up', 'turn on', 'turn off', 'go to bed',
  'by the way', 'for example', 'such as', 'of course', 'all right',
  'at first', 'at last', 'at least', 'at once', 'after all',
  'come from', 'listen to', 'look at', 'wait for', 'laugh at',
  'give up', 'put on', 'take off', 'fall in love with', 'be able to',
  'be proud of', 'be interested in', 'be afraid of', 'be good at',
  'would like to', 'used to', 'had better', 'as soon as', 'so that',
  'even though', 'even if', 'no matter', 'right now', 'just now'
];

/**
 * 清洗单词，用于判断是否匹配（转小写，去除首尾多余标点与空白）
 */
export function cleanWord(str: string): string {
  return str.toLowerCase().replace(/^[^\w']+|[^\w']+$/g, '').trim();
}

/**
 * 从文本中分离出末尾的标点符号
 * 如 "world!" -> { text: "world", trailingPunctuation: "!" }
 */
export function extractPunctuation(fullWord: string): { text: string; trailingPunctuation: string } {
  const match = fullWord.match(/^(.*?)([.,!?;:\"'—–]+)?$/);
  if (match) {
    return {
      text: match[1] || fullWord,
      trailingPunctuation: match[2] || ''
    };
  }
  return { text: fullWord, trailingPunctuation: '' };
}

/**
 * 单词级别拆分
 */
export function splitByWord(sentence: string): ChunkToken[] {
  // 按空白切分，保留连字符单词如 'well-known'
  const rawWords = sentence.trim().split(/\s+/);
  return rawWords.map((raw, idx) => {
    const { text, trailingPunctuation } = extractPunctuation(raw);
    return {
      id: `word-${idx}-${raw}`,
      text: text,
      fullText: raw,
      cleanText: cleanWord(text),
      trailingPunctuation
    };
  });
}

/**
 * 语块级别拆分（智能意群识别）
 */
export function splitByChunk(sentence: string): ChunkToken[] {
  const cleanSent = sentence.trim();
  const lowerSent = cleanSent.toLowerCase();
  
  // 贪心优先匹配已知语块
  const matchedSpans: { start: number; end: number; text: string }[] = [];
  
  for (const chunk of COMMON_CHUNKS) {
    let searchPos = 0;
    while (searchPos < lowerSent.length) {
      const idx = lowerSent.indexOf(chunk, searchPos);
      if (idx === -1) break;

      // 验证单词边界（避免匹配到单词中间）
      const prevChar = idx > 0 ? lowerSent[idx - 1] : ' ';
      const nextChar = idx + chunk.length < lowerSent.length ? lowerSent[idx + chunk.length] : ' ';
      const isWordBoundary = /[\s,.;!?]/.test(prevChar) && /[\s,.;!?]/.test(nextChar);

      if (isWordBoundary) {
        matchedSpans.push({
          start: idx,
          end: idx + chunk.length,
          text: cleanSent.slice(idx, idx + chunk.length)
        });
      }
      searchPos = idx + chunk.length;
    }
  }

  // 如果没有匹配到固定搭配，采用语法结构规则拆分（介词、连词、动词短语分组，通常 2-3 词一段）
  const words = splitByWord(cleanSent);
  if (words.length <= 3) {
    // 句子太短直接当作单词切分
    return words;
  }

  const result: ChunkToken[] = [];
  let tempGroup: ChunkToken[] = [];

  const flushGroup = () => {
    if (tempGroup.length === 0) return;
    const combinedFull = tempGroup.map(w => w.fullText).join(' ');
    const combinedClean = tempGroup.map(w => w.cleanText).join(' ');
    const lastWord = tempGroup[tempGroup.length - 1];

    result.push({
      id: `chunk-${result.length}-${tempGroup[0].id}`,
      text: tempGroup.map(w => w.text).join(' '),
      fullText: combinedFull,
      cleanText: combinedClean,
      trailingPunctuation: lastWord.trailingPunctuation
    });
    tempGroup = [];
  };

  const chunkBreakKeywords = new Set([
    'and', 'but', 'or', 'so', 'because', 'although', 'if', 'when', 'while',
    'that', 'which', 'who', 'where', 'in', 'on', 'at', 'to', 'for', 'with',
    'about', 'after', 'before'
  ]);

  for (let i = 0; i < words.length; i++) {
    const w = words[i];
    const lower = w.cleanText;

    // 当遇到标点、特定连接词或累计已满 2-3 个词时断开
    if (tempGroup.length >= 2 && chunkBreakKeywords.has(lower)) {
      flushGroup();
    }

    tempGroup.push(w);

    // 如果该词后面有逗号、分号，直接闭合语块
    if (w.trailingPunctuation.includes(',') || w.trailingPunctuation.includes(';') || tempGroup.length >= 3) {
      flushGroup();
    }
  }

  flushGroup();
  return result.length > 0 ? result : words;
}

/**
 * 整句拆分模式
 */
export function splitBySentence(sentence: string): ChunkToken[] {
  const trimmed = sentence.trim();
  const { text, trailingPunctuation } = extractPunctuation(trimmed);
  return [{
    id: `sentence-0`,
    text: text,
    fullText: trimmed,
    cleanText: cleanWord(text),
    trailingPunctuation
  }];
}

/**
 * 自定义拆分模式（例如用 / 分隔的语块）
 */
export function splitByCustom(sentence: string, customChunks?: string[]): ChunkToken[] {
  if (customChunks && customChunks.length > 0) {
    return customChunks.map((chunk, idx) => {
      const trimmed = chunk.trim();
      const { text, trailingPunctuation } = extractPunctuation(trimmed);
      return {
        id: `custom-${idx}`,
        text: text,
        fullText: trimmed,
        cleanText: cleanWord(text),
        trailingPunctuation
      };
    });
  }

  // 如果句子本身包含 '/' 分割符
  if (sentence.includes('/')) {
    const parts = sentence.split('/').map(p => p.trim()).filter(Boolean);
    return parts.map((chunk, idx) => {
      const { text, trailingPunctuation } = extractPunctuation(chunk);
      return {
        id: `custom-slash-${idx}`,
        text: text,
        fullText: chunk,
        cleanText: cleanWord(text),
        trailingPunctuation
      };
    });
  }

  return splitByChunk(sentence);
}

/**
 * 统一分词入口
 */
export function tokenizeSentence(sentence: string, mode: SplitMode, customChunks?: string[]): ChunkToken[] {
  switch (mode) {
    case 'word':
      return splitByWord(sentence);
    case 'chunk':
      return splitByChunk(sentence);
    case 'sentence':
      return splitBySentence(sentence);
    case 'custom':
      return splitByCustom(sentence, customChunks);
    default:
      return splitByWord(sentence);
  }
}

/**
 * 打乱词块（Fisher-Yates 算法）
 * 确保打乱后的顺序不等于原顺序（当词块大于1时）
 */
export function shuffleTokens(tokens: ChunkToken[]): ChunkToken[] {
  if (tokens.length <= 1) return [...tokens];
  
  let shuffled = [...tokens];
  let attempts = 0;
  
  const isSame = (a: ChunkToken[], b: ChunkToken[]) => 
    a.every((token, idx) => token.id === b[idx].id);

  do {
    for (let i = shuffled.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    attempts++;
  } while (isSame(shuffled, tokens) && attempts < 10);

  return shuffled;
}
