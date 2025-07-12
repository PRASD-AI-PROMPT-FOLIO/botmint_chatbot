import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_bot(user_input, hospital_name="BotMint Care"):
    system_prompt = f"""
You are a friendly and helpful chatbot for a hospital named {hospital_name}.
Here are the hospital details:

- Departments: Cardiology, ENT, Pediatrics, General Medicine.
- Doctors: Dr. Ramesh (Cardiologist), Dr. Anitha (ENT), Dr. Vinay (Pediatrician)
- Opening Hours: 9 AM to 8 PM
- Location: Hyderabad, India

Answer questions based on this info in a helpful and polite tone.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.5,
        max_tokens=300
    )

    return response['choices'][0]['message']['content']
