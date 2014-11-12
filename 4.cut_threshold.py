chrs = list(map(str, list(range(1, 23)))) + ['X']

fns = 'forward', 'reverse_sorted'
fr = 5

types = "WT", "RGEN"

for type in types:
    for cn in chrs:
        for fn in fns:
            print ('Processing chr' + cn + '_' + fn + '_freq.txt...')
            f = open(type+'_chr' + cn + '_' + fn + '_freq.txt')
            fo = open(type+'_chr' + cn + '_' + fn + '_freq_from_' + str(fr) + '.txt', 'w')
            for line in f:
                entries = line.split('\t')
                cnt = int(entries[1])
                if fr <= cnt:
                    fo.write(line)
            fo.close()
            f.close()
