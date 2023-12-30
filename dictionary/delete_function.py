mydict = {'Name':'Sovon','School':'BZS','College':'Hatem Ali ','University':'BU'}

# pop mrthod --- removes the value and key and takes key as a parameter
#mydict.pop('Name')

#popitem -- doesnt take any arguments and delete any random key value pair mainly last key value pair
#mydict.popitem()

# delete method -- same as pop
#del mydict['College']

# clear method -- deletes the whole dictionary
#mydict.clear()

#print(mydict)

# copy method
new_dict = mydict.copy()

# print(new_dict)

# from keys method
new_dict2 = {}.fromkeys([1,2,3],0)

# print(new_dict2)

# get method

''' get methods return a value according to the key. The key value exist it will return the value ,else the second 
paramter '''


#print(mydict.get('Priamry School','Barishal College'))
#print(mydict.get('College','Barishal College'))

'''Keys method: returns all the keys of a dictionary as a list'''
#print(mydict.keys())

'''Keys method: returns all the keys of a dictionary as a list'''
#print(mydict.values())

'''pop method'''
#print(mydict.pop('University'))

''' Update method: like extends method of list, concatenate two dictionaries '''

new_dict3 = {1:'one',2:'two',3:'three'}

mydict.update(new_dict3)
#print(mydict)

# Looping through Dictionaries:
for i ,j in mydict.items():
    #print(f"{i}:{j}")
    pass

''' all method--- if all values are true it will return True else false '''

print(all(mydict))

mydict['age'] = None
mydict['Good_Looking'] = False

# print(mydict)
# print(all(mydict))

'''any method -- if all are false it will return false else true'''

# print(any(mydict))

'''sorted'''
new = {'nameeee':'sovon','address':'Barishal','mobile':'realmeX2'}

print(sorted(new,key=len))
print(sorted(new,reverse=True))