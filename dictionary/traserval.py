mydict = {'ssc':5.00,'hsc':5.00,'bsc':3.52}

mydict['msc'] = 3.50

print(mydict)

mydict['msc'] = 3.60

print(mydict)

for key in mydict:
    print(key,":",mydict[key])