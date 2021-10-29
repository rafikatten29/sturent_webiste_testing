from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


@given(u'user visits description page')
def open_description_page(context):
    context.driver = webdriver.Chrome(executable_path=r"C:\Users\Tammy\Documents\Rafii\sturent\chromedriver.exe")
    context.driver.get("https://sturents.com/student-accommodation/lerwick/house/stanegarth/301309")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@when(u'user selects availability "Short let"')
def select_short_let_availability(context):
    try:
        dropdown = Select(context.driver.find_element_by_xpath('//*[@id="availability-select"]'))
        dropdown.select_by_value("400823")
    except NoSuchElementException:
        print("Cannot locate availability dropdown element")


@when(u'user clicks on Book now button')
def click_on_book_now_button(context):
    try:
        buttons = context.driver.find_elements_by_xpath('//button[@data-url="https://sturents.com/house/book-now"]')
        if buttons[0].is_displayed():
            buttons[0].click()
    except NoSuchElementException:
        print("Cannot locate Book now button element")


@then(u'user is on booking page')
def check_user_on_booking_page(context):

    tabs = context.driver.window_handles
    if len(tabs) == 2:
        context.driver.switch_to.window(tabs[1])
    title = context.driver.title
    assert title == 'Property'


@then(u'user can see "Rent & Availability" title')
def check_user_can_see_rent_availability_title(context):
    try:
        status = context.driver.find_element_by_xpath('//*[@id="new--house-profile-rent-availability"]/div/h5').is_displayed()
        assert status is True
    except NoSuchElementException:
        print("Cannot locate 'Rent & Availability' title element")
        context.driver.close()


@then(u'user can see pricing information and availability')
def check_user_can_see_pricing_and_availability(context):
    try:
        status = context.driver.find_element_by_class_name("new--house-profile-rent-availability-container").is_displayed()
        assert status is True
    except NoSuchElementException:
        print("Cannot locate the pricing information and availability")
        context.driver.close()


@then(u'the property details are accurate')
def check_property_details_are_accurate(context):
    try:
        status = context.driver.find_element_by_xpath("//*[contains(text(),'17 Stanegarth, Lerwick, ZE1 0PF')]").is_displayed()
        assert status is True
    except NoSuchElementException:
        print("Cannot locate the correct property details on the page")
        context.driver.close()


@then(u'short let is preselected as a radio button')
def short_let_radio_button_is_preselected(context):
    try:
        status = context.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div[2]/div/div/main/div/form/div/div[2]/div[1]/div[2]/label[1]/label/input").is_displayed()
        assert status is True
    except NoSuchElementException:
        print("Cannot locate the short let radio button on the page")
        context.driver.close()


@then(u'user closes down browser')
def close_down_browser(context):
    context.driver.close()



