from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

def ask_ai(question):

    prompt = f"Question: {question}\nAnswer:"

    response = generator(
        prompt,
        max_new_tokens=60,
        temperature=0.7,
        do_sample=True
    )

    text = response[0]["generated_text"]

    # Remove prompt from output
    answer = text.replace(prompt, "").strip()

    return answer