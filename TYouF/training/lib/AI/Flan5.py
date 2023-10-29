from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import scipy
import pipeline
def improvement(input_sentence):
    model_name = "google/flan-t5-xl"
    device='cuda:0'
    tokenizer = T5Tokenizer.from_pretrained(model_name, device_map = device,)
    model = T5ForConditionalGeneration.from_pretrained(model_name, device_map=device, torch_dtype=torch.float16,)
    input_text = "Please rephrase the following sentence in a correct way:"
    input_text += input_sentence
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")

    outputs = model.generate(input_ids,max_new_tokens=512)
    print(tokenizer.decode(outputs[0]))
input_sentence = str(input())
improvement(input_sentence)