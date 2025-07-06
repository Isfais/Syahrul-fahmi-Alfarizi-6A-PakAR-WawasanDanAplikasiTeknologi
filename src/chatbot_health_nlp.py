"""
Studi Kasus 3: Chatbot Kesehatan Sederhana Berbasis NLP
"""

import random

RESPONSES = {
    "demam": "Jika Anda mengalami demam ringan, pastikan cukup istirahat dan minum air putih.",
    "batuk": "Batuk kering bisa jadi gejala awal flu. Hindari debu dan minum air hangat.",
    "covid": "Jika Anda merasa gejala COVID-19, lakukan tes antigen atau PCR dan isolasi mandiri."
}

def chatbot_response(input_text):
    input_text = input_text.lower()
    for keyword in RESPONSES:
        if keyword in input_text:
            return RESPONSES[keyword]
    return "Maaf, saya belum memahami gejala tersebut. Konsultasikan ke dokter ya."

# Contoh penggunaan:
# print(chatbot_response("Saya merasa batuk sejak kemarin."))
