from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import info


CD_PATH = "/Users/hiplandic/Desktop/bots/bestbuy-atc-bot/chromedriver"

class WindowInstance:
    def __init__(self, sku):
        self.driver = webdriver.Chrome(CD_PATH)
        self.sku = sku
        self.username = info.email
        self.password = info.password
        self.addedToCart = False
        print(str(self.sku) + " : Created new Window instance for user " + self.username)
        self.cart_link = "https://api.bestbuy.com/click/-/" + str(sku) + "/cart"
        
    def login(self):
        print(str(self.sku) + " : Attemping to log in to : " + self.username)
        # go to log in page
        self.driver.get("https://www.bestbuy.com/identity/global/signin")

        time.sleep(1)

        # enter email and pass
        emailField = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.ID, "fld-e"))
        )
        emailField.send_keys(info.email)
        print(str(self.sku) + " : Filled in email")

        pwField = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.ID, "fld-p1"))
        )
        pwField.send_keys(info.password)
        print(str(self.sku) + " : Filled in pass")

        # click sign in 
        signInBtn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[4]/button"))
        )
        signInBtn.click()
        print(str(self.sku) + " : Signing in")


    def attempt_to_cart(self):
        self.driver.get(self.cart_link)
        print(str(self.sku) + " : attempting to cart: " + self.sku)
        """
        try:
            print("HERE1!")
            checkoutBtn = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button"))
            )
            print("HERE2!")
            checkoutBtn.click()
            self.addedToCart = True
            print("ADDED TO CART!")
        except:
            print(str(self.sku) + " : OOS")
            self.driver.get(self.cart_link)
            self.addedToCart = False
        """
        txt = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "page-heading__title"))
        )
        if "Your cart is empty" in txt.text:
            print(str(self.sku) + " : CART IS EMPTY")
        else:
            print(str(self.sku) + " : ADDED TO CART")
            self.addedToCart = True
    def goToSKU(self, sku):
        link = "https://api.bestbuy.com/click/-/" + str(sku)
        self.driver.get(link)
        print(str(self.sku) + " : pulled up site for this sku")
