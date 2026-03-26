import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

def test_total_sales():
    client = app.test_client()
    response = client.get('/total-sales')
    assert response.status_code == 200
    data = response.get_json()
    assert 'total_sales' in data
    assert isinstance(data['total_sales'], float)

def test_sales_by_region():
    client = app.test_client()
    response = client.get('/sales-by-region')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)

def test_profit_by_category():
    client = app.test_client()
    response = client.get('/profit-by-category')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)