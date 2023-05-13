import urllib.request
import re
import csv

for year in range(1991,2022):       #change the year!!!
    #crawl all the page content
    pagename = 'https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_' + str(year)
    response =  urllib.request.urlopen(pagename)
    html = response.read()
    page_content = str(html.decode('utf-8'))

    #select chart part
    str_start = '<tbody><tr>'
    str_end = '</td></tr></tbody></table>'
    raw_table = page_content[page_content.index(str_start):page_content.index(str_end)]
    raw_table = raw_table + '\n</td></tr></tbody></table>'
    
    #clean the data
    raw_table = re.sub('\<.*?\>', '', raw_table)        #remove all the <> stuff
    raw_table = raw_table.replace('"','')       #remove all the ""

    #extract info into a dict
    raw_table_list = list(raw_table.split('\n'))        #split data into lines

    songs_dict = {}
    for i in range(101):
        for p in range(len(raw_table_list)):
            if raw_table_list[p] == str(i):
                song_name = raw_table_list[p+1]
                artist_name = raw_table_list[p+2]
                songs_dict[song_name] = artist_name

    #create new csv file
    filename = 'D:/pyfiles/final/general_lyrics/' + str(year) + '.csv'
    f = open(filename, mode='a',encoding='utf-8',newline='')
    
    #write dict in csv file
    csv_writer = csv.DictWriter(f,fieldnames=['song_name','artist_name','lyrics'])
    csv_writer.writeheader()

    writer = csv.writer(f)
    for key, value in songs_dict.items():
       writer.writerow([key, value])