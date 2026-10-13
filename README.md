# E-Commerce Test Automation Framework

## Project Overview

A Python-based UI test automation framework designed to validate core e-commerce functionality using **Selenium WebDriver, Behave (BDD), and Page Object Model (POM)**.

The framework emphasizes maintainability, reusable test components, data-driven testing, and end-to-end validation.

**Application Under Test:** [Automation Exercise](https://www.automationexercise.com/)

## Technology Stack

- **Python** — Programming language
- **Selenium WebDriver** — Browser automation
- **Behave / Gherkin** — Behavior-Driven Development (BDD)
- **Page Object Model (POM)** — Framework design pattern
- **Allure** — Test reporting
- **Git / GitHub** — Version control

## Test Coverage

The automated UI suite covers:

- **Authentication:** Login, logout, and invalid credentials
- **Product Catalog:** Product listings, details, and data-driven search
- **Shopping Cart:** Adding and removing products, quantity verification, and cart persistence
- **Checkout:** Address verification, order details, payment, and order confirmation

Testing approaches include positive and negative testing, Scenario Outlines, integration testing, and end-to-end workflows.

## Framework Architecture

The framework follows the Page Object Model to separate test logic from browser interactions.

- `features/tests/` — Gherkin feature files
- `features/steps/` — Python step definitions
- `features/environment.py` — Test setup and teardown hooks
- `pages/` — Page Object classes and locators
- `reports/` — Allure test results
- `requirements.txt` — Project dependencies

## Running the Tests

**1. Clone the repository**

```bash
git clone https://github.com/Chotika77/AutomationExerciseEcommerceProject
cd AutomationExerciseEcommerceProject
```

**2. Create and activate a virtual environment (Windows)**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the UI tests**

```bash
behave features/tests/
```

## Test Reporting

Allure is integrated for test execution reporting and failure analysis.

The generated test results are stored locally and excluded from version control using `.gitignore`.

## Project Objectives

- Develop a maintainable Python-based test automation framework.
- Implement reusable Page Objects and BDD step definitions.
- Validate critical e-commerce workflows through automated UI testing.
- Apply data-driven, positive, negative, and end-to-end testing techniques.
- Improve test reliability through explicit waits and stable element interactions.