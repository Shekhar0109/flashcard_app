from transformers import pipeline

# Load the text generation model once
generator = pipeline("text-generation", model="gpt2", max_new_tokens=100)

def generate_flashcards(text, num_flashcards=5):
    prompt = f"Generate {num_flashcards} flashcards based on this text:\n{text}\nFormat: Question and Answer."
    output = generator(prompt)[0]["generated_text"]
    
    flashcards = []
    lines = output.split("\n")
    for line in lines:
        if "?" in line:
            q, *a = line.split("?")
            question = q.strip() + "?"
            answer = a[0].strip() if a else "N/A"
            flashcards.append({"question": question, "answer": answer})
    return flashcards
