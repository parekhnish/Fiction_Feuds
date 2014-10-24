import numpy as np
from nltk.corpus import sentiwordnet as swn

###############################################################################################################################################

'''
Load data from the file created by 'create_all_data.py'
'''
all_data = np.load("all_data.npy")


'''
Sort tokens into Adjectives, Adverbs, Nouns, and Verbs
Append the above list with a 2-list, with the second part containing the appropriate character denoting the type of word
'''
LOTR_BoxedSet = []

for data in all_data:
    if data["book_name"]==" The Lord of the Rings - Boxed Set" and data["score"]<=2:
        for word in data["review_tokens"]:
            if word[1]=="JJ" or word[1]=="JJR" or word[1]=="JJS":   #-------------------------------------------------------- Adjectives
                LOTR_BoxedSet.append([word[0],'a'])
            elif word[1]=="RB" or word[1]=="RBR" or word[1]=="RBS" or word[1]=="WBR":   #------------------------------------ Adverbs
                LOTR_BoxedSet.append([word[0],'r'])
            elif word[1]=="NN" or word[1]=="NNS" or word[1]=="NNP" or word[1]=="NNPS":  #------------------------------------ Nouns
                LOTR_BoxedSet.append([word[0],'n'])
            elif word[1]=="VB" or word[1]=="VBD" or word[1]=="VBG" or word[1]=="VBN" or word[1]=="VBP" or word[1]=="VBZ":   # Verbs
                LOTR_BoxedSet.append([word[0],'v'])


'''
Populate a list with Synsets, based on the tokens found above
'''
LOTR_BoxedSet_Synsets = []
for word in LOTR_BoxedSet:
    LOTR_BoxedSet_Synsets.append(list(swn.senti_synsets(word[0],word[1])))


'''
Populate a list with all negative Synsets, from above
'''
LOTR_BoxedSet_Synsets_neg = []
for lst in LOTR_BoxedSet_Synsets:
    for word in lst:
        if word.neg_score() > word.pos_score(): #--------- Word is negative, if its negative score is more than positive score
            LOTR_BoxedSet_Synsets_neg.append(word)


'''
Manually, make a SET of the above tokens
NOTE:   This is done because the Python keyword 'set' fails to distinguish between the same Synsets
'''
LOTR_BoxedSet_negWords = []
LOTR_BoxedSet_Synset_negWords = []

for ss in LOTR_BoxedSet_Synsets_neg:
    if not(ss.synset.name() in LOTR_BoxedSet_negWords):
        LOTR_BoxedSet_negWords.append(ss.synset.name())
        LOTR_BoxedSet_Synset_negWords.append(ss)


'''
Sort the Obtained Synsets, based on their negative score
'''
LOTR_BoxedSet_Synset_negWords.sort(key=lambda x:x.neg_score(), reverse=True)



for word in LOTR_BoxedSet_Synset_negWords:
    print word