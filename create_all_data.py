import numpy as np
from nltk.corpus import sentiwordnet as swn
from nltk.stem import *
import nltk
import xlrd as xlrd
import sys

###############################################################################################################################################

'''
<<< stripString >>>
Performs stripping (I.e. deletion of extra characters from start and end) on every word

PARAMETERS: List of Unstripped Words
RETURN:     List of Stripped Words
'''

def stripString(lst):

    for i in range(len(lst)):
        lst[i] = lst[i].strip(" !@#$%^&*()-+_={[}]/.,<>~:;'")

    return lst

###############################################################################################################################################

'''
<<< lowerCase >>>
Converts all words to lowerCase

PARAMETERS: List of Normal Words
RETURN:     List of Lowercase Words
'''

def lowerCase(lst):

    for i in range(len(lst)):
        lst[i] = lst[i].lower()

    return lst

###############################################################################################################################################

'''
Open the book, choose the first sheet (I.e. the one that contains the data)
'''
book = xlrd.open_workbook('Books_Dataset.xlsx')
sheet = book.sheet_by_index(0)


'''
Initialise the lists
'''
book_name_list = []     # Name of the book
helpful_list = []       # Helpfulness of the review
score_list = []         # Score given in the review
review_list = []        # Review


'''
Run through the whole sheet, and populate the above lists
NOTE:   "  range(2,..  " --> This is because the Sheet's first two rows are blank
'''
for i in range(2,sheet.nrows):
    book_name_list.append(str(sheet.cell(i,1).value))
    helpful_list.append(str(sheet.cell(i,2).value))
    score_list.append(int(sheet.cell(i,3).value))
    review_list.append(str(sheet.cell(i,5).value))


'''
Extract tokens from each review, pre-process them, and populate the above list
'''
review_tokens = []  # To store List of tokens for each review
i = 0               # Counter for below loop

for review in review_list:
    temp = list(nltk.word_tokenize(review))
    temp = stripString(temp)
    temp = lowerCase(temp)
    review_tokens.append(list(nltk.pos_tag(temp)))


    '''
    Showing progress in the Standard output.
    '.' ---> + 1%
    '|' ---> + 5%
    '''
    if i%1500==0:
        sys.stdout.write('|')
    elif i%300==0:
        sys.stdout.write('.')
    i+=1


'''
Create, for each review, a temp. Dictionary, with the following tags. Append them to the above list
'''
all_data = []   # List to store all processed data

for i in range(len(book_name_list)):
    tempDict = {"book_name":book_name_list[i], "help":helpful_list[i], "score":score_list[i], "review_tokens":review_tokens[i]}
    all_data.append(tempDict)


'''
Save the data to a local file
'''
np.save("all_data.npy",all_data)

###############################################################################################################################################