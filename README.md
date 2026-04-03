# COVID-19 Interactive Dashboard

## Setup Instructions

### 1. Install Python if not already installed
Download from https://www.python.org/downloads/

### 2. Install required libraries
Open a terminal.
Navigate to this folder then run:

pip install flask plotly pandas

### 3. Run the app
In the same terminal run:

flask run

Or

python app.py

### 4. Open in browser
Go to: http://127.0.0.1:5000

## File Structure

covid_app/
├── app.py
├── COVID_Country_Sample.csv
├── README.md
└── templates/
    └── index.html

## Features
- Interactive line chart switchable by country and metric
- Metrics: New Cases, New Vaccinations, New Deaths
- Live JSON data fetching
- Responsive layout that works on mobile and desktop
- Insights section with data caveats
