from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


@given(u'user is on booking page')
def user_on_booking_page(context):
    context.driver = webdriver.Chrome(executable_path=r"C:\Users\Tammy\Documents\Rafii\sturent\chromedriver.exe")
    context.driver.get("https://sturents.com/student-accommodation/lerwick/house/stanegarth/301309")
    context.driver.maximize_window()
    context.driver.implicitly_wait(time_to_wait=10)
    try:
        dropdown = Select(context.driver.find_element_by_xpath('//*[@id="availability-select"]'))
        dropdown.select_by_value("400823")
    except NoSuchElementException:
        print("Cannot locate availability dropdown element")
    try:
        buttons = context.driver.find_elements_by_xpath('//button[@data-url="https://sturents.com/house/book-now"]')
        if buttons[0].is_displayed():
            buttons[0].click()
    except NoSuchElementException:
        print("Cannot locate Book now button element")
    tabs = context.driver.window_handles
    if len(tabs) == 2:
        context.driver.switch_to.window(tabs[1])


@given(u'user selects "{availability}" radio button')
def user_selects_short_let_radio_button(context):
    try:
        context.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div[2]/div/div/main/div/form/div/div[2]/div[1]/div[2]/label[1]/label/input").click()
    except NoSuchElementException:
        print("Cannot locate the short let radio button on the page")


@given(u'user chooses "{move_in_date}" as move in date')
def user_chooses_move_in_date(context, move_in_date):

    stripped = move_in_date.replace('-','')
    try:
        context.driver.find_element_by_xpath("//input[@placeholder = 'Select move in']").send_keys(stripped)
        context.driver.implicitly_wait(10)
    except NoSuchElementException:
        print("Cannot locate the move in date picker on the page")


@given(u'user chooses "{move_out_date}" as move out date')
def user_chooses_move_out_date(context, move_out_date):
    stripped = move_out_date.replace('-', '')
    try:
        context.driver.find_element_by_xpath("//input[@placeholder = 'Select move out']").send_keys(stripped)
    except NoSuchElementException:
        print("Cannot locate the move out date picker on the page")


@given(u'user chooses "{title}" as title')
def user_chooses_title(context, title):
    try:
        dropdown = Select(context.driver.find_elements_by_xpath("//select[@placeholder = 'Select title']"))
        dropdown.select_by_value(title)
    except NoSuchElementException:
        print("Cannot locate title dropdown element")


@given(u'user enters "{first_name}" as first name')
def user_enters_first_name(context, first_name):
    try:
        elements = context.driver.find_elements_by_xpath("//input[@placeholder = 'First name']")
        elements[0].send_keys(first_name)
    except NoSuchElementException:
        print("Cannot locate the first name field on the page")


@given(u'user enters "{last_name}" as last name')
def user_enters_last_name(context, last_name):
    try:
        elements = context.driver.find_elements_by_xpath("//input[@placeholder = 'Email address']")
        elements[0].send_keys(last_name)
    except NoSuchElementException:
        print("Cannot locate the last name field on the page")


@given(u'user enters "{email}" as email')
def user_enters_email(context, email):
    try:
        elements = context.driver.find_elements_by_xpath("//input[@placeholder = 'Email address']")
        elements[0].send_keys(email)
        context.driver.find_element_by_xpath("//input[@placeholder = 'Confirm your email address']").send_keys(email)
    except NoSuchElementException:
        print("Cannot locate the email fields on the page")


@given(u'user enters "{phone_num}" as phone number')
def user_enters_phone_num(context, phone_num):
    try:
        elements = context.driver.find_element_by_xpath("//input[@placeholder = 'Phone number']")
        elements[0].semdKeys(phone_num)
    except NoSuchElementException:
        print("Cannot locate the phone num field on the page")


@given(u'user chooses "{nationality}" as nationality')
def user_chooses_nationality(context, nationality):
    try:
        dropdown = Select(context.driver.find_element_by_xpath("//select[@placeholder = 'Select nationality']"))
        dropdown.select_by_value(nationality)
    except NoSuchElementException:
        print("Cannot locate nationality dropdown element")


@given(u'user chooses "{country}" as country')
def user_chooses_country(context, country):
    try:
        dropdown = Select(context.driver.find_element_by_xpath("//select[@placeholder = 'Select country of residence']')"))
        dropdown.select_by_value(country)
    except NoSuchElementException:
        print("Cannot locate country dropdown element")


@given(u'user enters "{property_num}" as property number')
def user_enters_property_num(context, property_num):
    try:
        context.driver.find_element_by_xpath("//input[@placeholder = 'Property number/name']").send_keys(property_num)
    except NoSuchElementException:
        print("Cannot locate the property num field on the page")


@given(u'user enters "{street}" as street')
def user_enters_street(context, street):
    try:
        context.driver.find_element_by_xpath("//input[@placeholder = 'Street']").send_keys(street)
    except NoSuchElementException:
        print("Cannot locate the street field on the page")


@given(u'user enters "{city}" as city')
def user_enters_city(context, city):
    try:
        context.driver.find_element_by_xpath("//input[@placeholder = 'Town/City']").send_keys(city)
    except NoSuchElementException:
        print("Cannot locate the city field on the page")


@given(u'user enters "{postcode}" as postcode')
def user_enters_postcode(context, postcode):
    try:
        context.driver.find_element_by_xpath("//input[@placeholder = 'Postcode']").send_keys(postcode)
    except NoSuchElementException:
        print("Cannot locate the postcode field on the page")
