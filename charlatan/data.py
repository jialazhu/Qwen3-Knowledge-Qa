from modelscope.msdatasets import MsDataset
import json
import random
import os
import time
# # 设置ModelScope镜像源
# # os.environ['MODELSCOPE_ENDPOINT'] = 'https://modelscope.oss-cn-beijing.aliyuncs.com'

# # 设置随机种子以确保可重复性
random.seed(42)

PROMPT = "你是一个江湖郎中，你需要根据用户的问题，给出带有江湖气息的回答。"
def dataset_jsonl_transfer(origin_path):
    """
    将原始数据集转换为大模型微调所需数据格式的新数据集
    """
    messages = []
    # 读取旧的JSONL文件（Windows 下强制使用 UTF-8 防止解码错误）
    with open(origin_path, "r", encoding="utf-8") as file:
        for line in file:
            # 解析每一行的json数据
            data = json.loads(line)
            input = data["instruction"]
            output = data["output"]
            message = {
                "instruction": PROMPT,
                "input": f"{input}",
                "output": output,
            }
            messages.append(message)

    random.shuffle(messages)
    messages = messages[:2000]
    # 计算分割点
    split_idx = int(len(messages) * 0.9)

    # 分割数据
    train_data = messages[:split_idx]
    val_data = messages[split_idx:]

    # 保存训练集
    with open('../dataSets/金庸-train.jsonl', 'w', encoding='utf-8') as f:
        for item in train_data:
            json.dump(item, f, ensure_ascii=False)
            f.write('\n')

    # 保存验证集
    with open('../dataSets/金庸-val.jsonl', 'w', encoding='utf-8') as f:
        for item in val_data:
            json.dump(item, f, ensure_ascii=False)
            f.write('\n')

    print(f"数据集已分割完成：")
    print(f"训练集大小：{len(train_data)}")
    print(f"验证集大小：{len(val_data)}")


dataset_jsonl_transfer('../dataSets/train_jinyong.jsonl')
