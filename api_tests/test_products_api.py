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

def test_delete_verify_login():
    url = "https://automationexercise.com/api/verifyLogin"

    response = requests.delete(url, timeout=15)
    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."

def test_verify_login_invalid_credentials():
    url = "https://automationexercise.com/api/verifyLogin"

    response = requests.post(
        url,
        data={
            "email": "invalid@example.com",
            "password": "wrongpassword"
        },
        timeout=15
    )

    data = response.json()
    print(data)
    print(data["responseCode"])

    assert response.status_code == 200
    assert data["responseCode"] == 404
    assert data["message"] == "User not found!"

import uuid

def test_create_user_account():
    url = "https://automationexercise.com/api/createAccount"

    email = f"testuser{uuid.uuid4().hex[:8]}@example.com"

    response = requests.post(
        url,
        data={
            "name": "Test User",
            "email": email,
            "password": "TestPassword123",
            "title": "Mr",
            "birth_date": "10",
            "birth_month": "5",
            "birth_year": "1995",
            "firstname": "Test",
            "lastname": "User",
            "company": "Test Company",
            "address1": "123 Test Street",
            "country": "United States",
            "zipcode": "10001",
            "state": "New York",
            "city": "New York",
            "mobile_number": "1234567890"
        },
        timeout=15
    )

    data = response.json()
    print(data)
    print(data["responseCode"])

    assert response.status_code == 200
    assert data["responseCode"] == 201
    assert data["message"] == "User created!"

def test_delete_user_account():
    email = f"testuser{uuid.uuid4().hex[:8]}@example.com"
    password = "TestPassword123"

    user_data = {
        "name": "Test User",
        "email": email,
        "password": password,
        "title": "Mr",
        "birth_date": "10",
        "birth_month": "5",
        "birth_year": "1995",
        "firstname": "Test",
        "lastname": "User",
        "company": "Test Company",
        "address1": "123 Test Street",
        "country": "United States",
        "zipcode": "10001",
        "state": "New York",
        "city": "New York",
        "mobile_number": "1234567890"
    }

    # First, create the account
    response = requests.post(
        "https://automationexercise.com/api/createAccount",
        data=user_data,
        timeout=15
    )

    assert response.json()["responseCode"] == 201

    # Then, delete the account
    response = requests.delete(
        "https://automationexercise.com/api/deleteAccount",
        data={"email": email, "password": password},
        timeout=15
    )

    data = response.json()
    print(data)

    assert response.status_code == 200
    assert data["responseCode"] == 200
    assert data["message"] == "Account deleted!"


def test_update_user_account():
    email = f"testuser{uuid.uuid4().hex[:8]}@example.com"
    password = "TestPassword123"

    user_data = {
        "name": "Test User",
        "email": email,
        "password": password,
        "title": "Mr",
        "birth_date": "10",
        "birth_month": "5",
        "birth_year": "1995",
        "firstname": "Test",
        "lastname": "User",
        "company": "Test Company",
        "address1": "123 Test Street",
        "country": "United States",
        "zipcode": "10001",
        "state": "New York",
        "city": "New York",
        "mobile_number": "1234567890"
    }

    # Create the account first
    response = requests.post(
        "https://automationexercise.com/api/createAccount",
        data=user_data,
        timeout=15
    )
    assert response.json()["responseCode"] == 201

    # Update the account
    user_data["name"] = "Updated Test User"

    response = requests.put(
        "https://automationexercise.com/api/updateAccount",
        data=user_data,
        timeout=15
    )

    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 200
    assert data["message"] == "User updated!"


def test_update_user_account():
    email = f"testuser{uuid.uuid4().hex[:8]}@example.com"
    password = "TestPassword123"

    user_data = {
        "name": "Test User",
        "email": email,
        "password": password,
        "title": "Mr",
        "birth_date": "10",
        "birth_month": "5",
        "birth_year": "1995",
        "firstname": "Test",
        "lastname": "User",
        "company": "Test Company",
        "address1": "123 Test Street",
        "country": "United States",
        "zipcode": "10001",
        "state": "New York",
        "city": "New York",
        "mobile_number": "1234567890"
    }

    # Create the account first
    response = requests.post(
        "https://automationexercise.com/api/createAccount",
        data=user_data,
        timeout=15
    )
    assert response.json()["responseCode"] == 201

    # Update the account
    user_data["name"] = "Updated Test User"

    response = requests.put(
        "https://automationexercise.com/api/updateAccount",
        data=user_data,
        timeout=15
    )

    data = response.json()
    print(data)

    assert response.status_code == 200
    assert data["responseCode"] == 200
    assert data["message"] == "User updated!"


def test_get_user_account_details():
    email = f"testuser{uuid.uuid4().hex[:8]}@example.com"

    user_data = {
        "name": "Test User",
        "email": email,
        "password": "TestPassword123",
        "title": "Mr",
        "birth_date": "10",
        "birth_month": "5",
        "birth_year": "1995",
        "firstname": "Test",
        "lastname": "User",
        "company": "Test Company",
        "address1": "123 Test Street",
        "country": "United States",
        "zipcode": "10001",
        "state": "New York",
        "city": "New York",
        "mobile_number": "1234567890"
    }

    # Create an account
    response = requests.post(
        "https://automationexercise.com/api/createAccount",
        data=user_data,
        timeout=15
    )
    assert response.json()["responseCode"] == 201

    # Retrieve that account using its email
    response = requests.get(
        "https://automationexercise.com/api/getUserDetailByEmail",
        params={"email": email},
        timeout=15
    )

    data = response.json()

    assert response.status_code == 200
    assert data["responseCode"] == 200
    assert data["user"]["name"] == "Test User"
    assert data["user"]["email"] == email