from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load pre-trained model
MODEL_NAME = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

def get_chatbot_response(user_input, sentiment):
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    
    # Generate response
    output = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

    # Modify response based on sentiment
    if sentiment == "negative":
        response += " I understand this might be tough. You're not alone."
    
    return response