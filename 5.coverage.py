import re
import pysam
from sys import argv # argv[1]: "WT" or "RGEN", argv[2]: PATH of BAM file
from os import path

linechunk = []
prev_pos = -1
prev_chrom = ""

depth_dic = {}

def process_chunk(linechunk):
    for chrom, pos, cigar in linechunk:
        cur_pos = pos
        pos_back = 0
        leftflag = True
        for s, n in cigar:
            if not leftflag or (s != 4 and s != 5):
                for pos_diff in range(n):
                    if (s != 1 and s != 4 and s != 5):
                        if (cur_pos-pos_back) in depth_dic:
                            depth_dic[cur_pos-pos_back] += 1
                        else:
                            depth_dic[cur_pos-pos_back] = 1
                    if s == 1:
                        pos_back += 1
                    cur_pos += 1
                leftflag = False
                
if True:
    f = pysam.Samfile(argv[2], "rb")
    depth_dic = {}
    for cnt, ar in enumerate(f):
        chrom = f.getrname(ar.tid)
        if prev_chrom != chrom:
            if prev_chrom != "":
                fo.close()
            print ("Processing " + chrom + "...")
            prev_chrom = chrom
            fo = open(argv[1]+"_"+chrom+"_depth.txt", "w")
        pos = ar.pos+1
        cigar = ar.cigar
        
        if pos != prev_pos:
            if prev_pos != -1:
                process_chunk(linechunk)
                for i in range(prev_pos, pos):
                    try:
                        fo.write('%s:%d\t%d\n'%(chrom, i, depth_dic[i]))
                        del depth_dic[i]
                    except KeyError:
                        fo.write('%s:%d\t%d\n'%(chrom, i, 0))

            prev_pos = pos
            linechunk = [ (chrom, pos, cigar) ]
        else:
            linechunk.append( (chrom, pos, cigar) )
        if cnt % 100000 == 0:
            print (pos)

    process_chunk(linechunk)
    for i in range(pos, pos+150):
        try:
            fo.write('%s:%d\t%d\n'%(chrom, i, depth_dic[i]))
        except KeyError:
            fo.write('%s:%d\t%d\n'%(chrom, i, 0))

    f.close()
    fo.close()    
