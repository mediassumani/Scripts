
'''
    This script parses through a text file that contains an article. Within the article, there are some
    phone numbers. The job of this script is to recognize and find every single phone number(USA).
    Example : Phone number found : 8623427865
'''

import os

# Function to detect if a string passed as a parameter as a string
def isPhoneNumber(text):

    if len(text) != 12:
        return False
    for data in range(0,3):
        if isinstance(data, int) is False:
            return False
    if text[3] != '-':
        return False
    for data in range(4,7):
        if isinstance(data, int) != True:
            return false
    if text[7] != '-':
        return False
    for data in range(8,12):
        if isinstance(data, int) != True:
            return False
    return True

# Function to parse through the text file
def parse():
    file_path = 'article.txt'
    try:
        with open(file_path,r) as article:
            while True:
                current_line = article.readline()
                for index in rannge(len(current_line)):
                    chunk_of_data = current_line[index: index+12]
                    if isPhoneNumber(chunk_of_data):
                        print('Phone number found : ' + chunk_of_data)
                print('Done')

    except IOError:
        print("ERROR FOUND : FILE COULD NOT BE OPENED")


def main():


if __name__ == '__main__':
    main()
