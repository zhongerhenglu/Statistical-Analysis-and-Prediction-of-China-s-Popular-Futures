# 中国热门期货统计分析与预测 —— Team02-G04
**数据分析与经济决策（ds2026）课程作业**

## 📋 项目基本信息
| 项目 | 内容 |
|---|---|
| 课程 | 数据分析与经济决策 ds2026 |
| 小组 | Team02-G04 |
| 研究方向 | 能源化工、地产基建、贵金属、新能源四大板块期货量化分析 |
| 组员 | 25210227 荣渝渝｜25210229 沈仕沐｜25210246 王丽娜｜25210257 吴玥｜25210271 连伊丽｜25210275 薛佳程｜25210285 易忠凯 |
| 主仓库 | https://github.com/zhongerhenglu/Statistical-Analysis-and-Prediction-of-China-s-Popular-Futures |
| 提交格式 | 严格遵循 lianxhcn/ds2026/homework/Team02 规范 |
| 完成日期 | 2026-05-23 |

---

## 📖 项目简介
本项目围绕**中国四大核心产业链期货**开展全流程量化分析：数据获取 → 标准化清洗 → 探索性分析 → 可视化 → 决策结论。
严格按照课程要求：**明确决策主体、基于真实政策与市场背景、输出可落地的数据驱动结论**。

研究时间：2010-01-01 — 2025-12-31（日度高频数据）
研究对象：
- 能源化工：原油 SC、PTA
- 地产基建：螺纹钢 RB、铁矿石 I
- 贵金属：沪金 AU
- 新能源：碳酸锂 LC、工业硅 SI

项目目标：
为**实体企业、贸易商、期货交易者、机构投资者**提供价格联动、波动风险、趋势特征的量化依据，支持套期保值、趋势交易、风险管理等真实决策。

---

## 👥 任务分工
| 学号姓名 | 负责板块 | 核心任务 |
|---|---|---|
| 25210275 薛佳程 | 能源化工（SC+PTA） | 数据获取、代码整合、项目结构规范 |
| 25210271 连伊丽 | 能源化工（SC+PTA） | 可视化、统计检验、报告撰写 |
| 25210227 荣渝渝 | 地产基建（RB+Iron） | 数据采集、清洗、预处理 |
| 25210229 沈仕沐 | 地产基建（RB+Iron） | 分析、图表解读、决策结论 |
| 25210246 王丽娜 | 新能源（LC+SI） | 数据获取、指标构建、波动分析 |
| 25210257 吴玥 | 新能源（LC+SI） | 联动分析、报告整理、幻灯片制作 |
| 25210285 易忠凯 | 贵金属（AU） | 避险属性分析、统计检验、结论输出 |

---

## 📂 标准目录结构
Statistical-Analysis-and-Prediction-of-China-s-Popular-Futures/  
├── README.md # 项目总说明（本文件）  
├── requirements.txt # Python 依赖环境  
├── .gitignore # Git 忽略文件  
├── _quarto.yml # Quarto 报告配置文件  
│  
├── Team02-G04 - 原油 SC + PTA 投资分析 /  
├── Team02-G04 - 螺纹钢 RB、铁矿石 I 投资分析 /  
├── Team02-G04 - 黄金现货投资分析 /  
├── Team02-G04 - 碳酸锂 LC 期货投资分析 /  
│  
└── 每个子模块统一结构：  
├── README.md # 模块说明  
├── report.md/report.qmd # 完整分析报告  
├── slides.md # 汇报幻灯片  
├── slides.pdf # 幻灯片 PDF  
├── code/  
│ ├── 01_data_collect.py  
│ ├── 02_data_clean.py  
│ ├── 03_visual_eda.py  
│ └── 04_analysis_conclusion.py  
├── data/  
│ ├── data_raw/  
│ └── data_clean/  
└── output/  
├── charts/ # 7 张标准可视化图  
└── conclusion.txt # 数据驱动结论  

---
## 🔧 运行环境（可直接安装）
```bash
pip install -r requirements.txt

requirements.txt 内容
akshare>=1.12.0
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
scipy>=1.10.0

🚀 运行步骤（标准四步）
数据获取  
python code/01_data_collect.py  
标准化清洗  
python code/02_data_clean.py  
可视化分析（7 张标准图）  
python code/03_visual_eda.py  
统计分析与结论输出  
python code/04_analysis_conclusion.py  
生成报告（Quarto）  
quarto render report.qmd  

📌 提交规范符合性说明
✅ 每个模块均包含：决策主体 → 政策背景 → 数据 → 统计 → 可视化 → 结论 → 局限
✅ 代码命名规范：01/02/03/04 标准流程
✅ 图表规范：时序图、直方图、KDE、箱线图、波动率、散点图、热力图
✅ 文件规范：README + report.md + slides.md + slides.pdf
✅ 路径规范：纯相对路径，无中文乱码，可直接复现
✅ 分析规范：包含描述统计、偏度峰度、JB 检验、极端行情、相关性分析
📎 数据来源说明
所有数据均来自 akshare 公开免费接口，合规可复现，无付费数据、无侵权内容。





