# 不背成语 

## 第一步：在 iPhone 与 Mac 添加到主屏幕 / 程序坞

1. **iPhone / iPad**：
   - 必须用系统自带 **Safari** 打开上面的网址。
   - 点击底部正中间的「分享」按钮（向上箭头方框） -> 下滑点击 **「添加到主屏幕」** -> 点击右上角「添加」。
   - 返回手机桌面点击「不背错词」图标，即可以无浏览器地址栏的全屏原生形态运行，且首次打开后自动离线缓存，没网也能刷。

2. **Mac 电脑**：
   - 用 macOS 自带 **Safari**（macOS 14 Sonoma 及以上）或 **Chrome** 打开同一网址。
   - Safari 点击顶部菜单栏 **「文件」 -> 「添加到程序坞（Add to Dock）」**；Chrome 点击地址栏右侧安装图标。
   - 在 Mac 上背词时可直接用键盘操作：`空格键` 翻开解析，数字键 `1 / 2 / 3 / 4` 自评记忆强度，按 `X` 键一键把太简单的词永久剔除。

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

然后在网页应用底部的 **「桌面与同步」 -> 「导入进度或扩充词包 (.json)」** 选中生成的 `expanded_high_freq_words.json` 即可一键合入。
