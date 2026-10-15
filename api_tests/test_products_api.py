import requests


def test_get_all_products():
    url = "https://automationexercise.com/api/productsList"

    response = requests.get(url, timeout=15)
    data = response.json()

    print(data)

    print(response.status_code)
    print(data["responseCode"])

    assert response.status_code == 200
    assert data["responseCode"] == 200
    assert len(data["products"]) > 0


def test_post_to_products_list():
    url = "https://automationexercise.com/api/productsList"

    response = requests.post(url, timeout=15)
    data = response.json()
    print(data)
    print(response.status_code)
    print(data["responseCode"])

    assert response.status_code == 200
    assert data["responseCode"] == 405