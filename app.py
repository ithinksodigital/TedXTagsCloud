from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import urllib
import urllib.request
import requests
import numpy as np
import matplotlib.pyplot as plt
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize


##################################################################
# collect data from ted2str
##################################################################


# for i in range(1, 32618, 1):
#     # for i in range(1, 2, 1):
#     try:
#         link = "https://ted2srt.org/api/talks/" + str(i) + "/transcripts/download/txt?lang=en"
#         save_as = "txt/" + str(i) + ".txt"
#         urllib.request.urlretrieve(link, save_as)
#     except urllib.error.HTTPError as err:
#         if err.code == 404:
#             print("Opps...", i, "return 404 error")
#         elif err.code == 500:
#             print(i, "505")
#         else:
#             raise


##################################################################
#Concatenation all files into one
##################################################################

# files = []
# for i in range (1, 2995, 1):
#     a = "txt/Plik"+str(i)+".txt"
#     files.append(a)
#
#
# with open('file', 'w') as outfile:
#     for fname in files:
#         with open(fname) as infile:
#             for line in infile:
#                 outfile.write(line)


##################################################################
#create list with all words then string & nlp tokenize
##################################################################

words_ = []
with open('file','r') as f:
    for line in f:
        for word in line.split():
           words_.append(word)

# words = " ".join(words_).replace(',','').replace('.','').replace('!','').replace('?', '').replace('-','').replace('\'','').replace(':','').replace(';', '').replace('Laughter','')


words_tokenize = word_tokenize(words_)

words_to_used = " ".join(words_tokenize).replace(',','').replace('.','').replace('!','').replace('?', '').replace('-','').replace('\'','').replace(':','').replace(';', '').replace('Laughter','')


##################################################################
# This function takes in your text
# and your mask and generates a wordcloud.
##################################################################


def generate_words_cloud(words_to_used):
    word_cloud = WordCloud(width=600, height=600, background_color='white', stopwords=STOPWORDS).generate(
        words_to_used)
    plt.figure(figsize=(10, 8), facecolor='white', edgecolor='black')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()


generate_words_cloud(words_to_used)
