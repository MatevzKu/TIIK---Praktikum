# -*- coding: utf-8 -*-

def compress(uncompressed,dictionary):
    """Compress a string to a list of output symbols."""

    # Build the dictionary.
    #dict_size = 256
    #dictionary = dict((chr(i), i) for i in range(dict_size))
    # in Python 3: dictionary = {chr(i): i for i in range(dict_size)}
    dict_size = len(dictionary)
    #dictionary = {'B': 0, 'I': 1, 'T': 2, 'A': 3, 'L': 4, 'N': 5, 'E': 6}
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        #print(wc)
        #print(w)
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w.
    if w:
        result.append(dictionary[w])
    print(dictionary)
    return result


def decompress(compressed,dictionary):
    """Decompress a list of output ks to a string."""
    from io import StringIO

    # Build the dictionary.
    #dict_size = 256
    #dictionary = dict((i, chr(i)) for i in range(dict_size))
    # in Python 3: dictionary = {i: chr(i) for i in range(dict_size)}
    dict_size = len(dictionary)
    #dictionary = {0: 'B', 1: 'I', 2: 'T', 3: 'A', 4: 'L', 5: 'N', 6: 'E'}

    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    result = StringIO()
    w = dictionary[compressed.pop(0)]
    #print(w)
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)

        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    print(dictionary)
    return result.getvalue()


# How to use:
input_string = "BITIALINEBITI"

# Initialize dictionaries
char_to_num = {}
num_to_char = {}
count = 0

# Iterate through the string
for char in input_string:
    if char not in char_to_num:
        # If the character is not already in char_to_num, add it and assign a numerical value
        char_to_num[char] = count
        num_to_char[count] = char
        count += 1

# Print the dictionaries
print("char_to_num:", char_to_num)
print("num_to_char:", num_to_char)

print(len(char_to_num))


compressed = compress(input_string,char_to_num)
print (compressed)
decompressed = decompress(compressed,num_to_char)
print (decompressed)