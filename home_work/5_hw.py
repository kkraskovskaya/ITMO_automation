from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def check_saucedemo_elements():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


        driver.get("https://www.saucedemo.com/")
        print("Страница открыта!")

        driver.find_element(By.ID, "user-name")
        driver.find_element(By.ID, "password")
        driver.find_element(By.ID, "login-button")


        print("Элементы найдены")

        driver.quit()

    except Exception as e:
        print(f"Ошибка: {e}")


check_saucedemo_elements()