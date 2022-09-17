import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    driver = webdriver.Chrome()
    driver.get('https://www.twitch.tv/directory/game/Just%20Chatting/clips?range=7d')
    time.sleep(3)
    links = driver.find_elements(By.XPATH, "//a[@data-a-target='preview-card-image-link']")
    tytul = driver.find_elements(By.XPATH, '//h3[@title]')
    linki = []
    tytuly = []
    for link in links:
        string = link.get_attribute('href').strip()
        linki.append(string)

    for title in tytul:
        string = title.get_attribute('title')
        tytuly.append(string)
    file_name = 'clips.csv'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write = csv.writer(f)
        f.write.writerow(['Linki', 'tytuly'])
        for i in range(len(linki)):
            f.write.writerow([i + 1, tytuly[i], linki[i]])


main()
