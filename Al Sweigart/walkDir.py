# -*- coding: cp1251 -*-
import os


for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('Текущая папка - ' + folderName)

    for subfolder in subfolders:
        print('Подпапка папки ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('Файл в папке ' + folderName + ': ' + filename)
    print(' ')
