'''
lineage_counter.py

A script to count the number of each kazi lineage in the six ancestor competition assays.

8/21/12
'''

import gzip

folders = ['10k-r-0002_','10k-r-002_','10k-r-01_','5k-r-0002_','5k-r-002_','5k-r-01_','1k-r-0002_','1k-r-002_','1k-r-01_','10k-u-0002_','10k-u-002_','10k-u-01_','5k-u-0002_','5k-u-002_','5k-u-01_','1k-u-0002_','1k-u-002_','1k-u-01_']
runs = range(51, 81)

for folder in folders:
    lineages = [0,0,0,0,0,0]
    for seed in runs:
        workline = gzip.open(folder+str(seed)+'/data/average.dat.gz', 'rb').readlines()[-1]
        split = workline.split()
        lineage = split[-2]
        if lineage == '0':
            lineages[0] += 1
        elif lineage == '1':
            lineages[1] += 1
        elif lineage == '2':
            lineages[2] += 1
        elif lineage == '3':
            lineages[3] += 1
        elif lineage == '4':
            lineages[4] += 1
        elif lineage == '5':
            lineages[5] += 1
        else:
            print "indeterminate ", folder, seed
            print "lineage = ", lineage

    print folder, ' ', lineages
