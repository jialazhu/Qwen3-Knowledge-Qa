# Qwen3 江湖郎中&百科问答助手项目

## 项目概述

本项目是基于Qwen3大语言模型的专业微调项目，主要实现两大核心功能：

### 🏥 智能金庸风格江湖郎中助手
- 以金庸武侠小说风格提供风趣幽默的医疗咨询服务
- 支持多种医疗场景的专业问答，包括症状诊断、治疗方案、疾病预防等
- 具备R1推理风格，提供带思考过程的深度医疗分析

### 📚 智能百科问答助手
- 提供多场景、多领域的智能问答服务
- 支持中文百科知识的深度理解和回答
- 适用于教育、咨询、知识检索等多种应用场景
### 核心特性

- 🎯 **双模态支持**：同时支持医疗咨询和百科问答两大应用场景
- 🧠 **R1推理风格**：具备深度思考过程的推理能力，提供专业分析
- 🔧 **多种微调方式**：支持全参数微调和LoRA微调，适应不同硬件条件
- 📊 **完整训练流程**：从数据准备到模型部署的完整pipeline
- 🎭 **特色风格**：金庸武侠风格的独特表达方式，提升用户体验
- 📈 **实时监控**：集成SwanLab进行训练过程监控和可视化
- 🎯 **专业提示词**：针对不同场景优化的提示词模板，提升回答质量

## 项目结构

### 📚 百科问答助手 (chinese/)
```
chinese/
├── 📁 核心脚本
│   ├── medical_assistant.py     # 助手主程序
│   ├── train_chinese_lora.py    # LoRA微调训练脚本
│   ├── predict.py               # 模型推理脚本
│   ├── data.py                  # 数据处理脚本
│   └── download_model.py        # 模型下载脚本
├── 📁 数据文件
│   ├── dataSets/chinese_simpleqa.jsonl     # 原始数据集
│   ├── dataSets/chinese-category.jsonl     # 场景分类数据集
│   ├── dataSets/chinese-train.jsonl        # 格式化训练数据
│   └── dataSets/chinese-val.jsonl          # 格式化验证数据
├── 📁 模型文件
│   ├── models/                  # 基础模型存储
│   └── output/                  # 训练输出模型
└── 📁 日志文件
    └── swanlog/                 # SwanLab训练日志
```

### 🏥 江湖郎中助手 (charlatan/)
```
charlatan/
├── 📁 核心脚本
│   ├── medical_assistant.py     # 助手主程序
│   ├── train.py                 # 全参数微调训练脚本
│   ├── train_lora.py            # LoRA微调训练脚本
│   ├── inference.py            # 基础推理脚本
│   ├── inference_lora.py       # LoRA推理脚本
│   ├── predict.py              # 预测脚本
│   ├── data.py                  # 数据处理脚本
│   └── download_model.py       # 模型下载脚本
├── 📁 数据文件
│   ├── dataSets/金庸-train.jsonl    # 格式化训练数据
│   └── dataSets/金庸-val.jsonl      # 格式化验证数据
├── 📁 模型文件
│   ├── models/                  # 基础模型存储
│   └── output/                  # 训练输出模型
└── 📁 日志文件
    └── swanlog/                 # SwanLab训练日志
```

### 📊 数据集说明
- **chinese_simpleqa.jsonl**: 中文百科问答数据集 (1.76MB)
- **金庸-train.jsonl**: 江湖郎中风格训练数据 (2.05MB)
- **金庸-val.jsonl**: 江湖郎中风格验证数据 (224KB)
- **chinese-train.jsonl**: 中文百科训练数据 (644KB)
- **chinese-val.jsonl**: 中文百科验证数据 (72KB)

## 技术架构

### 基础模型
- **Qwen3-0.6B**: 项目主要使用的轻量级模型，适合资源受限环境
- **Qwen3-1.7B**: 可选模型，用于对比实验

