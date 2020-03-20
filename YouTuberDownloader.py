from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pytube import Playlist
from pytube import YouTube


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

YouTuber = input("Enter YouTuber: ")
YouTuber = YouTuber.replace(" ","")
YouTuber = YouTuber.lower()
url = "https://YouTube.com/user/" + YouTuber + "/playlists"
driver.get(url)
html = driver.find_element_by_xpath(".//html")
text = html.text.split("\n")
playlists = []
n = len(text)
for i in range(n):
    if(text[i] == "VIEW FULL PLAYLIST"):
        playlists.append(text[i - 1])

print(" ***** SAMPLE PLAYLISTS *****")
for i in range(len(playlists)):
    print(playlists[i])
print("*************************")

links = driver.find_elements_by_link_text('VIEW FULL PLAYLIST')
toDownload = input("Input Playlist To Download: ")

for i in range(len(playlists)):
    if(playlists[i] == toDownload):
        links[i].click()

print("Downloading Playlist...")
playlist = Playlist(driver.current_url)

for i in range(len(playlist)):
    print(playlist[i])
    YouTube(playlist[i]).streams[0].download()

print("Done!")





driver.quit()

