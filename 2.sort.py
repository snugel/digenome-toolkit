from sys import argv # all reverse should be sorted

for arg in argv[1:]:
    print ("Reading...")
    with open(arg) as f:
        l = [int(line) for line in f]
    print ("Sorting...")
    l.sort()
    print ("Writing...")
    fns = arg.split(".")
    with open('.'.join(fns[:-1]) + "_sorted.txt", 'w') as fo:
        fo.write('\n'.join(map(str, l)))
