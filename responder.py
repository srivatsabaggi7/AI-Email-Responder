from transformers import pipeline

# Load a pre-trained transformer for text generation
'''generator = pipeline("text-generation", model="gpt2")

def generate_response(email_text):
    prompt = f"Reply to the following email professionally:\n\n{email_text}\n\nResponse:"
    response = generator(prompt, max_new_tokens=100, do_sample=True, temperature=0.7)
    return response[0]["generated_text"].split("Response:")[-1].strip()
'''

'''
# Load the fine-tuned model
model_path = "gpt2-finetuned-email"
generator = pipeline("text-generation", model=model_path)

def generate_response(email_text):
    prompt = f"Reply to the following email professionally:\n\n{email_text}\n\nResponse:"
    response = generator(
        prompt,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        num_return_sequences=1
    )
    # Improved response extraction
    generated_text = response[0]["generated_text"]
    # Find the last occurrence of 'Response:' and extract everything after it
    if "Response:" in generated_text:
        reply = generated_text.split("Response:")[-1].strip()
        # Remove any repeated input text from the reply
        if email_text in reply:
            reply = reply.replace(email_text, "").strip()
        return reply
    return "I apologize, but I couldn't generate a proper response. Please try again."
'''

from transformers import pipeline, GPT2LMHeadModel, GPT2Tokenizer

model_path = "./gpt2-finetuned-email"

tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_response(email):
    # Format prompt to be more specific and guide the model better
    prompt = f"Generate a professional business email response to the following inquiry:\n\nIncoming email: {email}\n\nResponse:"
    
    result = generator(
        prompt,
        max_new_tokens=200,
        do_sample=True,
        top_p=0.92,        # Slightly increased for better coherence
        temperature=0.6,    # Reduced for more focused responses
        repetition_penalty=1.2,  # Prevent repetitive text
        no_repeat_ngram_size=3,  # Avoid repeating phrases
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id
    )
    
    # Clean up the response
    response = result[0]["generated_text"]
    
    # Extract only the generated response part
    if "Response:" in response:
        response = response.split("Response:")[-1].strip()
    
    # Remove any echoed input
    if email in response:
        response = response.replace(email, "").strip()
        
    # Remove any repeated "Response:" markers
    response = response.replace("### RESPONSE:", "").replace("Response:", "").strip()
    
    # Clean up any HTML entities
    response = response.replace("&#39;", "'").strip()
    
    return response

if __name__ == "__main__":
    email = input("Paste an email:\n")
    print("\nGenerated Response:\n", generate_response(email))