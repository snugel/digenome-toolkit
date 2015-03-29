from sys import argv # [-s] [-c count_cutoff] [-r ratio_cutoff], [-g differnce], forward 1, reverse 1, forward 2, reverse 2, ...

fr = 5
count_cutoff = 10
ratio_cutoff = 20.0
difference = 1
sum_cutoffs = False

fns = []
for i in range(1, len(argv)):
    if i != len(argv)-1 and argv[i] == "-r":
        ratio_cutoff = float(argv[i+1])
    elif i != len(argv)-1 and argv[i] == "-g":
        difference = int(argv[i+1])
    elif i != len(argv)-1 and argv[i] == "-c":
        count_cutoff = int(argv[i+1])
    elif argv[i] == "-s":
        sum_cutoffs = True
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
            forward_dic[pos] = (count, depth, ratio, line)

    ffnhead = '.'.join(ffn.split('.')[:-1])
    frnhead = '.'.join(frn.split('.')[:-1])

    print ("Comparing it with reverse information from {} and writing to file...".format(frn))
    with open(frn) as f,\
         open(ffnhead + "_%d_%.1f%%_diff_%d%s.txt"%(count_cutoff, ratio_cutoff, difference, "_summed" if sum_cutoffs else ""), "w") as ffo,\
         open(frnhead + "_%d_%.1f%%_diff_%d%s.txt"%(count_cutoff, ratio_cutoff, difference, "_summed" if sum_cutoffs else ""), "w") as fro:
        if sum_cutoffs:
            fso = open(ffnhead.replace('_forward', '') + "_%d_%.1f%%_diff_%d%s.txt"%(count_cutoff, ratio_cutoff, difference, "_summed" if sum_cutoffs else ""), "w")
        for line in f:
            entries = line.split('\t')
            pos_rev = int(entries[0])
            pos_for = pos_rev+difference
            try:
                count_for, depth_for, ratio_for, line_for = forward_dic[pos_for]
            except:
                continue
            count_rev = int(entries[1])
            depth_rev = int(entries[2])
            ratio_rev = float(entries[3])

            if not sum_cutoffs and (count_rev >= count_cutoff and not ratio_rev < ratio_cutoff and count_for >= count_cutoff and not ratio_for < ratio_cutoff):
                ffo.write(line_for)
                fro.write(line)
            elif sum_cutoffs and (count_rev+count_for >= count_cutoff and not ratio_rev+ratio_for < ratio_cutoff):
                ffo.write(line_for.strip())
                fro.write(line.strip())
                fso.write(line_for.strip() + '\t' + line.strip() + '\t%d\t%d\t%.1f\n'%(count_rev+count_for, depth_rev+depth_for, ratio_rev+ratio_for))
        if sum_cutoffs:
            fso.close()
