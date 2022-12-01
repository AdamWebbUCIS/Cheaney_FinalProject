from PIL import *
import json
#https://www.geeksforgeeks.org/read-json-file-using-python/
#might have to make all of this a function idk
f = open('EncryptedGroupHints.json')
hints = json.load(f)
Chean = hints['Cheaney']
print(type(Chean))
list_ = open("english.txt").read().split()

for x in Chean:
    print(list_[int(x)])
    
    
    
list_ = open("english.txt").read().split()
#print(list_[30941], list_[46341],list_[42060],list_[103567],list_[5039],list_[41699],list_[31065])

#def loadImage():
