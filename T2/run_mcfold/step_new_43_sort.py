#!/usr/bin/python

from common.base import partition

fninp = 'step_new_42_to_run.out'
fnout = 'step_new_43_sort.out'

lines = open(fninp).readlines()
bks = partition(lines, lambda x: x[:1]=='>', include='header')

data = []
for bk in bks:
    seqname = bk[0][1:].strip()
    seqstr = bk[1].strip()
    items = []
    for line in bk[2:]:
        fds = line.split()
        ss = fds[0]
        dG = float(fds[1])
        t = fds[2]
        items.append((ss,dG,t))
    data.append((seqname, seqstr, items))

result = filter(lambda x: len(x[2])>1 and x[2][0][1]==0.0 and
                x[2][1][2]=='Type2', data)
result.sort(key=lambda x: x[2][1][1])

f = open(fnout, 'wt')
for seqname,seqstr,items in result:
    f.write('>%s\n'%seqname)
    f.write('%s\n'%seqstr)
    for item in items:
        f.write('%s    %4.2f    %s\n'%item)
f.close()
