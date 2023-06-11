from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from constants import globalTrendyolConstants
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class TestTrendyol:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(globalTrendyolConstants.URL)
        
        

    def teardown_method(self):
        self.driver.quit()

    def waitMethod(self,locater):
        WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((locater)))

    def btnOfWoman(self):
        #butonun üstüne gelme işlemi
        btnOn= self.driver.find_element(By.XPATH,"//div[@id='navigation-wrapper']/nav/ul/li[1]/a")
        actions = ActionChains(self.driver)
        actions.move_to_element(btnOn).perform()
        self.waitMethod((By.XPATH,"//div[@id='sub-nav-1']/div/div/div/div/ul/li/a"))

    def btnOfMan(self):
        btnOn = self.driver.find_element(By.XPATH,"//*[@id='navigation-wrapper']/nav/ul/li[2]/a")     
        actions = ActionChains(self.driver)
        actions.move_to_element(btnOn).perform()
        self.waitMethod((By.XPATH,"//*[@id='navigation-wrapper']/nav/ul/li[2]/a"))
        

    def test_buttonsOfWomans(self):
        btnCross = self.driver.find_element(By.ID,"Combined-Shape")
        btnCross.click()
        for i in range(13):
            i += 1
            self.btnOfWoman()
            btnLink = self.driver.find_element(By.XPATH,f"//*[@id='sub-nav-1']/div/div/div[1]/div/ul/li[{i}]/a")
            btnLink.click()
    def test_buttonsOfMan(self):
        btnCross = self.driver.find_element(By.ID,"Combined-Shape")
        btnCross.click()
        for j in range(1,14):
            self.btnOfMan()
            self.waitMethod((By.XPATH,f"//*[@id='sub-nav-2']/div/div/div[1]/div/ul/li[{j}]"))
            btnLink1 = self.driver.find_element(By.XPATH,f"//*[@id='sub-nav-2']/div/div/div[1]/div/ul/li[{j}]/a")
            btnLink1.click()
        btnSort = self.driver.find_element(By.XPATH,"//div[@id='search-app']/div/div/div[2]/div/div[2]/div/div/div")
        btnSort.click()
        btnMin = self.driver.find_element(By.XPATH,"//div[@id='search-app']/div/div/div[2]/div/div[2]/div/ul/li[2]")
        btnMin.click()

