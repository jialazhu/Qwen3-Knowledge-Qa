from modelscope.msdatasets import MsDataset
import json
import random
from json import JSONEncoder


# # 设置随机种子以确保可重复性
random.seed(42)

def dataset_jsonl_transfer(origin_path):
    """
    将原始数据集转换为大模型微调所需数据格式的新数据集
    """
    messages = []
    pricats = []
    # 读取旧的JSONL文件（Windows 下强制使用 UTF-8 防止解码错误）
    with open(origin_path, "r", encoding="utf-8") as file:
        for line in file:
            # 解析每一行的json数据
            data = json.loads(line)
            primary_category = data["primary_category"]
            secondary_category = data["secondary_category"]
            input = data["question"]
            output = data["answer"]

            if not pricats:
                pricats.append({
                    "category": primary_category,
                    "sec_category": {secondary_category}  # 直接创建集合
                })
            else:
                # 标记是否找到匹配的主分类
                found = False
                for cat in pricats:
                    if cat["category"] == primary_category:
                        cat["sec_category"].add(secondary_category)
                        found = True
                        break  # 找到后退出循环
                # 只有所有主分类都不匹配时才添加新项
                if not found:
                    pricats.append({
                        "category": primary_category,
                        "sec_category": {secondary_category}  # 直接创建集合
                    })


            message = {
                "instruction": f"你是一个{primary_category}学派学者，研究{secondary_category},你需要根据用户的问题，给出答案。",
                "input": f"{input}",
                "output": output,
            }
            messages.append(message)

    random.shuffle(messages)
    # messages = messages[:2000]
    # 计算分割点
    split_idx = int(len(messages) * 0.9)

    # 分割数据
    train_data = messages[:split_idx]
    val_data = messages[split_idx:]

    # 自定义编码器，处理set类型
    class SetEncoder(JSONEncoder):
        def default(self, obj):
            # 如果是set类型，转换为list
            if isinstance(obj, set):
                return list(obj)
            # 其他类型使用默认处理
            return super().default(obj)

    # 保存训练集
    with open('../dataSets/chinese-category.jsonl', 'w', encoding='utf-8') as f:
        for item in pricats:
            json.dump(item, f, ensure_ascii=False, cls=SetEncoder)
            f.write('\n')

    with open('../dataSets/chinese-train.jsonl', 'w', encoding='utf-8') as f:
        for item in train_data:
            json.dump(item, f, ensure_ascii=False)
            f.write('\n')

    # 保存验证集
    with open('../dataSets/chinese-val.jsonl', 'w', encoding='utf-8') as f:
        for item in val_data:
            json.dump(item, f, ensure_ascii=False)
            f.write('\n')

    print(f"数据集已分割完成：")
    print(f"训练集大小：{len(train_data)}")
    print(f"验证集大小：{len(val_data)}")


dataset_jsonl_transfer('../dataSets/chinese_simpleqa.jsonl')
