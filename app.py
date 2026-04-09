
from flask import Flask
import random
import time

app = Flask(__name__)

# fake AI memory (can be upgraded to real ML later)
win = 0
loss = 0

def ai_signal():
    global win, loss

    r = random.randint(1, 100)

    if r > 75:
        signal = "BUY"
        win += 1
    elif r < 25:
        signal = "SELL"
        win += 1
    else:
        signal = "HOLD"
        loss += 1

    accuracy = (win / (win + loss)) * 100 if (win + loss) > 0 else 0

    return signal, accuracy

@app.route("/")
def home():
    signal, acc = ai_signal()

    color = "#22c55e" if signal == "BUY" else "#ef4444" if signal == "SELL" else "#f59e0b"

    return f"""
    <html>
    <head>
        <meta http-equiv="refresh" content="3">
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
                margin:20px;
            }}
            .card {{
                background:#111827;
                padding:20px;
                border-radius:15px;
                display:inline-block;
            }}
        </style>
    </head>

    <body>
        <h1>📊 QUTOX OTC AI SYSTEM</h1>

        <div class="card">
            <div class="box">{signal}</div>
            <h2>Accuracy: {acc:.2f}%</h2>
            <p>Auto refresh every 3 seconds</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
