# Twitch-video-scraper

## Introduction
This script allows scraping top 20 clips in selected category on Twitch website. Storing clips metadata - origin url, title, channel name in csv format.

## Getting Started
Project tested using Python 3.10.11 64-bit, requirements are available in requirements.txt.

## How it works?
When we start the `main.py`, the program ask us for url link for twitch website that contains clips (www.twitch.tv/directory/category/just-chatting/clips?range=all) you can use any category for downloading the clips. By using `Selenium WebDriver` we can scrap data from any website. The data that we are intested in is url, title and channel of a clip by using XPATH. Finnaly selected data is saved in csv file.

## How to run code
To run the code use command:
```bash
$ python main.py
 ```
