import csv
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

class TwitchVideoScraper:
    def __init__(self, channel_url, max_links=20):
        """
        Args:
            channel_url (str): url of a website with clips that we want to scrap.
            max_links (int): amount of clips that we want. Defaults to 20.
            
        """
        
        self.channel_url = channel_url
        self.max_links = max_links
        self.link_list = []
        self.title_list = []
        self.channel_list = []

    def scrape_videos(self):
        driver = webdriver.Chrome()

        try:
            while len(self.link_list) < self.max_links:
                page_url = f"{self.channel_url}"
                driver.get(page_url)
                time.sleep(random.uniform(2, 5))

                links = driver.find_elements(By.XPATH, "//a[@data-a-target='preview-card-image-link']")
                titles = driver.find_elements(By.XPATH, '//h3[@title]')
                channels = driver.find_elements(By.XPATH, '//a[@data-a-target="preview-card-channel-link"]')

                if not links:
                    break

                for link, title, channel in zip(links, titles, channels):
                    self.link_list.append(link.get_attribute('href').strip())
                    self.title_list.append(title.get_attribute('title').strip())
                    self.channel_list.append(channel.get_attribute('href').strip())

                if len(self.link_list) >= self.max_links:
                    break

        finally:
            driver.quit()

    def write_to_csv(self):
        file_name = 'Links_for_clips.csv'
        with open(file_name, 'w', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['Link', 'Title', 'Channel'])
            for link, title, channel in zip(self.link_list, self.title_list, self.channel_list):
                csv_writer.writerow([link, title, channel])

    def run(self):
        self.scrape_videos()
        self.write_to_csv()
        print(f"Scraped {len(self.link_list)} clips and saved to 'Links_for_clips'.")

def main():
    channel_url = input("Enter the URL of the Twitch channel you want to scrape: ")

    scraper = TwitchVideoScraper(channel_url)
    scraper.run()

if __name__ == "__main__":
    main()