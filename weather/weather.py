import json
from argparse import ArgumentParser
import sys

try:
    import xmltodict
except ModuleNotFoundError:
    import subprocess
    subprocess.call([sys.executable, "-m", "pip", "install", 'xmltodict'])
    import xmltodict

if sys.argv[1]:
    inputFileName = sys.argv[1]
    with open(inputFileName, 'r') as read_file:
        doc = xmltodict.parse(read_file.read())
else:
    inputType = int(
        input('Select input type :\n1 : text\n2 : xml file\n3 : exit program\n'))

    if inputType == 1:
        text = []
        print('** After finish entering input please press ENTER again **')
        print('Enter your xml text :')
        while True:
            line = str(input())
            if line:
                text.append(line)
            else:
                text = line.join(text)
                break

        doc = xmltodict.parse(text)
        inputFileName = str(input('Enter output file name : '))
        if '.xml' not in inputFileName:
            inputFileName += '.xml'

    if inputType == 2:
        inputFileName = ''
        tryAgain = True
        while tryAgain:
            try:
                inputFileName = str(input('Enter input file name/location: '))
                with open(inputFileName, 'r') as read_file:
                    doc = xmltodict.parse(read_file.read())
                tryAgain = False
            except FileNotFoundError:
                print('File not found. Please try again')

    if inputType == 3:
        exit(0)

with open(inputFileName.replace('.xml', '.json'), 'w') as write_file:
    json.dump(doc, write_file)

print('Complete!')
