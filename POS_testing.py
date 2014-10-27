import numpy as np

###############################################################################################################################################

'''
Load data from the file created by 'create_all_data.py'
'''
all_data = np.load("all_data.npy")


'''
Creat an Empty Dictionary, with keys similar to that output by the NLTK POS Tagger
NOTE:   This Dictionary has no Symbol Keys, as they are useless anyway
'''
token_examples = {"CC":[], "CD":[], "DT":[], "EX":[], "FW":[], "IN":[], "JJ":[], "JJR":[], "JJS":[], "LS":[], "MD":[], "NN":[], "NNS":[], "NNP":[], "NNPS":[], "PDT":[], "POS":[], "PRP":[], "PRP$":[], "RB":[], "RBR":[], "RBS":[], "RP":[], "SYM":[], "TO":[], "UH":[], "VB":[], "VBD":[], "VBG":[], "VBN":[], "VBP":[], "VBZ":[], "WDT":[], "WP":[], "WP$":[], "WRB":[]}


'''
Populate the above dictionary with tokens from the data.
'''
for i in range(len(all_data)):
    if all_data[i]["book_name"]==" The Lord of the Rings - Boxed Set":  # Specify book name
        for token in all_data[i]["review_tokens"]:
            if token[1] in token_examples:  #---------------------------- Ignore all symbols
                token_examples[token[1]].append(token[0])



print sorted(set(token_examples["RB"]))