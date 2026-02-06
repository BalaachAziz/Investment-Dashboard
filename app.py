from flask import Flask, render_template, request

app = Flask(__name__)

def compound_interest_over_time(principal, monthly, rate, years):
    balances = []
    months = int(years*12)
    monthly_rate = rate / 12 / 100
    total = principal
    for _ in range(months):
        total = total * (1 + monthly_rate) + monthly
        balances.append(round(total, 2))
    return balances

@app.route("/", methods=["GET", "POST"])
def home():
    balances = None
    principal = monthly = rate = years = 0  # default values
    if request.method == "POST":
        try:
            principal = float(request.form["principal"])
            monthly = float(request.form["monthly"])
            rate = float(request.form["rate"])
            years = float(request.form["years"])
            balances = compound_interest_over_time(principal, monthly, rate, years)
        except ValueError:
            return "Invalid input", 400

    # Pass all variables used in your template!
    return render_template(
        "index.html",
        balances=balances,
        principal=principal,
        monthly=monthly,
        rate=rate,
        years=years
    )

if __name__ == "__main__":
    app.run()




