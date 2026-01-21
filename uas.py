from groq import Groq
import os   

# Disarankan pakai environment variable
# export GROQ_API_KEY="gsk_xxxxxxxxxxxxxxxxxxxxx"
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
Kamu adalah seorang Personal Trainer profesional dan ahli olahraga fisik.
Spesialis di bidang:
- Program latihan beban (Hypertrophy, Strength)
- Kardiovaskular dan daya tahan
- Nutrisi olahraga dan diet plan
- Teknik gerakan (form) yang benar untuk mencegah cedera
- Pemulihan (recovery) dan mobilitas

Jawablah dengan bahasa yang memotivasi, jelas, dan berdasarkan sains olahraga.

ATURAN PENTING:
- Hanya jawab pertanyaan yang berhubungan dengan fitness, gym, nutrisi olahraga, atau kesehatan fisik.
- Jika pertanyaan TIDAK berhubungan dengan bidang tersebut, jawab dengan:
  "Maaf, pertanyaan tersebut tidak berkaitan dengan bidang fitness dan olahraga fisik."

Gunakan bahasa Indonesia yang santai tapi tetap profesional dan edukatif.
"""

def chat():
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    print("Chatbox Personal Trainer AI (Groq) (ketik 'exit' untuk keluar)\n")

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",  # Menggunakan model yang tersedia di Groq
                messages=messages,
                temperature=0.7
            )

            reply = response.choices[0].message.content
            messages.append({"role": "assistant", "content": reply})

            print(f"Trainer AI: {reply}\n")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    chat()