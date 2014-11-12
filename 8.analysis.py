types = "WT", "RGEN"

count_cutoff = 10
ratio_cutoff = 24.99

chromosomes = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","X")
directions = "forward", "reverse"

for type in types:
    filenames = (type+"_%s.txt", type+"_chr%s_ana_%s_from_"+str(fr)+"_depth.txt", type+"_chr%s_ana_%s_"+str(fr)+"_%d_%.1f%%.txt")

    # Read forward information
    for chromosome in chromosomes:
        forward_dic = {}
        print ("Reading forward information of chr%s..."%chromosome)
        with open(filenames[1]%(chromosome, directions[0])) as f:
            for line in f:
                entries = line.split('\t')
                pos = int(entries[0])
                count = int(entries[1])
                depth = int(entries[2])
                ratio = float(entries[3])
                if count >= count_cutoff and ratio > ratio_cutoff:
                    forward_dic[pos] = (count, ratio, line)
        print ("Comparing it with reverse information and writing to file...")
        with open(filenames[1]%(chromosome, directions[1])) as f,\
             open(filenames[2]%(chromosome, directions[0], count_cutoff, ratio_cutoff), "w") as ffo,\
             open(filenames[2]%(chromosome, directions[1], count_cutoff, ratio_cutoff), "w") as fro:
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
