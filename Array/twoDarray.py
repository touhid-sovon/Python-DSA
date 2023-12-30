import numpy as np

twoDarray = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

# print(twoDarray)

''' Insertion '''

# new2Darray = np.insert(twoDarray,1,[11,11,11,11],axis=1)
"""
second argument can be 0---n that denotes the row number
last argument axis denotes where we want to insert the value axis=0 means adding data in row and 1 means column
"""

# new_2_2Darray = np.insert(twoDarray,1,[11,11,11,11],axis=0)

# print(new_2_2Darray)

'''apend Method'''

new2Darray = np.append(twoDarray,[[22,22,22,22]],axis=0)

print(new2Darray)
