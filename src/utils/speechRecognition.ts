/**
 * 浏览器端原生语音识别与口语评测算法
 */

export interface WordScore {
  targetWord: string;
  spokenWord?: string;
  status: 'correct' | 'imperfect' | 'missing';
}

export interface SpeechEvalResult {
  score: number;             // 0 - 100
  transcript: string;        // 识别到的整句
  words: WordScore[];        // 逐词得分
}

/**
 * 计算两个字符串的 Levenshtein 距离
 */
function levenshteinDistance(s1: string, s2: string): number {
  const m = s1.length;
  const n = s2.length;
  const d: number[][] = [];

  for (let i = 0; i <= m; i++) d[i] = [i];
  for (let j = 0; j <= n; j++) d[0][j] = j;

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      const cost = s1[i - 1] === s2[j - 1] ? 0 : 1;
      d[i][j] = Math.min(
        d[i - 1][j] + 1,
        d[i][j - 1] + 1,
        d[i - 1][j - 1] + cost
      );
    }
  }
  return d[m][n];
}

/**
 * 单词相似度 0 ~ 1
 */
function calculateWordSimilarity(w1: string, w2: string): number {
  const clean1 = w1.toLowerCase().replace(/[^a-z0-9]/g, '');
  const clean2 = w2.toLowerCase().replace(/[^a-z0-9]/g, '');
  if (clean1 === clean2) return 1.0;
  const maxLen = Math.max(clean1.length, clean2.length);
  if (maxLen === 0) return 1.0;
  const dist = levenshteinDistance(clean1, clean2);
  return Math.max(0, 1 - dist / maxLen);
}

/**
 * 评测用户的口语朗读与目标句子
 */
export function evaluateSpokenText(targetSentence: string, userTranscript: string): SpeechEvalResult {
  const targetWords = targetSentence.trim().split(/\s+/).map(w => w.replace(/[.,!?;:"']/g, ''));
  const spokenWords = userTranscript.trim().split(/\s+/).map(w => w.replace(/[.,!?;:"']/g, ''));

  const results: WordScore[] = [];
  let spokenIdx = 0;
  let totalScorePoints = 0;

  for (let i = 0; i < targetWords.length; i++) {
    const tWord = targetWords[i];
    let bestSimilarity = 0;
    let matchedWord = '';
    let bestMatchOffset = -1;

    // 在当前及后续 2 个词范围内寻找最佳对齐
    for (let offset = 0; offset <= 2 && (spokenIdx + offset) < spokenWords.length; offset++) {
      const sWord = spokenWords[spokenIdx + offset];
      const sim = calculateWordSimilarity(tWord, sWord);
      if (sim > bestSimilarity) {
        bestSimilarity = sim;
        matchedWord = sWord;
        bestMatchOffset = offset;
      }
    }

    if (bestSimilarity >= 0.85) {
      results.push({ targetWord: tWord, spokenWord: matchedWord, status: 'correct' });
      totalScorePoints += 100;
      spokenIdx += (bestMatchOffset + 1);
    } else if (bestSimilarity >= 0.5) {
      results.push({ targetWord: tWord, spokenWord: matchedWord, status: 'imperfect' });
      totalScorePoints += 65;
      spokenIdx += (bestMatchOffset + 1);
    } else {
      results.push({ targetWord: tWord, status: 'missing' });
      totalScorePoints += 0;
    }
  }

  const finalScore = targetWords.length > 0 ? Math.round(totalScorePoints / targetWords.length) : 0;

  return {
    score: Math.min(100, Math.max(0, finalScore)),
    transcript: userTranscript,
    words: results
  };
}

/**
 * 创建语音识别器实例
 */
export function createSpeechRecognizer(
  onResult: (transcript: string, isFinal: boolean) => void,
  onError: (err: unknown) => void
) {
  if (typeof window === 'undefined') return null;

  const win = window as unknown as {
    SpeechRecognition?: any;
    webkitSpeechRecognition?: any;
  };

  const SpeechRec = win.SpeechRecognition || win.webkitSpeechRecognition;
  if (!SpeechRec) {
    return null;
  }

  const recognition = new SpeechRec();
  recognition.continuous = false;
  recognition.interimResults = true;
  recognition.lang = 'en-US';

  recognition.onresult = (event: any) => {
    let interim = '';
    let final = '';

    for (let i = event.resultIndex; i < event.results.length; ++i) {
      if (event.results[i].isFinal) {
        final += event.results[i][0].transcript;
      } else {
        interim += event.results[i][0].transcript;
      }
    }

    if (final.length > 0) {
      onResult(final.trim(), true);
    } else if (interim.length > 0) {
      onResult(interim.trim(), false);
    }
  };

  recognition.onerror = (e: unknown) => {
    onError(e);
  };

  return recognition;
}
