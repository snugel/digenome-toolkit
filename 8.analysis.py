from sys import argv # forward 1, reverse 1, forward 2, reverse 2, ...

count_cutoff = 10
ratio_cutoff = 24.99
fr = 5

fns = zip(argv[1::2], argv[2::2])

# Read forward information
for ffn, frn in fns:
    forward_dic = {}
    print ("Reading forward information from {}...".format(ffn))
    with open(ffn) as f:
        for line in f:
            entries = line.split('\t')
            pos = int(entries[0])
            count = int(entries[1])
            depth = int(entries[2])
            ratio = float(entries[3])
            if count >= count_cutoff and ratio > ratio_cutoff:
                forward_dic[pos] = (count, ratio, line)

    ffnhead = '.'.join(ffn.split('.')[:-1])
    frnhead = '.'.join(frn.split('.')[:-1])

    print ("Comparing it with reverse information from {} and writing to file...".format(frn))
    with open(frn) as f,\
         open(ffnhead + "_%d_%.1f.txt"%(count_cutoff, ratio_cutoff), "w") as ffo,\
         open(frnhead + "_%d_%.1f.txt"%(count_cutoff, ratio_cutoff), "w") as fro:
        for line in f:
            entries = line.split('\t')
            pos = int(entries[0])
            count = int(entries[1])
            ratio = float(entries[3])
            if count >= count_cutoff and ratio > ratio_cutoff:
                try:
                    ffo.write(forward_dic[pos+1][2])
                    fro.write(line)                    
                except KeyError:
                    pass
