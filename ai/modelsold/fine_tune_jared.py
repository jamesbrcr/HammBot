from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import Dataset

# Loads the tokenizer and the model (currently GPT 2)
MODEL_NAME = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Set pad token if not currently set
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Load the dataset for my JHamm
def load_dataset(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    return Dataset.from_dict({"text": [line.strip() for line in lines]})

dataset = load_dataset("jared_responses.txt")

# Tokenize the Jared data
def tokenize_function(examples):
    # tokenize text
    tokenized_output = tokenizer(
        examples["text"],
        padding = "max_length",
        truncation = True,
        max_length = 128,
    )

    tokenized_output["labels"] = tokenized_output["input_ids"].copy()
    return tokenized_output

tokenized_dataset = dataset.map(tokenize_function, batched=True, remove_columns=["text"])

# Set training arguments
training_args = TrainingArguments(
    output_dir="./results",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
    logging_dir='./logs',
    logging_steps=200,
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

# Train the model
trainer.train()

# Save the model
model.save_pretrained("./jared_gpt2_finetuned")
tokenizer.save_pretrained("./jared_gpt2_finetuned")