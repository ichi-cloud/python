from flask import Flask
from decimal import Decimal, getcontext

app = Flask(__name__)

@app.route("/")
def show_pi():
    getcontext().prec = 52  # 有効桁数を52に（小数点前1桁＋小数点以下50桁）
    pi = Decimal('3.14159265358979323846264338327950288419716939937510')
    return f"円周率（π）の小数第50位まで: {pi}"
