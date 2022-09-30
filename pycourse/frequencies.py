"""
frequencies of words in a text
马云飞
2020118092
"""

# dictionary of frequencies of words
frequencies = {}


# calculate the frequency of each word in a single line
def calculate_frequencies(s):
    global frequencies
    s = s.split()
    for word in s:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1


# read in and process the text
def read_process_text(filename):
    try:
        f = open(filename, 'r')
        for line in f:
            line = line.lower()
            calculate_frequencies(line)
        f.close()
    except:
        print(filename, 'could not be opened.')


# print the frequency distribution
def print_frequency(d):
    print('%-10s%-4s' % ('Word', 'Freq'))
    for word, freq in d.items():
        print('%-10s%-4d' % (word, freq))


# frequency distribution
def freq_dist(filename):
    read_process_text(filename)
    print_frequency(frequencies)


"""
>>> freq_dist('animals.txt')
Word      Freq
the       8   
large     4   
cat       1   
watches   2   
dog       1   
in        2   
park      1   
fish      2   
small     2   
very      1   
whale     2   
and       1   
swim      1   
sea       1 
"""
