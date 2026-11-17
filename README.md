# 不背成语

感谢 **Gemini4-Carbon** 设计制作了整个轻量 App。

## 立即打开「不背成语」

```text
https://hey-sayiwanna.github.io/Gongkao-Chengyu/
```

## 第一步：安装指南

### iPhone / iPad

1. 用系统自带的 **Safari** 打开上方链接。
2. 点击 Safari 的「分享」按钮（方框向上箭头），选择 **「添加到主屏幕」**，再点击「添加」。
3. 返回桌面，点击「不背成语」图标即可打开。首次联网加载后，支持离线使用。

### Mac

1. 用 **Safari**（macOS 14 Sonoma 及以上）打开上方链接。
2. 点击菜单栏 **「文件」→「添加到程序坞」**，即可像独立 App 一样打开。
3. 背词时可以使用快捷键：`空格键` 翻开解析，数字键 `1 / 2 / 3 / 4` 自评记忆强度，按 `X` 键把太简单的词永久剔除。

## 第二步：可选扩充上千条真题高频词（自动过滤简单词）

应用内置了精筛后的 **678 组公考 90% 覆盖应试核心词书（含专项一望文生义 152 组、专项二褒贬与对象易错 172 组、词书三真题已考少用核心词 156 组、词书四央媒时评潜力词 100 组、专项五高频双字实词 98 组，全部四字词逐条标明褒贬中性）+ 18 道国省考典型真题**。如果你想把历年 16,000 道言语理解真题里的全部高频成语都筛进来：

```bash
git clone https://github.com/pwxcoo/chinese-xinhua.git
git clone https://github.com/ERRRC/xingcezhenti.git
python3 scripts/extract_github_corpus.py \
  --xinhua chinese-xinhua/data/idiom.json \
  --zhenti xingcezhenti/03-言语理解与表达 \
  --min-freq 5 \
  --output expanded_high_freq_words.json
```

然后在网页应用底部的 **「桌面与同步」→「导入进度或扩充词包 (.json)」** 选中生成的 `expanded_high_freq_words.json` 即可一键合入。
