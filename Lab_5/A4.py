
def file_open(file, row):
    xfile = open(file, 'r')
    i=0
    for s in xfile:
        n=s.split('\t')
        if i==row:
            break
        i+=1
    return n
print(file_open('sequences.0.txt', 1))

