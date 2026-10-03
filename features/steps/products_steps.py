from behave import given, when, then


@given('the user is on the Products page')
def step_impl(context):
    context.app.main_page.open_products_page(context.base_url)
    context.app.products_page.assert_catalog_displayed()


@when('the user navigates to the Products page')
def step_impl(context):
    context.app.main_page.open_products_page(context.base_url)
    # context.app.main_page.open_products_page()
    # print("URL:", context.driver.current_url)
    # print("WINDOWS:", len(context.driver.window_handles))


@when('the user searches for "{search_term}"')
def step_impl(context, search_term):
    context.app.products_page.search_for_product(search_term)


@then('the Searched Products section should be displayed')
def step_impl(context):
    context.app.products_page.assert_searched_products_displayed()


@then('products matching "{search_term}" should be displayed')
def step_impl(context, search_term):
    context.app.products_page.assert_products_matching_search_term(search_term)


@then('the product catalog should be displayed')
def step_impl(context):
    context.app.products_page.assert_catalog_displayed()


@when('the user opens a product')
def step_impl(context):
    context.app.products_page.open_product(context.base_url)
    # context.app.products_page.open_product()


@then('the product details should display')
def step_impl(context):
    context.app.product_details_page.assert_product_details_panel_displayed()
    for row in context.table:
        field_name = row['field']
        context.app.product_details_page.assert_field_present(field_name)
