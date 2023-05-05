from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Browser:
    def __init__(self) -> None:
        self.browser = webdriver.Chrome()

    def go_to_link(self):
        self.browser.get(url="https://groall.noda.pro/test_qa")
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, "sendTokenForm")))
        body = self.browser.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ESCAPE)

    @property
    def current_balance(self):
        self.go_to_link()
        return int(self.browser.find_element(By.XPATH, "//div[@class='baseContent']/child::p").text.split()[1])

    def bring_out_part(self, *, value):
        self.go_to_link()
        input = self.browser.find_element(By.XPATH, "//input[@name='value']")
        input.send_keys(f"{value * 100}")
        button = self.browser.find_element(By.XPATH, "//input[@type='button']")
        button.submit()
        body = self.browser.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.END)
        return self.current_balance
    
    def bring_out_all(self):
        self.go_to_link()
        self.browser.find_element(By.XPATH, "//input[@name='value']").click()
        button = self.browser.find_element(By.XPATH, "//input[@type='button']")
        button.submit()
        body = self.browser.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ESCAPE)
        return self.current_balance








