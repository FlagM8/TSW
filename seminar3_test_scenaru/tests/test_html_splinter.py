from pytest_bdd import scenarios, given, when, then
import pytest
from splinter import Browser

pytestmark = pytest.mark.html_splinter

scenarios('../features/todo_html_splinter.feature')

@pytest.fixture
def browser():
    with Browser("chrome", headless=True) as browser:
        yield browser

@given("aplikace běží")
def app_runs():
    pass

@when("otevřu domovskou stránku v prohlížeči")
def open_homepage(browser):
    browser.visit("http://localhost:5000/")

@then('uvidím nadpis "My Tasks" v prohlížeči')
def see_title_in_browser(browser):
    assert browser.is_text_present("My Tasks", wait_time=3), browser.html
