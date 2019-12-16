from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package 
import requests
import re
import matplotlib.pyplot as plt
from nltk import tokenize
import numpy as np


frase=np.zeros(100)
#URL = 'https://elpais.com/tecnologia/2019/10/22/actualidad/1571763922_161368.amp.html'
URL='https://www.elconfidencial.com/empresas/2019-03-03/paula-carsi-ingeniera-ford-almussafes-mujeres_1858546/'
content = requests.get(URL)
#********** FORMA 1 ************
#soup = BeautifulSoup(content.text)#, 'html.parser')
#p=soup.findAll("p")
#print(p)
#******** FIN DE FORMA 1  ************


#************ FORMA 2 ***********
soup = BeautifulSoup(content.text, 'html.parser')
#p = soup.findAll("div", attrs={'itemprop':'articleBody'})
p=soup.findAll("p")
soup_string = str(p)
soup_string= re.sub('<[^>]+>', '', soup_string)
soup_string= re.sub('En Titania Compañía Editorial, S.L. creemos en la libertad de expresión y en la aportación de los lectores para crear y enriquecer el debate sobre los temas de actualidad que tratamos., Para promover y mantener ese ambiente de intercambio útil y libre de opiniones, hemos establecido un conjunto de normas sencillas que tienen como objetivo garantizar el desarrollo adecuado de esos debates. Su no cumplimiento supondrá la eliminación del comentario, o incluso la expulsión de La Comunidad en caso de actitudes reiteradas que desoigan avisos previos., Por lo demás, pedimos a nuestros usuarios que se comporten con los demás con el mismo respeto con el que quieren ser tratados igualmente. De esa manera La Comunidad seguirá siendo un espacio interesante en el que debatir y aprender. Agradecemos de antemano a todos nuestros lectores su esfuerzo y su aportación.','',soup_string)
sentences=tokenize.sent_tokenize(soup_string) #this command divides text into sentences
#soup_string=soup_string.replace('<p>', '')
#soup_string=soup_string.replace('</p>','')
#soup_string=soup_string.replace([soup_string.find("<"):soup_string.find(">")],'')

for i in range (0,len(sentences)):
    frase[i]=len(re.findall('\w+', sentences[i]))
    

#print(sentences[2]) #asi se imprime una frase
print(len(sentences))


# using regex (findall()) 
# to count words in string 
res = len(re.findall(r'\w+', soup_string))
# printing result 
print ("The number of words in string are : " +  str(res)) 

#map(len, s.split())       # assuming Python 2.x
#list(map(len, soup_string.split())) # assuming Python 3.x
h=list(map(len, soup_string.split()))
print(h)
#[len(x) for x in soup_string.split()]

# matplotlib histogram
fig= plt.figure()
plt.subplot(211)
plt.hist(h, bins=15, edgecolor='black', linewidth=1.2)
#plt.xlim(0, 20)
plt.xticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
plt.title("Frecuencia de palabras según su nº de caractreres. Nº total de palabras en el texto:" + str(res))


plt.subplot(212)
fig.tight_layout()
plt.hist(frase[0:58],bins=100, edgecolor='black', linewidth=1.2)
plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
plt.title('Frecuencia de frases según el número de palabras. 58 frases en el texto')
plt.show()

#*************** FIN DE FORMA 2 ****************

