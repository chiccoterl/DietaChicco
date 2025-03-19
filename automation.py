import os
import requests

def send_telegram_message(message, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
    }
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print("Errore nell'invio del messaggio:", response.text)
    else:
        print("Messaggio inviato correttamente!")
    return response.json()

def main():
    # Recupera token e chat id dalle variabili d'ambiente
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        raise Exception("Errore: TELEGRAM_TOKEN o TELEGRAM_CHAT_ID non sono impostati.")
    
    # Qui inserisci la logica per recuperare e filtrare le offerte.
    # Per ora usiamo un messaggio fisso di esempio.
    message = (
        "Buongiorno!\n"
        "Ecco le offerte di oggi:\n"
        "- Yogurt vegetale in offerta da Carrefour Express\n"
        "- Insalata pronta con pollo da Conad\n"
        "- Zuppa riscaldabile da Lidl\n"
        "\nBuona spesa!"
    )
    
    send_telegram_message(message, token, chat_id)

if __name__ == "__main__":
    main()
