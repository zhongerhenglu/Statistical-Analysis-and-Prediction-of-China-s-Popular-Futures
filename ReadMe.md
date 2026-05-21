
## 📋 项目基本信息
|项目|内容|
|---|---|
|课程|数据分析与经济决策（ds2026）|
|题目|能源化工、新能源、地产基建、贵金属|
|小组|第 4 组|
|成员|25210227 荣渝渝｜25210229 沈仕沐｜25210246 王丽娜｜25210257 吴玥｜25210271 连伊丽｜25210275 薛佳程｜25210285 易忠凯|
|GitHub 主仓库|[https://github\.com/zhongerhenglu/ds2026\-G04\-T\-B2\_FedPolicyAssets](https://github.com/zhongerhenglu/ds2026-G04-T-B2_FedPolicyAssets)|
|GitHub 子仓库|[https://github\.com/zhongerhenglu/Statistical\-Analysis\-and\-Prediction\-of\-China\-s\-Popular\-Futures](https://github.com/zhongerhenglu/Statistical-Analysis-and-Prediction-of-China-s-Popular-Futures)|
|Pages 在线报告|[https://zhongerhenglu\.github\.io/ds2026\-G04\-T\-B2\_FedPolicyAssets/](https://zhongerhenglu.github.io/ds2026-G04-T-B2_FedPolicyAssets/)|
|提交日期|2026\-05\-23|

## 📖 项目简介

本项目聚焦 **美联储货币政策周期**，深入分析加息、降息对全球资产价格的传导效应，同时结合中国热门期货市场，围绕四大核心主线（能源化工、新能源、地产基建、贵金属），开展数据收集、清洗、分析与预测工作，清晰呈现期货品种的价格逻辑、资金热度及未来趋势，为投资决策提供专业数据参考。

📅 研究时间范围：2020–2025 年（月度/日度频率）

🎯 核心研究对象：

- 能源化工：原油（SC）、精对苯二甲酸（PTA）

- 新能源：碳酸锂（LC）、工业硅（SI）（广州期货交易所）

- 地产基建：螺纹钢（RB）、铁矿石（I）

- 贵金属：沪金（AU）

## 👥 小组任务分工

|成员（学号）|核心任务|合作对象|
|---|---|---|
|薛佳程（25210275）|项目整体整合；能源化工（原油SC、PTA）数据收集与清洗|连伊丽|
|王丽娜（25210246）|新能源方向（碳酸锂LC、工业硅SI）数据收集与清洗|吴玥|
|易忠凯（25210285）|贵金属（沪金AU）方向数据收集、指标整理、联动分析|无|
|吴玥（25210257）|新能源（碳酸锂LC、工业硅SI）分析与结论撰写|王丽娜|
|荣渝渝（25210227）|地产基建（螺纹钢RB、铁矿石I）数据收集与清洗|沈仕沐|
|沈仕沐（25210229）|地产基建（螺纹钢RB、铁矿石I）分析与结论撰写|荣渝渝|
|连伊丽（25210271）|能源化工（原油SC、PTA）分析与结论撰写|薛佳程|

## 📂 目录结构

```plain text
Statistical-Analysis-and-Prediction-of-China-s-Popular-Futures/
├── README.md                  # 项目说明文档（本文件）
├── report.md                  # 完整分析报告（Markdown格式）
├── slides.md                  # Marp幻灯片源文件
├── slides.pdf                 # 幻灯片PDF导出版
├── data/                      # 数据目录
│   ├── data_raw/              # 原始数据（未清洗）
│   └── data_clean/            # 清洗后数据（可直接用于分析）
├── code/                      # 代码目录
│   ├── 01_get_data.ipynb      # 数据获取脚本（Notebook）
│   ├── 02_data_clean.ipynb    # 数据清洗脚本（Notebook）
│   └── 03_analysis_visualization.ipynb # 分析与可视化脚本
└── output/                    # 输出目录
    └── charts/                # 可视化图表（图片文件）
```

## 🔧 环境依赖

```python
# 核心依赖（必装）
pip install pandas numpy matplotlib

# 数据获取依赖（可选）
pip install fredapi yfinance tushare
```

## 📌 注意事项

- 所有数据、代码、报告已完整提交至对应GitHub仓库，可直接克隆使用。

- 数据文件禁止上传付费数据库（如Wind、CSMAR）内容，相关数据来源已在报告中注明。

- 代码可直接运行，文件路径已适配Windows系统，无需额外修改。

- Pages在线报告可直接访问，如需下载PDF版本，可在仓库中获取。

