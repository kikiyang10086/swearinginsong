gender = "male"                 # change the gender shere!!!
specified_word = "bitch"                 # change the word here!!!

word_list = []
with open("D:/pyfiles/final/" + gender + "_singer/total_" + gender + "_words.txt", 'r', encoding='utf-8') as f:
    for line in f:
        word_list.append(line.replace('\n',''))

# specify a word
word_count = 0
for i in word_list:
    if specified_word == i:
        word_count += 1

print(specified_word + ":")
print(word_count)