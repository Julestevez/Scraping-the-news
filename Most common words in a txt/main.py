import collections
import pandas as pd
import matplotlib.pyplot as plt

# Read input file. It may be different in your text file
file = open('julio.txt', encoding="utf8")
a= file.read()# Stopwords
stopwords = set(line.strip() for line in open('stopwords.txt'))
stopwords = stopwords.union(set(['nuestra','están','años','puede','hace','he','todos','(aplausos)', #add stopwords to the dictionary
'tanto','esa','vamos','decir','todo','ya','todo','hoy','ni','hacer','aquí','va','sin','ese','está',
'tenemos','desde','sí','ser','hemos','parlamentario','son','grupo','yo','gobierno','cuando','me',
'nuestro','eso','señorías','tiene','sánchez','hay','usted','ustedes','también','si','pero','porque',
'más','les','le','han','esta','este','la','que','de','y','a','las','una','lo','su','ha','sus','el',
'en','los','por','señor','se','un','es','del','no','al','presidenta','con','o','como','señora',
'para','nos','creo','sobre','dicho','estamos','diputados','investidura','partido','muy','muchas','hecho',
'tienen','sino','qué','gracias','vez','solo','contra','haya','muchos','popular','podemos','nosotros','parte',
'menos','mismo','quiere','durante','política','cámara','así','ahora','quieren','presidencia','candidato',
'tener','hablar','quiero','todas','unidas','cada','dos','ejemplo','mucho','estos','entre','fue','española','año','%','uno','mi','bien','mejor',
'sociedad','solamente','poder','oposición','esos','presidente','ir','alguna','mayoría','derechos','señores','nacional',
'socialista','sistema','esto','incluso','últimos','(aplausos','(rumores)','fuerzas','millones',
'nada','meses','después','sido','lugar','políticas','día','algo','antes','decía','van','cosas','sea','tan']))# Instantiate a dictionary, and for every word in the file, 
# Add to the dictionary if it doesn't exist. If it does, increase the count.
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

df = pd.DataFrame(lst, columns = ['Término', 'Nº de veces'])
df.plot.bar(x='Término',y='Nº de veces')
df.style.set_table_attributes('style="font-size: 25px"')
plt.xticks(fontsize=14)



plt.show()
