import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
def predict(messages, model, tokenizer):
    if torch.backends.mps.is_available():
        device = "mps"
    elif torch.cuda.is_available():
        device = "cuda"
    else:
        device = "cpu"

    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    model_inputs = tokenizer([text], return_tensors="pt").to(device)

    generated_ids = model.generate(model_inputs.input_ids, max_new_tokens=2048)
    generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]


    return response


# 加载原下载路径的tokenizer和model
# 使用实际下载的目录名，并根据设备选择合适的dtype
model_dir = "../models/Qwen/Qwen3-0___6B"
if torch.cuda.is_available():
    load_dtype = torch.float16
else:
    load_dtype = torch.float32

tokenizer = AutoTokenizer.from_pretrained(model_dir, use_fast=False, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_dir, device_map="auto", torch_dtype=load_dtype)

test_texts = {
    'instruction': "你是一个江湖郎中，你需要根据用户的问题，给出带有江湖气息的回答。",
    'input': "医生，我最近被诊断为糖尿病，听说碳水化合物的选择很重要，我应该选择什么样的碳水化合物呢？"
}

instruction = test_texts['instruction']
input_value = test_texts['input']

messages = [
    {"role": "system", "content": f"{instruction}"},
    {"role": "user", "content": f"{input_value}"}
]
response = predict(messages, model, tokenizer)
print(response)