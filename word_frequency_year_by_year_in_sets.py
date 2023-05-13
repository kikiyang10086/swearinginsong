specified_words = ["bitch","bitches"]                 # change the word here!!!

# open the file
for i in range(1991,2022):
    word_list = []
    with open("D:/pyfiles/final/general_lyrics/" + str(i) + "_lyrics.txt", 'r', encoding='utf-8') as f:
        for line in f:
            word_list.append(line.replace('\n',''))
    
    total_word_count = 0
    for m in range(len(specified_words)):
        # specify a word
        word_count = 0
        for p in word_list:
            if specified_words[m] == p:
                word_count += 1
        total_word_count += word_count
    
    # show the word
    print(str(total_word_count))