### 微调技术
1. **全参数微调**: 更新模型所有权重参数
2. **LoRA微调**: 低秩适应，高效微调技术

### 推理风格
- **R1推理风格**: 包含思考过程的推理模式
- **医疗专业提示词**: 针对不同医疗场景优化

## 环境要求

### 硬件要求（基于Qwen3-0.6B）
- **全参数微调**: 16GB显存
- **LoRA微调**: 12GB显存
- **推理**: 4GB显存（推荐）

### 软件依赖
```bash
swanlab                    # 训练监控
modelscope==1.22.0        # 模型下载
transformers              # 模型加载
datasets==3.2.0           # 数据处理
peft                      # LoRA微调
accelerate                # 训练加速
pandas                    # 数据处理
addict                    # 配置管理
```

## 快速开始

### 1. 环境安装
```bash
# 创建虚拟环境（推荐）
conda create -n qwen3-medical python=3.10
conda activate qwen3-medical

# 安装依赖
pip install -r requirements.txt
```

### 2. 模型下载
```bash
# 下载基础模型
python charlatan/download_model.py
# 或
python chinese/download_model.py
```

### 3. 数据准备
```bash
# 江湖郎中助手数据处理
python charlatan/data.py

# 百科问答助手数据处理
python chinese/data.py
```
自动完成：
- 数据集格式化
- 训练/验证集划分（9:1比例）
- 数据预处理和tokenization

### 4. 模型训练

#### 江湖郎中助手训练
```bash
# 全参数微调（需要16GB+显存）
python charlatan/train.py

# LoRA微调（需要12GB+显存）
python charlatan/train_lora.py
```

#### 百科问答助手训练
```bash
# LoRA微调
python chinese/train_chinese_lora.py
```

### 5. 模型推理

#### 江湖郎中助手
```bash
# 基础推理
python charlatan/inference.py

# LoRA推理
python charlatan/inference_lora.py

# 交互式医疗助手
python charlatan/medical_assistant.py
```

#### 百科问答助手
```bash
# 推理测试
python chinese/predict.py

# 交互式助手
python chinese/medical_assistant.py
```

## 医疗场景支持

项目支持10种专业医疗场景：

| 场景ID | 场景名称 | 专业领域 | 示例问题 |
|--------|----------|----------|----------|
| 1 | 症状诊断 | 临床诊断 | "我最近经常头痛，伴有恶心，这是什么原因？" |
| 2 | 治疗方案 | 治疗指导 | "高血压患者应该如何控制血压？" |
| 3 | 疾病预防 | 预防医学 | "如何预防心血管疾病？" |
| 4 | 医学教育 | 医学知识 | "什么是高血压？" |
| 5 | 紧急评估 | 急诊医学 | "胸痛持续了3天，需要立即就医吗？" |
| 6 | 营养指导 | 营养学 | "糖尿病患者应该如何选择食物？" |
| 7 | 心理健康 | 心理学 | "如何缓解焦虑情绪？" |
| 8 | 儿科咨询 | 儿科学 | "儿童发热应该如何处理？" |
| 9 | 老年健康 | 老年医学 | "老年人如何预防跌倒？" |
| 10 | 女性健康 | 妇科学 | "更年期症状如何缓解？" |

## 使用方式

### 交互式使用
```bash
python /charlatan/medical_assistant.py
```

### 命令行使用
```bash
# 单次问答
python /charlatan/medical_assistant.py -q "我最近头痛，可能是什么原因？" -s diagnosis

# 批量处理
python /charlatan/medical_assistant.py -b sample_questions.json

# 指定模型路径
python /charlatan/medical_assistant.py -c ./output/Qwen3-0.6B/checkpoint-900
```

### 编程接口
```python
from medical_assistant import MedicalAssistant

# 创建助手实例
assistant = MedicalAssistant("./output/Qwen3-0.6B/checkpoint-900")
assistant.load_model()

# 询问问题
response = assistant.ask_question(
    "我最近胃部不适，可能是什么原因？", 
    scenario_type="diagnosis"
)
print(response)
```

