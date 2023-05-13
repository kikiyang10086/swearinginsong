import urllib.request
import re
import csv
import urllib.request
from urllib import request
import random
import time
import string
import json

year = '2021'                  # change the year!!!
half = 'second'                   # first/second!!!
with open('D:/pyfiles/final/general_lyrics/'+ year +'.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    result = list(reader)

number = 0
songs_not_found = []
all_lyrics = ''
lyrics_list = []

if half == 'first':
    p = range(1,51)
if half == 'second':
    p = range(52,100)
for i in p:                   # change the number!!! 1,51;52,101
    number += 1
    
    # sleep a random time (in milliseconds) to prevent banning by host
    sleep_time = random.randint(0,10000)
    time.sleep(sleep_time / 1000)
    print('---sleep time', sleep_time)

    # clean artist and song's name for url search
    artist = str(result[i][1]).lower()
    song = str(result[i][0]).lower()
    artist = artist.split('featuring')[0]   # for ft. songs, we only want the main artist
    artist = artist.split(' ft ')[0]
    artist = artist.split(' and ')[0]
    artist = artist.split('+')[0]
    artist = artist.split(',')[0]
    artist = artist.replace(' ','')
    for ar in string.punctuation:           # delete the punctuations
        artist = artist.replace(ar, '')
    song = song.replace(' ','')
    for ar in string.punctuation:           # delete the punctuations
        song = song.replace(ar, '')
    print(str(number) + ' ' + artist + ' ' + song)

    # url search
    song_page = 'https://www.azlyrics.com/lyrics/' + artist + '/' + song + '.html'
    headers = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"), ("Accept", "text/html")]

    opener = urllib.request.build_opener()
    opener.addheaders = headers

    try:
        page_content = str(opener.open(song_page).read())
    except:
        print(number, artist, song, "can't find!")
        songs_not_found.append({number:song})
        continue
    
    if "It's a place where all searches end!" not in page_content:
        # slice the str and extract the lyrics part
        str_start = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
        str_end = '<!-- MxM banner -->'
        raw_lyrics = page_content[page_content.index(str_start):page_content.index(str_end)]

        # clean the string with re
        raw_lyrics = re.sub('<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->', '', raw_lyrics)
        raw_lyrics = re.sub('<br>', '', raw_lyrics)
        raw_lyrics = re.sub('</div>', '', raw_lyrics)
        raw_lyrics = raw_lyrics.replace("(","").replace(")","").replace("<i>","").replace("</i>","").replace(",","").replace("?","").replace("!","")
        raw_lyrics = str(raw_lyrics).replace("\\n"," ").replace("\\r"," ").replace("\\","").lower()
        
        # store the lyrics into string
        all_lyrics += raw_lyrics

# write words into txt
lyrics_list = all_lyrics.split()

with open("D:/pyfiles/final/general_lyrics/" + year + "_" + half + "half_lyrics.txt", "w+", encoding = "utf-8") as f:
    for line in lyrics_list:
        f.write(line + '\n')

with open("D:/pyfiles/final/general_lyrics/omitted_songs.txt", "w+", encoding = "utf-8") as file:
     file.write(json.dumps(songs_not_found))

print(year + ' ' + half + ' ' + 'Done.')