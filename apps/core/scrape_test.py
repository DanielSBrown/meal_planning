from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Ingredient:
    def __init__(self, name, amount=None, unit=None):
        self.name = name
        self.amount = amount
        self.unit = unit

    def __str__(self):
        if self.amount is None and self.unit is None:
            return f"{self.name}"
        return f"{self.amount} {self.unit} {self.name}"


if __name__ == "__main__":
    url = "https://www.hellofresh.com/recipes/sesame-sweet-soy-fried-rice-63bd8357978582d39f0f108a"
    ua = UserAgent()
    userAgent = ua.random
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument(f"user-agent={userAgent}")
    options.add_argument("--no-sandbox")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")

    options.add_argument("--headless")
    options.add_experimental_option("useAutomationExtension", False)

    # options.headless = True

    browser = webdriver.Chrome(desired_capabilities=options.to_capabilities())
    browser.get(url)

    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div[data-test-id='recipeDetailFragment.ingredients'")
        )
    )

    soup = BeautifulSoup(browser.page_source, features="lxml")

    browser.quit()
    ing_div = soup.find_all(
        "div", {"data-test-id": "recipeDetailFragment.ingredients"}
    )[0]
    ingredients = ing_div.find_all("p")

    for idx in range(0, len(ingredients), 2):
        if ingredients[idx].contents:
            amount, unit = ingredients[idx].contents[0].split()
        else:
            amount, unit = None, None
        name = ingredients[idx + 1].contents[0]
        ingredient = Ingredient(name=name, amount=amount, unit=unit)
        print(ingredient)
