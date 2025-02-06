from transformers import AutoModelForCausalLM, AutoTokenizer

# load trained jared model
MODEL_PATH = "./jared_gpt2"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)

# Set pad token if not already set
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Make sure the model is in evaluation mode
model.eval()

print("Fine-tuned Jared model and tokenizer loaded successfully!")

# TODO - create frontend to take user input
input_text = "Hey Jared, how are you?"

# Tokenize the input
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Attention mask for generating output as seen in function below
attention_mask = tokenizer.encode(input_text, return_tensors = "pt")

try:
    # Generate output
    output = model.generate(
        input_ids, 
        #attention_mask = attention_mask,
        max_length = 50, 
        do_sample = True,
        temperature = 0.7, # Changes the randomness of response
        top_k = 50, # Samples from n number of tokens
        pad_token_id = tokenizer.eos_token_id,
        eos_token_id = tokenizer.eos_token_ids,
    )

    # Decode generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    print(generated_text)

except Exception as e:
    print(f"Error during text generation: {str(e)}")
    print(f"Input shape: {input_ids.shape}")
    print(f"Model config: {model.config}")
