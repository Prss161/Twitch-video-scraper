import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    
    file = open("./url.txt", "r")
    list_of_channels = list(map(lambda x: x.strip("\n"), file.readlines()))
    file.close()
    driver = webdriver.Chrome()
    
    for channel in list_of_channels:
        driver.get(channel)
        time.sleep(3)
        links = driver.find_elements(By.XPATH, "//a[@data-a-target='preview-card-image-link']")
        tytul = driver.find_elements(By.XPATH, '//h3[@title]')
        kanal = driver.find_elements(By.XPATH, '//a[@data-a-target="preview-card-channel-link"]')
        linki = []
        tytuly = []
        kanaly = []
        
        for link in links:
            string = link.get_attribute('href').strip()
            linki.append(string)

        for title in tytul:
            string = title.get_attribute('title').strip()
            tytuly.append(string)
            
        for a in kanal:
            string = a.get_attribute('href').strip()
            kanaly.append(string)
            
        file_name = 'clips.csv'
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write = csv.writer(f)
            f.write.writerow(['Linki', 'Tytuly', 'Kanały'])
            for i in range(len(linki)):
                f.write.writerow([i + 1, tytuly[i], linki[i], kanaly[i]])


main()
