import numpy as np
from nltk.corpus import sentiwordnet as swn

###############################################################################################################################################

'''
<<<helpRatio>>>
Returns the float form of the helpfulness of the helpRatio

PARAMETERS: Helpfulness of the review (in the original String Form)
RETURN:     Float value of the helpfulness
'''

def helpRatio(help):

    help = help.strip(' \n')
    parts = help.split('/')

    if float(parts[1])==0:  # If the denominator is 0, then
        return 0            #                Return 0

    else:
        return (float(parts[0])/float(parts[1]))

###############################################################################################################################################

'''
Load data from the file created by 'create_all_data.py'
'''
all_data = np.load("all_data.npy")

help_list = []
i=0
for review in all_data:
    help_list.append([i,helpRatio(review["help"])])




###############################################################################################################################################