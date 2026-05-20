from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "file:///home/runner/work/my-ci-project/my-ci-project/index.html"

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    return driver


def test_page_title():
    driver = setup_driver()

    driver.get(URL)

    assert "Форма регистрации" in driver.title

    driver.quit()


def test_form_success():
    driver = setup_driver()

    driver.get(URL)

    driver.find_element(By.ID, "name").send_keys("Иван")
    driver.find_element(By.ID, "email").send_keys("ivan@test.com")

    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)

    message = driver.find_element(By.ID, "message").text

    assert message == "Форма успешно отправлена"

    driver.quit()


def test_short_name():
    driver = setup_driver()

    driver.get(URL)

    driver.find_element(By.ID, "name").send_keys("A")
    driver.find_element(By.ID, "email").send_keys("a@test.com")

    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)

    message = driver.find_element(By.ID, "message").text

    assert message == "Имя слишком короткое"

    driver.quit()


def test_input_exists():
    driver = setup_driver()

    driver.get(URL)

    name_input = driver.find_element(By.ID, "name")

    assert name_input is not None

    driver.quit()