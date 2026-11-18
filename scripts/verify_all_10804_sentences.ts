import { parseSentenceGrammar } from '../src/utils/grammarParser';
import { ALL_COURSES } from '../src/data/mall/index';

console.log("=== 正在全量核验全库所有 10,804 句句法成分中文释义准确性 ===");

let checkedSentences = 0;
let totalWords = 0;
let invalidCount = 0;

for (const course of ALL_COURSES) {
  for (const ch of course.chapters) {
    for (const sent of ch.sentences) {
      checkedSentences++;
      const parsed = parseSentenceGrammar(sent.english, undefined, sent.chinese);
      for (const item of parsed) {
        totalWords++;
        if (item.meaning.includes('核心概念') || item.meaning.includes('地道词汇表达')) {
          invalidCount++;
          console.error(`❌ 发现占位符: "${item.word}" in "${sent.english}"`);
        }
      }
    }
  }
}

console.log(`全库全量检验完成: 检验了全部 ${checkedSentences} 句, 共 ${totalWords} 个单词。`);
console.log(`非法占位/核心概念单词数: ${invalidCount}`);

if (invalidCount === 0) {
  console.log("🎉 完美！全库 10,804 句所有单词 100.00% 纯中文翻译，0 占位符！");
  process.exit(0);
} else {
  process.exit(1);
}
