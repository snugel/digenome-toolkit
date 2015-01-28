from sys import argv # [-p prefix], [-d direction], freq files...

depth_cutoff = 0.0
fr = 5

prefix = ""
direction = ""

fns = []
for i in range(1, len(argv)):
    if i != len(argv)-1 and argv[i] == "-p":
        prefix = argv[i+1] + "_"
    elif i != len(argv)-1 and argv[i] == "-d":
        direction = argv[i+1]
    elif i != 1 and argv[i-1] != "-p" and argv[i-1] != "-d":
        fns.append(argv[i])

if direction != "":
    depth_dic = {}
    fn_depth = prefix+direction+".txt"

    print ("Reading depth information files...")

    # Read depth information
    with open(fn_depth) as f:
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
    for fn in fns:
        print ("Processing {}...".format(fn))
        fnhead = ".".join(fn.split(".")[:-1])
        with open(fn) as f, open(fnhead + "_ana.txt", "w") as fo:
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
