from sys import argv

fr = 5

for fn in argv[1:]:
    print ('Processing {}...'.format(fn))
    f = open(fn)
    fnhead = '.'.join(fn.split('.')[:-1])
    fo = open('{}_from_{}.txt'.format(fnhead, fr), 'w')
    for line in f:
        entries = line.split('\t')
        cnt = int(entries[1])
        if fr <= cnt:
            fo.write(line)
    fo.close()
    f.close()
