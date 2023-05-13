from lyricsgenius import Genius
import re
import time

genius = Genius("iOGAm3q8_5_X8p7ed1oi-eIQRS7K8deCS8KNXCvAI7vIzPF4SOIT0rd1mwmBgXK1", excluded_terms=["(Remix)", "(Live)"])

# export singers' name
male_singer_list = []
f = open("D:/pyfiles/final/female_singer/female_singer.txt", "r", encoding ="utf-8")
lines = f.readlines()
for line in lines:
    male_singer_list.append(line.replace('\n',''))
print(male_singer_list)

# let API get singers' most popular songs
for i in range(0,20):

    # first we should avoid timeout
    artistname = str(male_singer_list[i])
    action = 0
    while action == 0:
        try:
            artist = genius.search_artist(artistname, max_songs = 20, sort = "popularity")
            action = 1
        except:
            print("Sorry, time out!")
            print("Sleeping and trying again...")
            time.sleep(5)
            action = 0

    # get songs' lyrics
    songs = artist.songs
    wordlist = []
    for song in songs:
        lyrics = str(song.lyrics).replace("\n", " ").replace(",", "").replace("?", "").replace(".", "").replace("!", "").lower()
        lyrics = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", lyrics)
        lyrics = lyrics.split(" ")                  # split lyrics into words
        wordlist.append(lyrics)

    # save lyrics words into files
    with open("D:/pyfiles/final/female_singer/" + artistname + ".txt", "w", encoding = "utf-8") as f:
        for i in range(20):
            for o in wordlist[i]:
                f.write(o + '\n')

    print(artistname + ' Done.')