import tkinter
from tkinter import filedialog
import os
import random
import ast


root = tkinter.Tk()
root.withdraw()


def generate_dict():

    result = {}
    usedHex = set()

    for i in range(32, 126):
        while True:
            randNumber = random.randint(1, 100)
            hexValue = hex(i + randNumber).replace('0x', '')
            if hexValue not in usedHex:
                result[i] = hexValue
                usedHex.add(hexValue)
                break
    return result


diction = generate_dict()
print (diction)

def get_key(val, currDict):
    dictSelected = currDict
    for key, value in dictSelected.items():
        if val == value:
            return key
    return 00


def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    return tempdir


file_path_variable = search_for_file_path()
encrypted_path = "{}.encrypted.txt".format(file_path_variable.replace('.txt', ''))
decrypted_path = "{}.decrypted.txt".format(file_path_variable.replace('.txt', ''))

while len(file_path_variable) <= 0:
    print ("\nSorry, but you need to select a file.")
    search_for_file_path()



file1 = open(file_path_variable, 'r')

file2 = open(encrypted_path, "w").close()
file2 = open(encrypted_path, "a")


file2.writelines("{}\n".format(diction))


Lines = file1.readlines()

    

for line in Lines:
    file2.writelines("{}\n".format(line.strip().translate(diction)))

file2.close()
file1.close()


file3 = open(encrypted_path, "r")

file4 = open(decrypted_path, "w").close()
file4 = open(decrypted_path, "a")

AllLines = file3.readlines()
Lines2 = AllLines[1:]
dictionary = AllLines[0]
dictionary = ast.literal_eval(str(dictionary))

for line in Lines2:
    decrypt = ''
    line = line.strip('\n')
    length = len(line)
    for i in range(0, length, 2):
        cur_char = "{}{}".format(line[i], line[i+1])
        decrypt += chr(int(get_key(cur_char, dictionary)))
    print ("Encoded: {}".format(line))
    print ("Decrypted: {}".format(decrypt))
    file4.writelines("{}\n".format(decrypt))

file3.close()
file4.close()
