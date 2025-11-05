
def file_open(file):
    xfile = open(file, 'r')
    for s in xfile:
        n=s.split('\t')
        print(n)
print(file_open('sequences.0.txt'))

