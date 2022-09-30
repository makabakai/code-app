"""
马云飞
2020118092
"""

import os


# read in the image as binary file and put it in a bytearray
def read_image_file(bmp_infile):
    try:
        file = open(bmp_infile, 'rb')
        data = bytearray(file.read())
        file.close()
        return data
    except:
        print(bmp_infile, 'could not be opened')


# read in the text as a string and split it into characters
# 'I am a student.' => ['I',' ','a','m',' ','a',' ','s','t','u','d','e','n','t','.']
def read_text(message_file):
    try:
        file = open(message_file)
        message = file.read()
        file.close()
        return list(message)
    except:
        print(message_file, 'could not be opened')


# store a secret ASCII text message in a .bmp image file.
def code_message(bmp_infile, bmp_outfile, message_file, p, q):
    current_position = 54 + p  # starting position
    bmp_in = read_image_file(bmp_infile)
    message = read_text(message_file)
    bit_message = []
    for character in message:
        tmp = ord(character)    # char to ascii
        tmp_list = []
        for i in range(8):
            tmp_list.insert(0, tmp & 0b1)   # insert the current last bit into the first position\
            tmp = tmp >> 1                  # so that the order would not change
        bit_message += tmp_list
    for i in range(8):
        bit_message.append(0)  # mark the end of the message
    for bit in bit_message:
        bmp_in[current_position] &= 0b11111110  # set the last bit to be zero
        bmp_in[current_position] |= bit  # set the last bit to be the text bit
        current_position += q
    try:
        file = open(bmp_outfile, 'wb')
        for byte in bmp_in:
            file.write(byte.to_bytes(1, byteorder='big'))
        file.close()
    except IOError:
        print('write error')
    print('CODE SUCCESS')


# read in the .bmp image file with secret message and decode the message
def decode_message(bmp_infile, message_outfile, p, q):
    bmp_in = read_image_file(bmp_infile)
    current_position = 54 + p  # starting position
    message = ''
    while True:
        character = 0b0
        for i in range(8):
            bit = bmp_in[current_position] & 0b1  # extract the last bit
            character |= bit
            character = character << 1  # building up a byte from separate bits
            current_position += q
        message += chr(character >> 1)
        if character == 0b0:  # meeting the end of the message
            break
    try:
        file = open(message_outfile, 'w')
        file.write(message)
        file.close()
    except IOError:
        print('write error')
    print('DECODE SUCCESS')


# find the size of bmp_infile and the size of message_file.
# And shows whether  the bytes of message_file can be stored
# in the image bmp_infile with the values of p and q given.
def size_message(bmp_infile, message_file, p, q):
    size_bmp = os.path.getsize(bmp_infile)
    size_text = os.path.getsize(message_file)
    num_of_bits = size_text * 8
    available_bits = (size_bmp - (54 + p)) / q + 1
    if_fit = '' if num_of_bits <= available_bits else ' not '
    print('Size of ', bmp_infile, ': ', size_bmp, ' bytes', sep='')
    print('Size of ', message_file, ': ', size_text, ' bytes', sep='')
    print('p: ', p, ' q: ', q, sep='')
    print('The message will', if_fit, ' fit in the image file.', sep='')


"""
E:\pycharm\message>type secret.txt 
The Stele Forest or Beilin Museum is a museum for steles and stone sculptures\ 
in Beilin District in Xi'an, Northwest China. The museum, which is housed in a former Confucian Temple, has housed a\ 
growing collection of Steles since 1087. By 1944 it was the principal museum for Shaanxi province. Due to the large\ 
number of steles, it was officially renamed the Forest of Stone Steles in 1992. Altogether, there are 3,000 steles in\ 
the museum, which is divided into seven exhibitions halls, which mainly display works of Chinese calligraphy,\ 
painting and historical records. 

>>> from message import *
>>> code_message('flower.bmp', 'flower_message.bmp', 'secret.txt', 1, 50)
CODE SUCCESS
>>> size_message('flower.bmp', 'secret.txt', 1, 50)
Size of flower.bmp: 271630 bytes
Size of secret.txt: 571 bytes
p: 1 q: 50
The message will fit in the image file.
>>> decode_message('flower_message.bmp', 'message.txt', 1, 50)
DECODE SUCCESS

E:\pycharm\message>type message.txt 
The Stele Forest or Beilin Museum is a museum for steles and stone sculptures in\ 
Beilin District in Xi'an, Northwest China. The museum, which is housed in a former Confucian Temple, has housed a\ 
growing collection of Steles since 1087. By 1944 it was the principal museum for Shaanxi province. Due to the large\ 
number of steles, it was officially renamed the Forest of Stone Steles in 1992. Altogether, there are 3,000 steles in\ 
the museum, which is divided into seven exhibitions halls, which mainly display works of Chinese calligraphy,\ 
painting and historical records. 
"""
