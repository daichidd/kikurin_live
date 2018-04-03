import os
import re
from time import sleep

curDir = os.getcwd()

TXT_EXT = '.txt'
IMG_DIR = 'img_text'
imgTextDir = curDir + '/' + IMG_DIR

files = os.listdir(imgTextDir)
cnt = 0
for file in files:
    index = re.search(TXT_EXT, file)
    if index:
        cnt = cnt + 1

while True:
    for i in range(1, cnt + 1):
        f = open('./' + IMG_DIR + '/' + str(i) + TXT_EXT)
        data = f.read()
        f.close()

        lines = data.split('\n')
        for line in lines:
            print(line)

        sleep(0.3);
        os.system('cls')
