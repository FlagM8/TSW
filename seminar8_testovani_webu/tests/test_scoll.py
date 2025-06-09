import time
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

scenarios('../features/scroll.feature')

@given("otevřu stránku s nekonečným scrollováním")
def open_scroll_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://infinite-scroll.com/demo/full-page/")
    context.initial_articles = len(context.driver.find_elements(By.TAG_NAME, "article"))

@when("scroluji na konec stránky a počkám")
def scroll_down(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)

@then("se načtou nové články")
def check_articles_loaded(context):
    new_count = len(context.driver.find_elements(By.TAG_NAME, "article"))
    assert new_count > context.initial_articles
    print(f"Počet článků se zvýšil z {context.initial_articles} na {new_count}")
    context.driver.quit()
