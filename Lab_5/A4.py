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
def process_commands(seq_file, cmd_file, out_file):
    proteins = file_open(seq_file)
    results = []
    xfile = open(cmd_file, 'r')
    commands = xfile.readlines()
    for idx, cmd in enumerate(commands, 1):
        cmd = cmd.strip()
        if not cmd:
            continue
        
        op_parts = cmd.split('\t')
        op_name = op_parts[0]
        
        if op_name == 'search':
            pattern = op_parts[1]
            found = []
            for name, (org, seq) in proteins.items():
                if pattern in seq:
                    found.append((org, name))
            results.append((idx, 'search', pattern, found))
        



