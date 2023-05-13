import string

word_list = []
with open("D:/pyfiles/final/female_singer/total_female_words.txt", 'r', encoding='utf-8') as f:
    for line in f:
        word_list.append(line.replace('\n',''))

# count the words
counts = {}
for word in word_list:
    counts[word] = counts.get(word, 0) + 1      #'get' returns the specified value in a dic, '0' means by default it's 0

# delete the words we don't want
excludes = {'is','a','in','on','','the','and','to','it','be','but','that','so','all','up','with','when','what','of','for','oh',"it's",'yeah','can',"'cause"}
for word in excludes:
	del counts[word]

# range the dic from top to bottom
counts = sorted(counts.items(), key = lambda x: x[1], reverse = True)      #sorted(iterable, key=None, reverse=False), False is by default which means ascending order

# show the top xxx results
for i in range(50):
    print(counts[i])