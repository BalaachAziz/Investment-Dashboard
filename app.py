from flask import Flask, render_template, request

app = Flask(__name__)

# NEW: Returns list of balances over time
def compound_interest_over_time(principal, monthly, rate, years):
    months = int(years * 12)
    monthly_rate = rate / 100 / 12
    balances = []
    current_balance = principal

    for _ in range(months):
        current_balance = current_balance * (1 + monthly_rate) + monthly
        balances.append(round(current_balance, 2))  # Save balance each month

    return balances  # List of monthly balances


@app.route("/", methods=["GET", "POST"])
def index():
    balances = None  # Will store monthly balances

    if request.method == "POST":
        principal = float(request.form["principal"])
        monthly = float(request.form["monthly"])
        rate = float(request.form["rate"])
        years = float(request.form["years"])

        balances = compound_interest_over_time(principal, monthly, rate, years)

    return render_template("index.html", balances=balances)


app.run(port=5004)
