from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
from time import sleep

class WANavagation:

    def __init__(self) -> None:
        self.nav = webdriver.Edge(EdgeChromiumDriverManager().install())

    def open_chat_whatsapp(self, name_chat: str):
        self.nav.get('https://web.whatsapp.com')
        while len(self.nav.find_elements_by_id('side')) < 1:
            sleep(1)
        sleep(5)
        self.nav.find_element_by_xpath(f'//*[@title="{name_chat}"]').click()
        WANavagation.send_photos(self)

    def send_mensage(self, txt: str):
        self.nav.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').click()
        self.nav.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(f'{txt}')
        self.nav.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
        sleep(20)
    
    def send_photos(self):
        sleep(5)
        self.nav.find_element_by_css_selector('span[data-icon="clip"]').click()
        sleep(3)
        self.nav.find_elements_by_css_selector('input[type="file"]').send_keys(r'Imagens\Eu.jpg')
        sleep(3)
        self.nav.find_element_by_xpath('//div[contains(@class, "_3Git-")]').click()

navegador = WANavagation()
navegador.open_chat_whatsapp('1°ANO PONTE NOVA')
