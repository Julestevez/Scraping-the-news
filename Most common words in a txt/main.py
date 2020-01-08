import collections
import pandas as pd
import matplotlib.pyplot as plt

# Read input file. It may be different in your text file
file = open('Example.txt', encoding="utf8")  ###CHANGE TO YOUR FILE
a= file.read()# Stopwords
stopwords = set(line.strip() for line in open('stopwords.txt')) ## ADD YOUR OWN STOPWORDS
stopwords = stopwords.union(set([''word4','word5','word6']))# Instantiate a dictionary, and for every word in the file, 
# Add to the dictionary if it doesn't exist. If it does, increase the count. ##ADD AS MANY WORDS AS NEEDED
wordcount = {}# To eliminate duplicates, remember to split by punctuation, and use case demiliters.
for word in a.lower().split():
    #replace the punctuation   
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1# Print most common word

n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)# Close the file
file.close()# Create a data frame of the most common words 
# Draw a bar chart
lst = word_counter.most_common(n_print)

df = pd.DataFrame(lst, columns = ['Word', 'Number of times'])
df.plot.bar(x='Word',y='Number of times')
df.style.set_table_attributes('style="font-size: 25px"')
plt.xticks(fontsize=14)



plt.show()
