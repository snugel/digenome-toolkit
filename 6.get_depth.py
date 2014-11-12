from glob import glob

chr_tails = list(map(str, range(1, 23))) + ["X"]
directions = "forward", "reverse"
types = "WT", "RGEN"
fr = 5

for type in types:
    for direction in directions:
        fo = open("%s_%s.txt"%(type, direction), "w")
        for chr_tail in chr_tails:
            print ("Processing chr" + chr_tail + "...")
            ffn = type+"_chr%s_%s_freq_from_%d.txt"%(chr_tail, direction, fr)
            fdn = type+"_chr%s_depth.txt"%chr_tail
            ff = open(ffn)
            fd = open(fdn)
            for ff_line in ff:
                pos = ff_line.split('\t')[0]
                while True:
                    fd_line = fd.readline()
                    try:
                        if fd_line.split('\t')[0].split(':')[1] == pos:
                            fo.write(fd_line)
                            break
                    except:
                        print (chr_tail, direction, type, ff_line, fd_line)
                        break
            ff.close()
        fo.write("\n")

