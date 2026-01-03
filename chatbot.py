from gpt4all import GPT4All
import os

# Path to your GGUF model
model_path = os.path.join(os.path.dirname(__file__), "models", "q4_0-orca-mini-3b.gguf")

# Load model
gpt = GPT4All(model_path, allow_download=False)

# Questions for practice
question_bank = [
    "Tell me about yourself.",
    "Explain your projects.",
    "Describe a challenge you faced and how you solved it."
]

def ask_gpt(question, answer):
    prompt = f"""
You are an interview coach.

You will receive:
Question: {question}
Answer: {answer}

Give feedback only. DO NOT ask any follow-up questions.

Your feedback must include:

1) Short evaluation (1–2 sentences)
2) What was missing or weak
3) How to improve
4) A revised example answer

Keep it supportive and concise.
"""

    response = gpt.generate(prompt)
    return response

