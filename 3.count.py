from sys import argv

for fn in argv[1:]:
    print ('Processing {}...'.format(fn))
    fnhead = '.'.join(fn.split('.')[:-1])
    f = open(fn)
    fo = open(fnhead + '_freq.txt', 'w')
    prev = ""
    cnt = 0
    for line in f:
        line = line.strip()
        if line != prev:
            if cnt != 0:
                fo.write("%s\t%d\n"%(prev, cnt))
            prev = line
            cnt = 0
        cnt += 1
    fo.write("%s\t%d"%(prev, cnt))
    fo.close()
    f.close()
