import os
import re
import sys
from time import sleep

cur_dir = os.getcwd()
args = sys.argv
sleep_time = float(args[1]) if len(args) > 1 else 0.3

TXT_EXT = '.txt'
IMG_DIR = 'img_text'
img_text_dir = cur_dir + '/' + IMG_DIR
img_text_dir = args[2] if len(args) > 2 else img_text_dir

files = os.listdir(img_text_dir)
cnt = 1 
for file in files:
    index = re.search(TXT_EXT, file)
    if index:
        cnt = cnt + 1

while True:
    for i in range(1, cnt):
        f = open('./' + IMG_DIR + '/' + str(i) + TXT_EXT)
        data = f.read()
        f.close()

        lines = data.split('\n')
        for line in lines:
            print(line)

        sleep(sleep_time);
        os.system('cls')
