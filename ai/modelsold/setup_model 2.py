from transformers import AutoModelForCausalLM, AutoTokenizer

# Choose a base model (GPT-2 for now)
MODEL_NAME = "gpt2"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Make sure the model is in evaluation mode
model.eval()

print("Model and tokenizer loaded successfully!")
