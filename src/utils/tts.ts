/**
 * 现代高品质语音合成引擎（Web Speech Synthesis）
 * 自动识别并选用系统高保真自然发音（Natural / Google / Microsoft / Samantha 等）
 */

let voices: SpeechSynthesisVoice[] = [];

function loadVoices(): Promise<SpeechSynthesisVoice[]> {
  return new Promise((resolve) => {
    if (typeof window === 'undefined' || !('speechSynthesis' in window)) {
      return resolve([]);
    }
    const current = window.speechSynthesis.getVoices();
    if (current.length > 0) {
      voices = current;
      return resolve(current);
    }
    window.speechSynthesis.onvoiceschanged = () => {
      voices = window.speechSynthesis.getVoices();
      resolve(voices);
    };
  });
}

// 启动时预加载声音列表
if (typeof window !== 'undefined') {
  loadVoices();
}

/**
 * 匹配最佳声音引擎
 */
function findBestVoice(lang: 'en-US' | 'en-GB'): SpeechSynthesisVoice | null {
  if (voices.length === 0 && typeof window !== 'undefined') {
    voices = window.speechSynthesis.getVoices();
  }

  const prefix = lang === 'en-GB' ? 'en-GB' : 'en-US';
  const matched = voices.filter(v => v.lang.replace('_', '-').startsWith(prefix));

  // 优先选取标记有 Natural、Online、Google、Microsoft 的优质音色
  const priorityMatch = matched.find(v => 
    /natural|online|google|microsoft|samantha|daniel|arthur/i.test(v.name)
  );

  if (priorityMatch) return priorityMatch;
  if (matched.length > 0) return matched[0];

  // 退回任意英语声音
  const anyEnglish = voices.find(v => v.lang.startsWith('en'));
  return anyEnglish || null;
}

export interface SpeakOptions {
  rate?: number;         // 语速 0.7 - 1.5
  accent?: 'en-US' | 'en-GB';
  onEnd?: () => void;
  onError?: () => void;
}

/**
 * 朗读英文文本
 */
export function speakText(text: string, options: SpeakOptions = {}) {
  if (typeof window === 'undefined' || !('speechSynthesis' in window)) {
    return;
  }

  // 立即中断前一个正在朗读的声音
  window.speechSynthesis.cancel();

  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = options.accent || 'en-US';
  utterance.rate = options.rate || 1.0;
  utterance.pitch = 1.0;

  const bestVoice = findBestVoice(options.accent || 'en-US');
  if (bestVoice) {
    utterance.voice = bestVoice;
  }

  if (options.onEnd) {
    utterance.onend = options.onEnd;
  }
  if (options.onError) {
    utterance.onerror = options.onError;
  }

  window.speechSynthesis.speak(utterance);
}

/**
 * 停止当前发音
 */
export function stopSpeaking() {
  if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
    window.speechSynthesis.cancel();
  }
}
