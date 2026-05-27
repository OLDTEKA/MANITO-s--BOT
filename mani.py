import requests
import time
import random

TOKEN = "8911372023:AAGq3nYDTqDOio5A-OUYaXnx1R7vUDsTfUQ"
URL = f"https://api.telegram.org/bot{TOKEN}"

offset = None

def generate_vip():
    matches = [
        ("Arsenal", "Chelsea"),
        ("Barcelona", "Valencia"),
        ("Bayern", "Dortmund")
    ]

    text = "💎 VIP PREDICTIONS 💎\n\n"

    for home, away in matches:
        hs = random.randint(0, 3)
        away_score = random.randint(0, 3)

        if hs > away_score:
            winner = home
        elif away_score > hs:
            winner = away
        else:
            winner = "Draw"

        text += f"{home} vs {away}\n"
        text += f"Score: {hs}-{away_score}\n"
        text += f"Winner: {winner}\n\n"

    return text

print("Bot running...")

while True:
    try:
        response = requests.get(URL + f"/getUpdates?offset={offset}")
        data = response.json()

        for update in data["result"]:
            offset = update["update_id"] + 1

            if "message" in update:
                text = update["message"].get("text", "")
                chat_id = update["message"]["chat"]["id"]

                if text == "/start":
                    requests.get(
                        URL + f"/sendMessage?chat_id={chat_id}&text=🤖 VIP Bot Active! Send /vip"
                    )

                elif text == "/vip":
                    vip_text = generate_vip()
                    requests.get(
                        URL + f"/sendMessage?chat_id={chat_id}&text={vip_text}"
                    )

    except Exception as e:
        print("Error:", e)

    time.sleep(2)
