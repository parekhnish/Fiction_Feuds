import numpy as np
from nltk.corpus import sentiwordnet as swn

###############################################################################################################################################

def helpRatio(help):

    parts = help.split('/')
    print parts

    # if parts[1]==0:
    #     return 0

    # else:
    #     return ((float)parts[0]/(float)parts[1])

###############################################################################################################################################

'''
Load data from the file created by 'create_all_data.py'
'''
all_data = np.load("all_data.npy")


for review in all_data:
    print helpRatio(review["help"])


###############################################################################################################################################