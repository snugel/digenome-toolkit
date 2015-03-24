from sys import argv # [-r ratio_cutoff], [-g differnce], forward 1, reverse 1, forward 2, reverse 2, ...

fr = 5
count_cutoff = 10
ratio_cutoff = 20.0
difference = 1

fns = []
for i in range(1, len(argv)):
    if i != len(argv)-1 and argv[i] == "-r":
        ratio_cutoff = float(argv[i+1])
    elif i != len(argv)-1 and argv[i] == "-g":
        difference = int(argv[i+1])
    elif i != len(argv)-1 and argv[i] == "-c":
        count_cutoff = int(argv[i+1])
    elif i != 0 and argv[i-1] != "-r" and argv[i-1] != "-g" and argv[i-1] != "-c":
        fns.append(argv[i])

fns = zip(fns[::2], fns[1::2])

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
         open(ffnhead + "_%d_%.1f%%_diff_%d.txt"%(count_cutoff, ratio_cutoff, difference), "w") as ffo,\
         open(frnhead + "_%d_%.1f%%_diff_%d.txt"%(count_cutoff, ratio_cutoff, difference), "w") as fro:
        for line in f:
            entries = line.split('\t')
            pos = int(entries[0])
            count = int(entries[1])
            ratio = float(entries[3])
            if count >= count_cutoff and not ratio < ratio_cutoff:
                try:
                    ffo.write(forward_dic[pos+difference][2])
                    fro.write(line)                    
                except KeyError:
                    pass
