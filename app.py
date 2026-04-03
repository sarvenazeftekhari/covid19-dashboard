from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load and clean data
df = pd.read_csv("COVID_Country_Sample.csv", parse_dates=["date"])

# Fill missing numeric values with 0
df["new_cases"] = df["new_cases"].fillna(0)
df["new_deaths"] = df["new_deaths"].fillna(0)
df["new_vaccinations"] = df["new_vaccinations"].fillna(0)
df["vaccinations_per_hundred"] = df["vaccinations_per_hundred"].fillna(0)

# Remove extreme outliers: cap new_cases above 99th percentile per country
p99 = df.groupby("country")["new_cases"].transform(lambda x: x.quantile(0.99))
df["new_cases"] = df["new_cases"].clip(upper=p99)

# Sort by date
df = df.sort_values("date")

countries = sorted(df["country"].unique().tolist())
date_min = df["date"].min().strftime("%B %Y")
date_max = df["date"].max().strftime("%B %Y")

@app.route("/")
def index():
    return render_template(
        "index.html",
        countries=countries,
        date_min=date_min,
        date_max=date_max
    )

@app.route("/data")
def data():
    country = request.args.get("country", "Canada")
    metric = request.args.get("metric", "new_cases")
    filtered = df[df["country"] == country][["date", metric]].copy()
    filtered["date"] = filtered["date"].dt.strftime("%Y-%m-%d")
    return jsonify(filtered.to_dict(orient="list"))

if __name__ == "__main__":
    app.run(debug=True)