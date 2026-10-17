import requests
import os
from dotenv import load_dotenv

load_dotenv()


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

def test_get_all_brands():
    url = "https://automationexercise.com/api/brandsList"

    response = requests.get(url, timeout=15)
    data = response.json()
    print(data)
    print(response.status_code)
    print(data["responseCode"])

    assert response.status_code == 200
    assert data["responseCode"] == 200
    assert len(data["brands"]) > 0

def test_put_to_brands_list():
    url = "https://automationexercise.com/api/brandsList"

    response = requests.put(url, timeout=15)
    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 405

def test_search_product():
    url = "https://automationexercise.com/api/searchProduct"

    response = requests.post(
        url,
        data={"search_product": "top"},
        timeout=15
    )
    data = response.json()
    print(data["responseCode"])
    print(data["products"])

    assert response.status_code == 200
    assert data["responseCode"] == 200
    assert len(data["products"]) > 0

def test_search_product_without_parameter():
    url = "https://automationexercise.com/api/searchProduct"

    response = requests.post(url, timeout=15)
    data = response.json()
    print(data["responseCode"])

    assert response.status_code == 200
    assert data["responseCode"] == 400

def test_verify_login_valid_credentials():
    url = "https://automationexercise.com/api/verifyLogin"

    response = requests.post(
        url,
        data={
            "email": os.getenv("TEST_USER_EMAIL"),
            "password": os.getenv("TEST_USER_PASSWORD")
        },
        timeout=15
    )

    data = response.json()
    print(data)
    print("Email loaded:", bool(os.getenv("TEST_USER_EMAIL")))
    print("Password loaded:", bool(os.getenv("TEST_USER_PASSWORD")))

    assert response.status_code == 200
    assert data["responseCode"] == 200
    assert data["message"] == "User exists!"

def test_verify_login_without_email():
    url = "https://automationexercise.com/api/verifyLogin"

    response = requests.post(
        url,
        data={"password": os.getenv("TEST_USER_PASSWORD")},
        timeout=15
    )

    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 400
    assert data["message"] == "Bad request, email or password parameter is missing in POST request."