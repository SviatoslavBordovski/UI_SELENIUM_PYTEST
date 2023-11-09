class LoginSignupLocators:
    email_address_xpath = "//input[@data-qa='login-email']"
    password_xpath = "//input[@data-qa='login-password']"
    login_button_xpath = "//button[@data-qa='login-button']"
    incorrect_email_password_xpath = "//p[text()='%s']"
    login_signup_topnav_link_xpath = "//a[text()=' Signup / Login']"
    name_xpath = "//input[@data-qa='signup-name']"
    signup_email_xpath = "//input[@data-qa='signup-email']"
    signup_button_xpath = "//button[@data-qa='signup-button']"
    title_radio_button_id = "id_gender1"
    input_name_field_id = "name"
    input_password_field_id = "password"
    select_dd_date_id = "uniform-days"
    select_dd_month_id = "uniform-months"
    select_dd_year_id = "uniform-years"
    newsletter_checkbox_id = "newsletter"
    special_offers_checkbox_id = "optin"
    days_xpath = "//select[@id='days']/option"
    months_xpath = "//select[@id='months']/option"
    years_xpath = "//select[@id='years']/option"
    address_information_value_xpath = "//p[@class='required form-group']"
    create_account_button_xpath = "//button[@data-qa='create-account']"
    account_created_header_xpath = "//h2[@data-qa='account-created']/b"
    registration_continue_button_xpath = "//a[@data-qa='continue-button']"
    user_name_navbar_xpath = "//a/b[contains(text(), '%s')]"
    delete_account_button_xpath = "//a[text()=' Delete Account']"
    logout_button_xpath = "//a[text()=' Logout']"
    close_advertising_button_xpath = "//span[text()='Close']"
    close_advertising_x_button_id = "dismiss-button"
    login_header_xpath = "//div[@class='login-form']/h2"
    full_signup_form_xpath = "//h2/b[text()='Enter Account Information']"
