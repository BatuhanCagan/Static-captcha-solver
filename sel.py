from PIL import Image
import pytesseract
from selenium import webdriver
import time
import selenium

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\Tesseract-OCR\\tesseract.exe'
driver = webdriver.Firefox

metin = open('ekle.txt','r')
numara = open('numaralar.txt','r')

browser = webdriver.Firefox()
browser.get("http://127.0.0.1:5500/home.html")
time.sleep(3)
name = browser.find_element_by_name("name")
tel = browser.find_element_by_name("tel")
adres = browser.find_element_by_name("adres")
capt = browser.find_element_by_id("ca")
tre = browser.find_element_by_id("ert")
a = pytesseract.image_to_string("Adsiz.png", lang="tur")
capta = browser.find_element_by_name("capt")
removed = a.replace("","")
for line in metin:
    isimler=line.strip()
    name.send_keys(isimler)
    tel.send_keys("12345678910")
    adres.send_keys("Elazığ")
    capta.send_keys(removed)
    time.sleep(2)
    tre.click()


time.sleep(10)
browser.close()