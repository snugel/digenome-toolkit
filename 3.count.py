chrs = list(map(str, list(range(1, 23)))) + ['X']

fns = 'forward', 'reverse_sorted'
types = "WT", "RGEN"

for type in types:
    for cn in chrs:
        for fn in fns:
            print ('Processing chr' + cn + '_' + fn + '.txt...')
            f = open(type + '_chr' + cn + '_' + fn + '.txt')
            fo = open(type + '_chr' + cn + '_' + fn + '_freq.txt', 'w')
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
