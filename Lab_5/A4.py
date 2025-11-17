import re
import string
def file_open(file):
    xfile = open(file, 'r')
    proteins = {}
    for line in xfile:
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                name = parts[0]
                organism = parts[1]
                sequence = parts[2]
                proteins[name] = (organism, sequence)
    return proteins
def encode(st):
    n='none'
    i=0
    count=1
    for char in st:
        if n==char: count+=1
        elif count>2:
            st=st.replace(st[i-count:i-1], str(count))
            i=i-count+2
            count=1
        else:count=1
        n=char
        i+=1
    return st
print(file_open('sequences.0.txt', 2))
print(file_open('commands.0.txt', 2))