## 训练监控

项目集成SwanLab进行训练监控：
- 实时损失曲线
- 学习率变化
- 模型性能指标
- 训练日志记录

访问地址：[SwanLab训练监控](https://swanlab.cn/@candle/qwen3-sft-medical/overview)

## 模型性能

### 训练效果对比
- **全参数微调**: 效果更好，但资源消耗大
- **LoRA微调**: 资源消耗小，效果略逊于全参数微调

### 推理示例
```
Question: 慢性心房颤动和毛细胞白血病是否存在某些共同点？

LLM:
少侠保重身体。江湖上有一句话，人生如战场，疾病如敌人。慢性心房颤动和毛细胞白血病虽然属于不同的疾病，但它们在某些方面确实存在一些共同点。

首先，慢性心房颤动和毛细胞白血病都是慢性疾病，需要长期的治疗和管理。就像江湖中的长期战斗一样，需要耐心和毅力。

其次，这两种疾病都会对患者的身体造成一定的影响。慢性心房颤动会导致心脏不规律跳动，可能引发心脏衰竭等并发症；而毛细胞白血病则会导致骨髓中的毛细胞异常增生，影响正常造血功能。这些都需要及时的治疗和调理，才能保持身体的健康。

最后，治疗这两种疾病都需要综合考虑个体情况和病情特点。就像江湖中的武功修炼一样，需要根据自身的实际情况选择合适的方法和药物。同时，也需要定期的复查和随访，以便及时调整治疗方案。

总的来说，慢性心房颤动和毛细胞白血病虽然不同，但都需要我们以坚定的意志和智慧来对抗，才能在这个医疗江湖中取得胜利。
```

## 注意事项

### 医疗免责声明
- 本助手仅提供参考建议，不能替代专业医疗诊断
- 紧急情况请立即就医
- 所有建议仅供参考，具体治疗请咨询专业医生

### 技术限制
- 模型基于训练数据，可能存在知识局限性
- 建议结合最新医学指南使用
- 定期更新模型以保持准确性

## 扩展开发

### 添加新的医疗场景
1. 在`MEDICAL_PROMPTS`中添加新的提示词
2. 在`MEDICAL_SCENARIOS`中添加场景描述
3. 在`SAMPLE_QUESTIONS`中添加示例问题

### 自定义模型路径
```python
assistant = MedicalAssistant("./your/custom/model/path")
```

### 批量处理自定义问题
```json
[
  {
    "question": "您的问题",
    "scenario": "diagnosis",
    "max_tokens": 512
  }
]
```

## 相关资源

### 模型资源
- **基础模型**: [Qwen3-0.6B](https://modelscope.cn/models/Qwen/Qwen3-0.6B/summary)
- **基础模型**: [Qwen3-1.7B](https://modelscope.cn/models/Qwen/Qwen3-1.7B/summary)

### 数据集资源
- **医疗数据集**: [llama2-jinyong-style](https://huggingface.co/datasets/conghao/llama2-jinyong-style)
- **中文百科数据集**: [Chinese-SimpleQA](https://huggingface.co/datasets/OpenStellarTeam/Chinese-SimpleQA)

### 工具和框架
- **训练监控**: [SwanLab](https://swanlab.cn/@ZeyiLin/qwen3-sft-medical/overview)
- **模型框架**: [Transformers](https://github.com/huggingface/transformers)
- **LoRA技术**: [PEFT](https://github.com/huggingface/peft)


## 贡献指南

欢迎提交Issue和Pull Request来改进项目！

1. Fork本项目
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个Pull Request

---

**免责声明**: 本项目提供的医疗咨询功能仅供学习和参考使用，不能替代专业医疗诊断。如有健康问题，请及时就医。


