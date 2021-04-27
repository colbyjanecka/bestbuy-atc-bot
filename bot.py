from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from window_instance import WindowInstance
import time
import info
import threading


SKU_list = info.SKU_list
exitFlag = 0
SKU_count = len(SKU_list)
instances = [WindowInstance] * len(SKU_list)


class myThread(threading.Thread):
   def __init__(self, threadID, sku, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.sku = sku
        self.counter = counter
   def run(self):
        print("Starting " + self.sku)
        setup_window(self.threadID, self.sku, 5, self.counter)
        attempt(self.threadID)
        print("Exiting " + self.sku) 

def setup_window(idx, sku, counter, delay):
    instances[idx] = WindowInstance(sku)
    instances[idx].login()
    time.sleep(5)

def attempt(idx):
    while(instances[idx].addedToCart == False):
        instances[idx].attempt_to_cart()

threads = [myThread] * SKU_count
for idx in range(SKU_count):
    threads[idx] = myThread(idx, str(SKU_list[idx]), 1)
    threads[idx].start()
    time.sleep(5)
    
print("Exiting Main Thread")