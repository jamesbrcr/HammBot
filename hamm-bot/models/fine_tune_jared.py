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
        return_tensors = "pt",
    )

    tokenized_output["labels"] = tokenized_output["input_ids"].clone()
    return tokenized_output

tokenized_dataset = dataset.map(tokenize_function, batched = True, remove_columns = ["text"])

# Set training arguments
training_args = TrainingArguments(
    output_dir = "./jared_gpt2", #Directory where tuned model will be saved
    overwrite_output_dir = True,
    num_train_epochs = 3, # Number of training epochs
    per_device_train_batch_size = 4, # Size of training batches
    save_steps = 500, # Save the trained model every 500 steps
    save_total_limit = 2, # Only keep the last 2 models to prevent crowding and slowness
    logging_dir = "./logs", # Directory for stored logs
    logging_steps = 100, # Log every 100 steps in the training
    evaluation_strategy = "no", # No evaluation during training
    prediction_loss_only = True,
)

# Create the trainer
trainer = Trainer(
    model = model,
    args = training_args,
    train_dataset = tokenized_dataset,
)

# Fine-tune the model with .train() function

trainer.train()

# Save the tuned model and tokenizer
model.save_pretrained("./jared_gpt2")
tokenizer.save_pretrained("./jared_gpt2")
