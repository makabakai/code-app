"""
马云飞
2020118092
"""


# this function returns True if filename is a BMP file and False if it is not
def confirm_bmp(filename):
    try:
        file = open(filename, 'rb')
        data = bytearray(file.read())
        file.close()
        if data[0] == 0x42 and data[1] == 0x4D:
            return True
        else:
            return False
    except:
        print(filename, 'could not be opened.')


# this function returns the number of bytes which the .bmp file
def bmp_size(filename):
    if not confirm_bmp(filename):
        print(filename, 'is not a BMP file')
        return -1
    try:
        file = open(filename, 'rb')
        data = bytearray(file.read())
        file.close()
        size = data[5] * 0x1000000 + data[4] * 0x10000 + data[3] * 0x100 + data[2]
        return int(size)
    except:
        print(filename, 'could not be opened.')


# this function reads in filename1 and alters the image.
# Then it writes the new image to filename2
def alter_bmp(filename1, filename2):
    if not confirm_bmp(filename1):
        print(filename1, 'is not a BMP file')
        return -1
    try:
        file1 = open(filename1, 'rb')
        file2 = open(filename2, 'wb')
        data = bytearray(file1.read())
        file1.close()
        for i in range(54):
            file2.write(data[i].to_bytes(1, byteorder='big'))
        for bt in data[54:]:
            if bt < 0xC8:
                file2.write((bt + 0x28).to_bytes(1, byteorder='big'))
            else:
                file2.write(bt.to_bytes(1, byteorder='big'))
        file2.close()
    except:
        print(filename1, 'could not be opened.')


"""
>>> confirm_bmp('it_building.bmp')
True
>>> bmp_size('it_building.bmp'))
7991350
The picture new_image.bmp looks quite strange,and some parts of it become red.
"""

