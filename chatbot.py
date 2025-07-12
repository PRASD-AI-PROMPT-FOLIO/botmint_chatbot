import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_bot(user_input, hospital_name="BotMint Care"):
    prompt = f"""
You are a friendly chatbot for a hospital named {hospital_name}.
Here are the details:

Departments: Cardiology, ENT, Pediatrics, General Medicine.
Doctors: Dr. Ramesh (Cardiologist), Dr. Anitha (ENT), Dr. Vinay (Pediatrician)
Opening Hours: 9 AM to 8 PM
Location: Hyderabad, India

Now answer the user's question: {user_input}
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}],
        temperature=0.5,
        max_tokens=300
    )

    return response.choices[0].message.content
