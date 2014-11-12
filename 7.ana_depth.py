types = "WT", "RGEN"
depth_cutoff = 0.0
fr = 5

directions = "forward", "reverse"
chromosomes = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","X")

for type in types:
    depth_dic = {}
    filenames = (type+"_%s.txt", type+"_chr%s_%s_freq_from_"+str(fr)+".txt", type+"_chr%s_ana_%s_from_"+str(fr)+"_depth.txt")


    print ("Reading depth information files...")
    # Read depth information
    for direction in directions:
        with open(filenames[0]%direction) as f:
            for line in f:
                entries = line.split('\t')
                if len(entries) < 2:
                    continue
                chromosome, position = entries[0].split(':')[:2] # For safety
                depth = int(entries[1])
                if depth != 0:
                    if not chromosome + direction in depth_dic:
                        depth_dic[chromosome + direction] = {}
                    depth_dic[chromosome+direction][int(position)] = depth

    # Read count information and print results
    for chromosome in chromosomes:
        print ("Processing chr%s..."%chromosome)
        for direction in directions:
            print ("Processing %s direction..."%direction)
            with open(filenames[1]%(chromosome, direction)) as f, \
                 open(filenames[2]%(chromosome, direction), "w") as fo:
                for line in f:
                    entries = line.split('\t')
                    position = entries[0]
                    count = entries[1].strip()
                    try:
                        depth = depth_dic["chr"+chromosome+direction][int(position)]
                        depth_percent = int(count)*100.0/depth
                        if depth_percent >= depth_cutoff:
                            fo.write("%s\t%s\t%d\t%.1f\n"%(position, count, depth, depth_percent))
                    except KeyError:
                        pass
