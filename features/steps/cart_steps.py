from behave import when, then


@when('the user types "{keyword}" into the "What can we help you find?" search bar')
def step_impl(context, keyword):
    context.app.search_results_page.type_search_query(keyword)


@when('the user presses "Enter"')
def step_impl(context):
    context.app.search_results_page.press_enter_in_search()


@then('the search results page should be displayed')
def step_impl(context):
    context.app.search_results_page.assert_results_page_displayed()


@then('each product card should show a title, a price, and an image')
def step_impl(context):
    context.app.search_results_page.are_product_cards_valid()
