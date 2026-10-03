Feature: Automation Exercise E-Commerce Functionality

  As a customer
  I want to use the core e-commerce functionality
  So that I can register, authenticate, find products, manage my cart, and place orders


  # ==================== REGISTRATION ====================


 @smoke @regression
  Scenario: User can open the Signup Login page
    Given the user opens the Automation Exercise website
    When the user navigates to the Signup Login page
    Then the Login form should be displayed
    And the "Login to your account" heading should be visible
    And the Email and Password fields should be visible
    And the Login button should be visible


  @smoke @regression
  Scenario: Registered user can log in with valid credentials
    Given a registered user account exists
    And the user is on the Signup Login page
    When the user enters valid login credentials
    And clicks the Login button
    Then the user should be logged in successfully


  @negative @regression
  Scenario Outline: User cannot log in with invalid credentials
    Given the user is on the Signup Login page
    When the user enters "<email>" and "<password>"
    And clicks the Login button
    Then the invalid login error message should be displayed

    Examples:
      | email                 | password         |
      | nonexistent@test.com  | TestPassword123  |
      | valid_user@test.com   | WrongPassword123 |
      | invalid@test.com      | InvalidPassword  |
      | sisona.chkuaseli112@gmail.com | WrongPassword123 |


  @regression
  Scenario: Logged-in user can log out
    Given the user is logged in
    When the user clicks the Logout button
    Then the user should be logged out
    And the Signup Login page should be displayed



  # ==================== PRODUCTS ====================

  @smoke @regression
  Scenario: User can view product details
    Given the user opens the Automation Exercise website
    When the user navigates to the Products page
    Then the product catalog should be displayed
    When the user opens a product
    Then the product details should display
      | field        |
      | name         |
      | category     |
      | price        |
      | availability |
      | condition    |
      | brand        |


  @regression
  Scenario Outline: User can search for products
    Given the user is on the Products page
    When the user searches for "<search_term>"
    Then the Searched Products section should be displayed
    And products matching "<search_term>" should be displayed

    Examples:
      | search_term |
      | top         |
      | tshirt      |
      | jeans       |


  # ==================== SHOPPING CART ====================

  @smoke @regression
  Scenario: User can add multiple products to the cart
    Given the user is on the Products page
    When the user adds two different products to the cart
    And opens the shopping cart
    Then both products should be displayed in the cart
    And the correct price should be displayed for each product
    And the correct quantity should be displayed for each product
    And the correct total should be displayed for each product


  @regression
  Scenario Outline: Cart reflects selected product quantity
    Given the user opens a product details page
    When the user sets the product quantity to "<quantity>"
    And adds the product to the cart
    And opens the shopping cart
    Then the product quantity should be "<quantity>"

    Examples:
      | quantity |
      | 1        |
      | 2        |
      | 4        |


  @regression
  Scenario: User can remove a product from the cart
    Given the user has a product in the shopping cart
    When the user opens the shopping cart
    And removes the product
    Then the product should no longer be displayed in the cart


  @regression @e2e
  Scenario: Shopping cart persists after user login
    Given a registered user account exists
    And the user is not logged in
    When the user adds a product to the cart
    And navigates to the Signup Login page
    And logs in with valid credentials
    And opens the shopping cart
    Then the previously added product should still be displayed in the cart


  # ==================== CHECKOUT AND ORDER ====================

  @negative @regression
  Scenario: Unauthenticated user is required to authenticate during checkout
    Given the user is not logged in
    And the user has a product in the shopping cart
    When the user proceeds to checkout
    Then the user should be prompted to register or log in


  @regression
  Scenario: Checkout displays correct address and order information
    Given a registered user is logged in
    And the user has a product in the shopping cart
    When the user proceeds to checkout
    Then the delivery address should match the registered user address
    And the billing address should match the registered user address
    And the order details should match the shopping cart


  @smoke @regression @e2e
  Scenario: Registered user can complete an order successfully
    Given a registered user is logged in
    And the user has a product in the shopping cart
    When the user proceeds to checkout
    And reviews the delivery and order information
    And enters an order comment
    And proceeds to payment
    And enters valid payment information
    And confirms the order
    Then the order should be placed successfully
    And an order confirmation message should be displayed