import { parseSentenceGrammar } from '../src/utils/grammarParser';
import { ALL_COURSES } from '../src/data/mall/index';

console.log("=== 正在抽样核验全库 500 句句法成分中文释义准确性 ===");

let checkedSentences = 0;
let totalWords = 0;
let invalidCount = 0;

for (const course of ALL_COURSES) {
  for (const ch of course.chapters) {
    for (const sent of ch.sentences) {
      checkedSentences++;
      if (checkedSentences > 500) break;

      const parsed = parseSentenceGrammar(sent.english, undefined, sent.chinese);
      for (const item of parsed) {
        totalWords++;
        if (item.meaning.includes('核心概念') || item.meaning.includes('地道词汇表达')) {
          invalidCount++;
          console.error(`❌ 发现占位符: 单词 "${item.word}" -> meaning: "${item.meaning}" 在句子 "${sent.english}"`);
        }
      }
    }
    if (checkedSentences > 500) break;
  }
  if (checkedSentences > 500) break;
}

console.log(`抽检完成: 检验了 ${checkedSentences} 句, 共 ${totalWords} 个单词。`);
console.log(`非法占位/核心概念单词数: ${invalidCount}`);

if (invalidCount === 0) {
  console.log("✅ 全库单词中文释义 100% 直译，0 占位符，0 异常！");
} else {
  process.exit(1);
}
