
from flask import Flask
import requests
import pandas as pd
import time

pairs = ["EURUSD", "GBPUSD", "USDJPY"]

app = Flask(__name__)

# fake AI memory (can be upgraded to real ML later)
win = 0
loss = 0

def get_candles():
    url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=50"
    data = requests.get(url).json()

    df = pd.DataFrame(data, columns=[
        "t","o","h","l","c","v","ct","q","n","tb","tq","ig"
    ])

    df["c"] = df["c"].astype(float)
    df["o"] = df["o"].astype(float)

    return df

def generate_signal(df):

    last = df.iloc[-1]
    prev = df.iloc[-2]

    # candle body
    last_body = last["c"] - last["o"]
    prev_body = prev["c"] - prev["o"]

    # BUY condition
    if last_body > 0 and prev_body > 0:
        return "BUY"

    # SELL condition
    if last_body < 0 and prev_body < 0:
        return "SELL"

    return "HOLD"

@app.route("/")
def home():

    df = get_candles()
    signal = generate_signal(df)

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
            .small {{
                margin-top:20px;
                font-size:20px;
            }}
        </style>
    </head>

    <body>
        <h1>📊 QUTOX OTC CANDLE SYSTEM</h1>

        <div class="box">{signal}</div>

        <div class="small">
            Timeframe: 1 Minute Candle<br>
            Status: LIVE
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
