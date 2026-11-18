import { parseSentenceGrammar } from '../src/utils/grammarParser';

const sentence = "Good afternoon, I have a guaranteed room reservation under the name Miller.";
const sentenceCn = "下午好，我有以戴维·米勒名字担保的客房预订。";

const results = parseSentenceGrammar(sentence, undefined, sentenceCn);

console.log("=== 解析结果检验 ===");
for (const item of results) {
  console.log(`Word: ${item.word.padEnd(14)} | Role: ${item.role.padEnd(4)} | Pos: ${item.pos.padEnd(6)} | Short: ${item.shortMeaning?.padEnd(16)} | Meaning: ${item.meaning}`);
}
