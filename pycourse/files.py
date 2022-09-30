"""
马云飞
2020118092
"""

import os


# states the current working directory, says the number of files in the directory
# and gives a breakdown of the files by file type.
def show_files(dir=os.getcwd(), types=[]):
    print('Current Working Directory:', os.getcwd())
    print('Required Directory:', dir, '\n')
    if os.getcwd() != dir:
        os.chdir(dir)
    file_list = os.listdir()
    print('Total files:', len(file_list), '\n')
    print('%-11s%-10s' % ('Extension', 'Frequency'))
    count = {}
    if len(types) == 0:
        for file in file_list:
            if not (file.split('.')[1] in count.keys()):
                count[file.split('.')[1]] = 1
            else:
                count[file.split('.')[1]] += 1
    else:
        for file in file_list:
            if file.split('.')[1] in types:
                if not (file.split('.')[1] in count.keys()):
                    count[file.split('.')[1]] = 1
                else:
                    count[file.split('.')[1]] += 1
    for i, j in count.items():
        print('%-11s%-10s' % ('.' + i, j))


show_files('E:\\pycharm\\files\\sample', ['py', 'txt'])


"""
>>> show_files('E:\\pycharm\\files\\sample')
Current Working Directory: E:\pycharm\files
Required Directory: E:\pycharm\files\sample

Total files: 15

Extension  Frequency
.py        2         
.txt       4         
.doc       3         
.doc~      1         
.pptx      3         
.exe       2

>>> show_files('E:\\pycharm\\files\\sample', ['py', 'txt'])
Current Working Directory: E:\pycharm\files
Required Directory: E:\pycharm\files\sample

Total files: 15

Extension  Frequency 
.py        2         
.txt       4         

"""
