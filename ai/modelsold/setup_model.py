from transformers import AutoModelForCausalLM, AutoTokenizer

# Choose a base model (GPT-2 for now)
MODEL_NAME = "gpt2"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Make sure the model is in evaluation mode
model.eval()

print("Model and tokenizer loaded successfully!")

input_text = "Hey, how are you?"
input_ids = tokenizer.encode(input_text, return_tensors="pt")

output = model.generate(input_ids, max_length=50, do_sample=True)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)
