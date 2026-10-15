import requests


def test_get_all_products():
    url = "https://automationexercise.com/api/productsList"

    response = requests.get(url, timeout=15)
    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 200
    assert len(data["products"]) > 0