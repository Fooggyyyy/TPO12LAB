from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "http://localhost:8000/index.html"

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)


def test_page_title():
    driver = setup_driver()
    driver.get(URL)

    assert "Форма регистрации" in driver.page_source

    driver.quit()


def test_form_success():
    driver = setup_driver()
    driver.get(URL)

    driver.find_element(By.ID, "name").send_keys("Иван")
    driver.find_element(By.ID, "email").send_keys("ivan@test.com")
    driver.find_element(By.TAG_NAME, "button").click()

    message = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "message"))
    ).text

    assert message == "Форма успешно отправлена"

    driver.quit()


def test_short_name():
    driver = setup_driver()
    driver.get(URL)

    driver.find_element(By.ID, "name").send_keys("A")
    driver.find_element(By.ID, "email").send_keys("a@test.com")
    driver.find_element(By.TAG_NAME, "button").click()

    message = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "message"))
    ).text

    assert message == "Имя слишком короткое"

    driver.quit()


def test_input_exists():
    driver = setup_driver()
    driver.get(URL)

    element = driver.find_element(By.ID, "name")
    assert element is not None

    driver.quit()