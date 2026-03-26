from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Load dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'superstore.csv')
df = pd.read_csv(DATA_PATH, encoding='latin1')

@app.route('/total-sales', methods=['GET'])
def total_sales():
    total = round(float(df['Sales'].sum()), 2)
    return jsonify({'total_sales': total})

@app.route('/sales-by-region', methods=['GET'])
def sales_by_region():
    result = df.groupby('Region')['Sales'].sum().round(2).to_dict()
    return jsonify(result)

@app.route('/profit-by-category', methods=['GET'])
def profit_by_category():
    result = df.groupby('Category')['Profit'].sum().round(2).to_dict()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)