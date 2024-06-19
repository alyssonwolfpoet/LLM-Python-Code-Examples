from transformers import pipeline

# Initialize the text generation pipeline
text_generator = pipeline("text-generation")

# Prompt the LLM with a starting sentence
prompt = "Once upon a time, there was a brave knight..."

# Generate text based on the prompt
generated_text = text_generator(prompt)

# Print the generated text
print(generated_text[0]["generated_text"])