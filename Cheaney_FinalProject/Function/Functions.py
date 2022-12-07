'''
Name: Alex Bridge, Adam Krisciunas, Adam Webb, Ryan Lupton
email: bridgeax@mail.uc.edu, krisciag@mail.uc.edu, webb2at@mail.uc.edu, luptonrj@mail.uc.edu
Assignment: Final Project
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Decode a location on campus, take a picture there, and write code to show the picture
'''
from PIL import Image
import json
#https://www.geeksforgeeks.org/read-json-file-using-python/
#might have to make all of this a function idk
def loadHints():
    f = open('EncryptedGroupHints.json')
    hints = json.load(f)
    Chean = hints['Cheaney']
    list_ = open("english.txt").read().split()
    for x in Chean:
        print(list_[int(x)])
    list_ = open("english.txt").read().split()
    return list_[30941], list_[46341],list_[42060],list_[103567],list_[5039],list_[41699],list_[31065]
#print(list_[30941], list_[46341],list_[42060],list_[103567],list_[5039],list_[41699],list_[31065])


def loadImage():
    f = "baseball.jpg"
    img = Image.open(f)
    return img.show()

