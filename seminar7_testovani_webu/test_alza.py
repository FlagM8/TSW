import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_search_product(driver):    
    driver.get("https://www.alza.cz/")
    wait = WebDriverWait(driver, 2)
    search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-testid="searchInput"]')))
    search_box.send_keys("iPhone 15")
    search_box.send_keys(Keys.RETURN)
    results = driver.find_elements(By.CLASS_NAME, "browsinglink")
    assert any("iPhone 15" in result.text for result in results), "Produkt 'iPhone 15' nebyl nalezen ve výsledcích vyhledávání."

def test_product_price(driver):
    driver.get("https://www.alza.cz/")
    wait = WebDriverWait(driver, 5)
    search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-testid="searchInput"]')))
    search_box.send_keys("Samsung Galaxy S25")
    search_box.send_keys(Keys.RETURN)
    # Wait for prices to appear
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.price-box__primary-price__value.js-price-box__primary-price__value")))
    price_elements = driver.find_elements(By.CSS_SELECTOR, "span.price-box__primary-price__value.js-price-box__primary-price__value")
    prices = []
    for el in price_elements:
        price_text = el.text.replace("\xa0", "").replace(",-", "").replace("Kč", "").replace(" ", "").replace(",", ".")
        try:
            price = float(price_text)
            prices.append(price)
        except ValueError:
            continue
    assert all(p >= 15000 for p in prices), f"Za tu cenu je to krádež! Nalezené ceny: {prices}"

def test_add_to_cart(driver):
    driver.get("https://www.alza.cz/")
    wait = WebDriverWait(driver, 5)
    search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-testid="searchInput"]')))
    search_box.send_keys("PlayStation 5")
    search_box.send_keys(Keys.RETURN)
    box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.box[data-id="8078676"]')))
    price_element = box.find_element(By.CSS_SELECTOR, "span.price-box__primary-price__value.js-price-box__primary-price__value")
    price_text = price_element.text.replace("\xa0", "").replace(",-", "").replace("Kč", "").replace(" ", "").replace(",", ".")
    listing_price = float(price_text)
    add_to_cart_btn = box.find_element(By.CSS_SELECTOR, "a.btnk1[href^='javascript:boxOrder']")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_btn)
    driver.execute_script("arguments[0].click();", add_to_cart_btn)
    WebDriverWait(driver, 5).until(lambda d: d.execute_script("return window.Alza"))
    import time
    time.sleep(1)
    basket_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="headerBasketIcon"]')))
    basket_icon.click()
    # driver.get("https://www.alza.cz/Order1.htm")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.mainItem")))
    product_link = driver.find_element(By.CSS_SELECTOR, "a.mainItem")
    assert "playstation-5" in product_link.get_attribute("href").lower()
    cart_price_el = driver.find_element(By.CSS_SELECTOR, "span.last.price")
    cart_price_text = cart_price_el.text.replace("\xa0", "").replace("Kč", "").replace(" ", "").replace(",", ".")
    cart_price = float(cart_price_text)
    assert abs(cart_price - listing_price) < 1, f"Cena v košíku ({cart_price}) neodpovídá ceně v listingu ({listing_price})"


def test_frontpage_featured_products(driver):
    driver.get("https://www.alza.cz/")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="swiperContainer"]')))
    product_names = [el.text.lower() for el in driver.find_elements(By.CSS_SELECTOR, '[data-testid="itemName"] .carousel-0-alz-35')]
    assert any("iphone 16 pro" in name for name in product_names), "iPhone 16 Pro není na hlavní stránce"
    assert any("mac mini m4" in name for name in product_names), "Mac mini M4 není na hlavní stránce"
    assert any("imac 24" in name for name in product_names), "iMac 24 není na hlavní stránce"

def test_login_redirect(driver):
    driver.get("https://www.alza.cz/")
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[data-testid="headerContextMenuToggleLogin"]')))
    login_button.click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.login-body")))
    login_title = driver.find_element(By.CSS_SELECTOR, "div.login-title h1")
    assert "přihlášení" in login_title.text.lower(), "Přesměrování na přihlašovací stránku selhalo."
