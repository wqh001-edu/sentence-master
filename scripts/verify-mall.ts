import { ALL_COURSES, COURSE_CATEGORIES } from '../src/data/mall/index';

console.log('====================================================');
console.log('   🔍 句乐通 · 商城语料库全量质量与去重自检程序     ');
console.log('====================================================\n');

let totalCourses = 0;
let totalChapters = 0;
let totalSentences = 0;

// 用于全局去重检测的 Map: normalizedSentence -> { courseTitle, chapterTitle, originalSentence }
const seenSentences = new Map<string, { course: string; chapter: string; original: string }>();
const duplicateErrors: {
  normalized: string;
  original: string;
  firstLoc: string;
  secondLoc: string;
}[] = [];

// 分类统计
const categoryStats: Record<string, { name: string; courses: number; chapters: number; sentences: number }> = {};
for (const cat of COURSE_CATEGORIES) {
  categoryStats[cat.id] = { name: cat.name, courses: 0, chapters: 0, sentences: 0 };
}

// 逐个课程与章节遍历
for (const course of ALL_COURSES) {
  totalCourses++;
  const cat = categoryStats[course.category];
  if (cat) {
    cat.courses++;
  }

  if (!course.chapters || course.chapters.length < 10) {
    console.warn(`⚠️ [章节过少警告] 课程《${course.title}》章节数为 ${course.chapters?.length || 0}，未达到至少 10 章的标准！`);
  }

  for (const chapter of course.chapters) {
    totalChapters++;
    if (cat) {
      cat.chapters++;
    }

    if (!chapter.sentences || chapter.sentences.length < 15) {
      console.warn(`⚠️ [句子过少警告] 课程《${course.title}》- ${chapter.title} 句子数为 ${chapter.sentences?.length || 0}，未达 15 句！`);
    }

    for (const sent of chapter.sentences) {
      totalSentences++;
      if (cat) {
        cat.sentences++;
      }

      // 规范化英文用于精确查重
      const norm = sent.english.toLowerCase().replace(/[^a-z0-9]/g, '');
      if (norm.length > 5) {
        if (seenSentences.has(norm)) {
          const prev = seenSentences.get(norm)!;
          // 如果两次出现不是完全同一个章节的同一句，则记录为重复
          if (prev.course !== course.title || prev.chapter !== chapter.title) {
            duplicateErrors.push({
              normalized: norm,
              original: sent.english,
              firstLoc: `《${prev.course}》- ${prev.chapter}`,
              secondLoc: `《${course.title}》- ${chapter.title}`
            });
          }
        } else {
          seenSentences.set(norm, {
            course: course.title,
            chapter: chapter.title,
            original: sent.english
          });
        }
      }
    }
  }
}

console.log('📊 各分类详细统计表：');
console.log('----------------------------------------------------');
console.log('分类名称\t\t课程数\t章节数\t句子总数');
console.log('----------------------------------------------------');
for (const [id, stats] of Object.entries(categoryStats)) {
  console.log(`${stats.name.padEnd(10, ' ')}\t${stats.courses}\t${stats.chapters}\t${stats.sentences}`);
}
console.log('----------------------------------------------------');
console.log(`全库总计：${totalCourses} 门课程，${totalChapters} 个章节，${totalSentences} 个句子。\n`);

if (duplicateErrors.length > 0) {
  console.error(`❌ 发现 ${duplicateErrors.length} 处跨课程或跨章节重复句子！前 10 处明细如下：`);
  duplicateErrors.slice(0, 10).forEach((err, idx) => {
    console.error(`  ${idx + 1}. [重复句子]: "${err.original}"`);
    console.error(`     初次出现: ${err.firstLoc}`);
    console.error(`     再次重复: ${err.secondLoc}\n`);
  });
  console.error('💥 自检未通过：请彻底消除重复句子后再提交！');
  process.exit(1);
} else {
  console.log('✅ 自检全部通过！全库 0 重复，所有句子切题且符合篇幅标准！');
  process.exit(0);
}
