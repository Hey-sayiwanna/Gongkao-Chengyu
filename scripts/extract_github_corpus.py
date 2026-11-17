#!/usr/bin/env python3
"""从开源公考真题库与新华字典库提取高频成语，并自动剔除日常过简熟词。

数据源仓库（按需克隆到本地同一目录后运行）：
1. 行测真题库：https://github.com/ERRRC/xingcezhenti
2. 中华新华字典成语库：https://github.com/pwxcoo/chinese-xinhua

运行方式：
  python3 scripts/extract_github_corpus.py \
    --xinhua ../chinese-xinhua/data/idiom.json \
    --zhenti ../xingcezhenti/03-言语理解与表达 \
    --output expanded_high_freq_words.json

生成的 expanded_high_freq_words.json 可直接在网页端「桌面与同步 -> 导入进度或扩充词包」一键导入。
"""

import argparse
import collections
import json
import pathlib
import re

# 日常口语极熟、字面直白无陷阱的常见简单词黑名单（可自行追加）
SIMPLE_STOPWORDS = {
    "一心一意", "三心二意", "一举两得", "半途而废", "实事求是", "自言自语",
    "四面八方", "千方百计", "五颜六色", "十全十美", "九牛一毛", "一帆风顺",
    "成千上万", "不约而同", "津津有味", "迫不及待", "无能为力", "莫名其妙",
    "理所当然", "全神贯注", "聚精会神", "兴高采烈", "垂头丧气", "大吃一惊",
    "不计其数", "层出不穷", "众所周知", "显而易见", "归根结底", "微不足道",
    "全力以赴", "脚踏实地", "持之以恒", "坚持不懈", "齐心协力", "众志成城",
    "同舟共济", "精益求精", "日新月异", "突飞猛进", "与日俱增", "名副其实",
    "不言而喻", "无可奈何", "一模一样", "大惊小怪", "顺理成章", "得心应手",
}

def main() -> None:
    parser = argparse.ArgumentParser(description="提取行测真题高频且非简单的成语词包")
    parser.add_argument("--xinhua", required=True, help="pwxcoo/chinese-xinhua 的 data/idiom.json 路径")
    parser.add_argument("--zhenti", required=True, help="ERRRC/xingcezhenti 的 03-言语理解与表达 目录路径")
    parser.add_argument("--min-freq", type=int, default=5, help="在历年言语真题中最低出现次数（默认 5 次）")
    parser.add_argument("--output", default="expanded_high_freq_words.json", help="输出词包 JSON 文件名")
    args = parser.parse_args()

    idiom_list = json.loads(pathlib.Path(args.xinhua).read_text(encoding="utf-8"))
    idiom_map = {}
    for entry in idiom_list:
        w = entry.get("word", "").strip()
        if len(w) == 4 and w not in SIMPLE_STOPWORDS:
            idiom_map[w] = entry

    counter: collections.Counter[str] = collections.Counter()
    zhenti_dir = pathlib.Path(args.zhenti)
    four_char_re = re.compile(r"[\u4e00-\u9fa5]{4}")

    for md_file in zhenti_dir.rglob("*.md"):
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        for token in four_char_re.findall(text):
            if token in idiom_map:
                counter[token] += 1

    exported = []
    for idx, (word, freq) in enumerate(counter.most_common(), start=1):
        if freq < args.min_freq:
            break
        meta = idiom_map[word]
        derivation = (meta.get("derivation") or "").strip()
        example = (meta.get("example") or "").strip()
        explanation = (meta.get("explanation") or "").strip()
        exported.append({
            "id": f"gh_{idx:04d}",
            "word": word,
            "pinyin": meta.get("pinyin", ""),
            "cat": "error_prone_idiom",
            "tag": f"真题出现 {freq} 次",
            "trap": "留意字面语素古义、感情色彩（褒贬）及固定搭配对象。",
            "meaning": explanation,
            "usage": f"出处：{derivation} 例句：{example}".strip(),
            "src": "https://github.com/ERRRC/xingcezhenti"
        })

    pathlib.Path(args.output).write_text(
        json.dumps({"words": exported}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"已完成筛选：共导出 {len(exported)} 条真题高频成语 -> {args.output}")

if __name__ == "__main__":
    main()