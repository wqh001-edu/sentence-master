import type { SentenceExpansion } from '../types';

// 常用高频词的词族数据库（串记）
const WORD_FAMILIES: Record<string, { root: string; chain: string[] }> = {
  care: {
    root: 'care (关怀/小心)',
    chain: ['care (v./n. 关心/关怀)', 'careful (adj. 小心的)', 'carefully (adv. 小心地)', 'careless (adj. 粗心的)']
  },
  succeed: {
    root: 'succeed (成功/继承)',
    chain: ['succeed (v. 成功)', 'success (n. 成功)', 'successful (adj. 成功的)', 'successfully (adv. 成功地)']
  },
  beauty: {
    root: 'beauty (美丽)',
    chain: ['beauty (n. 美丽)', 'beautiful (adj. 美丽的)', 'beautifully (adv. 美丽地)', 'beautify (v. 美化)']
  },
  excite: {
    root: 'excite (激发/激动)',
    chain: ['excite (v. 使激动)', 'excited (adj. 感到兴奋的)', 'exciting (adj. 令人激动的)', 'excitement (n. 兴奋/激动)']
  },
  live: {
    root: 'live (生活/居住)',
    chain: ['live (v. 居住/生活)', 'alive (adj. 活着的)', 'living (adj. 活着的/生活)', 'life (n. 生命/生活)']
  },
  hard: {
    root: 'hard (努力/硬)',
    chain: ['hard (adj./adv. 努力的/硬的)', 'harden (v. 使变硬)', 'hardly (adv. 几乎不)', 'hardship (n. 艰难困苦)']
  },
  friend: {
    root: 'friend (朋友)',
    chain: ['friend (n. 朋友)', 'friendly (adj. 友好的)', 'friendship (n. 友谊)', 'friendless (adj. 无友的)']
  },
  act: {
    root: 'act (行动/表演)',
    chain: ['act (v./n. 行动/表演)', 'action (n. 行动)', 'actor (n. 演员)', 'active (adj. 积极的)']
  },
  civil: {
    root: 'civil (市民/文明)',
    chain: ['civil (adj. 国内的/公民的)', 'civilian (n. 平民)', 'civilize (v. 教化/使文明)', 'civilization (n. 文明)']
  },
  hope: {
    root: 'hope (希望)',
    chain: ['hope (v./n. 希望)', 'hopeful (adj. 充满希望的)', 'hopefully (adv. 有希望地)', 'hopeless (adj. 绝望的)']
  }
};

/**
 * 为句子自动生成或提取 串记·联想·扩展
 */
export function getSentenceExpansion(sentenceText: string, customExpansion?: SentenceExpansion): SentenceExpansion {
  if (customExpansion) {
    return customExpansion;
  }

  const words = sentenceText.toLowerCase().replace(/[^a-z\s]/g, '').split(/\s+/);

  // 1. 尝试匹配词族
  let matchedFamily: { root: string; chain: string[] } | undefined = undefined;
  for (const w of words) {
    if (WORD_FAMILIES[w]) {
      matchedFamily = WORD_FAMILIES[w];
      break;
    }
  }

  if (!matchedFamily) {
    // 默认兜底常用词族
    matchedFamily = {
      root: 'practice (练习/实践)',
      chain: ['practice (n./v. 练习)', 'practical (adj. 实用的)', 'practically (adv. 实际上)', 'practitioner (n. 从业者)']
    };
  }

  // 2. 主题联想词
  const defaultAssociations = [
    { word: 'expression', phonetic: '/ɪkˈsprɛʃən/', meaning: '表达；表情' },
    { word: 'fluency', phonetic: '/ˈfluːənsi/', meaning: '流利度；语感' },
    { word: 'context', phonetic: '/ˈkɒntɛkst/', meaning: '语境；上下文' },
    { word: 'idiom', phonetic: '/ˈɪdiəm/', meaning: '习语；成语' }
  ];

  // 3. 扩展固定搭配与例句
  const defaultExtensions = [
    {
      phrase: 'in terms of',
      meaning: '在...方面；依据',
      example: 'Think about it in terms of long-term benefits.',
      exampleCn: '从长远利益的角度来思考这件事。'
    },
    {
      phrase: 'make sense of',
      meaning: '理解；弄懂...的意思',
      example: 'Can you make sense of this difficult sentence?',
      exampleCn: '你能弄明白这个难句的意思吗？'
    }
  ];

  return {
    wordFamily: matchedFamily,
    associations: defaultAssociations,
    extensions: defaultExtensions
  };
}
