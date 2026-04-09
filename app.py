
from flask import Flask
import random
import time

pairs = ["EURUSD", "GBPUSD", "USDJPY"]

app = Flask(__name__)

# fake AI memory (can be upgraded to real ML later)
win = 0
loss = 0

def ai_signal():
    pair = random.choice(pairs)
    r = random.randint(1, 100)

    if r > 70:
        signal = "BUY"
    elif r < 30:
        signal = "SELL"
    else:
        signal = "HOLD"

    return pair, signal

@app.route("/")
def home():

    pair, signal = ai_signal()

    color = "#22c55e" if signal == "BUY" else "#ef4444" if signal == "SELL" else "#f59e0b"

    return f"""
    <html>
    <head>
        <meta http-equiv="refresh" content="60">
        <title>OTC AI SIGNALS</title>
        <style>
            body {{
                background:#0f172a;
                color:white;
                text-align:center;
                font-family:Arial;
                margin-top:80px;
            }}
            .box {{
                font-size:60px;
                font-weight:bold;
                color:{color};
            }}
        </style>
    </head>

    <body>
        <h1>📊 QUTOX OTC AI SYSTEM</h1>

        <h2>Pair: {pair}</h2>

        <div class="box">{signal}</div>

        <p>Auto refresh every 5 seconds</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
