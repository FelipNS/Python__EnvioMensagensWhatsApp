from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class WANavagation:

    def __init__(self, name: str) -> None:
        self.nav = webdriver.Edge()
        self.name = name

    def open_chat_whatsapp(self):
        self.nav.get('https://web.whatsapp.com')
        while len(self.nav.find_elements_by_id('side')) < 1:
            sleep(1)
        sleep(5)
        self.nav.find_element_by_xpath(f'//*[@title="{self.name}"]').click()

    def send_mensage(self, txt: str):
        WANavagation.open_chat_whatsapp(self)
        self.nav.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').click()
        self.nav.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(f'{txt}')
        self.nav.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
        sleep(20)
    
    def send_photos(self, path_midia: str):
        WANavagation.open_chat_whatsapp(self)
        sleep(5)
        self.nav.find_element_by_css_selector('span[data-icon="clip"]').click()
        sleep(3)
        self.nav.find_element_by_css_selector('input[type="file"]').send_keys(f'{path_midia}')
        sleep(3)
        self.nav.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]/div/div/span').click()
        sleep(10)


