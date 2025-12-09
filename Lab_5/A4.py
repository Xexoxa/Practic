import re
import string
def file_open(file):
    xfile = open(file, 'r')
    proteins = {}
    for line in xfile:
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                name = parts[0]
                org = parts[1]
                seq = parts[2]
                proteins[name] = (org, seq)
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
        elif op_name == 'diff':
            prot1, prot2 = op_parts[1], op_parts[2]
            if prot1 not in proteins or prot2 not in proteins:
                missing = []
                if prot1 not in proteins:
                    missing.append(prot1)
                if prot2 not in proteins:
                    missing.append(prot2)
                results.append((idx, 'diff', (prot1, prot2), 'MISSING: ' + ', '.join(missing)))
            else:
                seq1 = proteins[prot1][1]
                seq2 = proteins[prot2][1]
                min_len = min(len(seq1), len(seq2))
                diff_count = sum(1 for i in range(min_len) if seq1[i] != seq2[i])
                diff_count += abs(len(seq1) - len(seq2))
                results.append((idx, 'diff', (prot1, prot2), diff_count))
        elif op_name == 'mode':
            prot_name = op_parts[1]
            if prot_name not in proteins:
                results.append((idx, 'mode', prot_name, 'MISSING: ' + prot_name))
            else:
                seq = proteins[prot_name][1]
                freq = {}
                for aa in seq:
                    freq[aa] = freq.get(aa, 0) + 1
                max_count = max(freq.values())
                most_common = min([aa for aa, cnt in freq.items() if cnt == max_count])
                results.append((idx, 'mode', prot_name, (most_common, max_count)))
        f=open(out_file, 'w')
        f.write("Ignatchik Mark\n")
        f.write("Genetic Searching\n")
        for idx, op, param, res in results:
            f.write("--------------------------------------------------------------------------\n")
            f.write(f"{idx:03d} {op} {param if isinstance(param, str) else ' '.join(param)}\n")
            if op == 'search':
                f.write(f"{'organism':<30} {'protein'}\n")
                if res:
                    for org, name in res:
                        f.write(f"{org}\t{name}\n")
                else:
                    f.write("NOT FOUND\n")
            elif op == 'diff':
                f.write("amino-acids difference:\n")
                f.write(f"{res}\n")
            elif op == 'mode':
                f.write("amino-acid occurs:\n")
                if isinstance(res, tuple):
                    f.write(f"{res[0]}\t{res[1]}\n")
                else:
                    f.write(f"{res}\n")
process_commands("sequences.1.txt", "commands.1.txt", "genedata.1.txt")                    


