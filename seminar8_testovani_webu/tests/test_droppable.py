from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

scenarios('../features/droppable.feature')

@given("otevřu stránku s drag and drop")
def open_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://jqueryui.com/droppable/")
    context.driver.switch_to.frame(0)

@when('přetáhnu prvek "Drag me to my target" na target')
def drag_and_drop(context):
    source = context.driver.find_element(By.ID, "draggable")
    target = context.driver.find_element(By.ID, "droppable")
    ActionChains(context.driver).drag_and_drop(source, target).perform()
    context.target = target

@then('target obsahuje text "Dropped!"')
def check_dropped(context):
    assert "Dropped!" in context.target.text
    context.driver.quit()
