specified_word = "bitch"                 # change the word here!!!

# open the file
for i in range(1991,2022):
    word_list = []
    with open("D:/pyfiles/final/general_lyrics/" + str(i) + "_lyrics.txt", 'r', encoding='utf-8') as f:
        for line in f:
            word_list.append(line.replace('\n',''))

    # specify a word
    word_count = 0
    for p in word_list:
        if specified_word == p:
            word_count += 1

    # show the word
    print(str(word_count))