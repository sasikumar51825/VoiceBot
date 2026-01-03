from stt import record_audio, speech_to_text
from tts import speak
from chatbot import ask_gpt, question_bank

def main():
    print("Welcome to VoiceBot Interview Coach")

    for question in question_bank:
        print(f"\nQuestion: {question}")
        speak(question)

        # Record your answer
        audio = record_audio(duration=7)
        answer = speech_to_text(audio)
        print(f"Your answer: {answer}")

        # Get GPT feedback
        feedback = ask_gpt(question, answer)
        print(f"Feedback: {feedback}")
        speak(feedback)

if __name__ == "__main__":
    main()
