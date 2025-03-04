from datasets import load_dataset, concatenate_datasets
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
import torch

# Load the selected datasets
dataset1 = load_dataset("csv", data_files={"train": "mental_health_conversational_data.csv"})
dataset2 = load_dataset("ShenLab/MentalChat16K")

# Merge datasets
train_dataset = concatenate_datasets([dataset1["train"], dataset2["train"]])

# Check if 'test' split exists in both datasets
if "test" in dataset1 and "test" in dataset2:
    test_dataset = concatenate_datasets([dataset1["test"], dataset2["test"]])
else:
    # If 'test' split does not exist, create a test split from the train dataset
    dataset = train_dataset.train_test_split(test_size=0.1)
    train_dataset = dataset["train"]
    test_dataset = dataset["test"]

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")

# Tokenization function
def tokenize_function(examples):
    return tokenizer(examples["conversation"], truncation=True, padding="max_length", max_length=512)

tokenized_datasets = {
    "train": train_dataset.map(tokenize_function, batched=True),
    "test": test_dataset.map(tokenize_function, batched=True)
}

# Load Pre-trained Chatbot Model
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Define Training Arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=3e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=5,
    weight_decay=0.01,
    push_to_hub=False,
)

# Trainer Setup
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
model.save_pretrained("./fine_tuned_mental_health_bot")
tokenizer.save_pretrained("./fine_tuned_mental_health_bot")

print("Fine-tuning complete! Model saved.")