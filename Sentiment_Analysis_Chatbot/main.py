# Cleaning Text Steps
# 1) Create a text file and take text from it 
# 2) Convert the letter into lowercase ('Apple' is not equal to 'apple')
# 3) Remove punctuations like .,!? etc. (Hi! This is tanecious_theorist.)

import string
text = open('/workspaces/DataScienceProjects/Sentiment_Analysis_Chatbot/read.txt',encoding='utf-8').read()
lower_case = text.lower()

# str1 : Specifies the list of charecters that need to be replaced.
# str2 : Specifies the list of charecters with which the charecters need to be replaced.
# str3 : Specifies the list of charecters that need to be deleted.
# str1 : 'abc'
# str2 : 'gef'
# Returns : Returns the translation table which specifies the conversions that can be used by 

cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
tokenized_words = cleaned_text.split()
print(tokenized_words)

stop_words




