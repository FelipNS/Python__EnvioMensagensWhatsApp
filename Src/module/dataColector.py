from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def start_browser():
    global nav 
    nav = webdriver.Edge()

class WANavagation:

    
    def __init__(self, name: str) -> None:
        self.name = name

    def open_chat_whatsapp(self):
        nav.get('https://web.whatsapp.com')
        while len(nav.find_elements_by_id('side')) < 1:
            sleep(1)
        sleep(5)
        nav.find_element_by_xpath(f'//*[@title="{self.name}"]').click()

    def send_mensage(self, txt: str):
        nav.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').click()
        nav.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(f'{txt}')
        nav.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
        sleep(5)
    
    def send_photos(self, path_midia):
        nav.find_element_by_css_selector('span[data-icon="clip"]').click()
        nav.find_element_by_css_selector('input[type="file"]').send_keys(path_midia)
        sleep(3)
        nav.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]/div/div/span').click()
        sleep(5)

def quit_browser():
    nav.quit()
