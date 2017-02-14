import time
import re
import string
import os

# We use the file saved from last step as example
file = open("/home/vivek/Desktop/twitter_nlp-master/Cleaned_NER/travel_new8.txt", "r")
file1 = open("/home/vivek/Desktop/twitter_nlp-master/Cleaned_NER/travel_new8_new.txt", "w")
#new_path='/home/vivek/Desktop/twitter_nlp-master/Cleaned_NER'
#for root, dirs, files in os.walk('/home/vivek/Desktop/twitter_nlp-master/Ner'):
    #for file in files:

for line in file:
    if 'out offer' in line:
        continue
    file1.write(line)
file1.close()
