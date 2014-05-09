################## DON'T TOUCH ME ####################

import matplotlib.pyplot as plt
import time
import gzip

###################### OPTIONS #######################

FOLDERS = ['10k-r-01-50_','5k-r-01-50_','1k-r-01-50_','10k-r-0008-50_','5k-r-0008-50_','1k-r-0008-50_','10k-r-006-50_','5k-r-006-50_','1k-r-006-50_']
#FOLDERS = ['5k-r-002-50_']

#FOLDERS = ['10k-r-0002-50_','10k-r-002-50_','10k-r-02-50_','5k-r-0002-50_','5k-r-002-50_','5k-r-02-50_','1k-r-0002-50_','1k-r-002-50_','1k-r-02-50_','10k-u-0002-50_','10k-u-002-50_','10k-u-02-50_','5k-u-0002-50_','5k-u-002-50_','5k-u-02-50_','1k-u-0002-50_','1k-u-002-50_','1k-u-02-50_']
#FOLDERS = ['a_','b_','c_', 'd_','e_','f_','g_','h_','i_','j_','k_','l_','m_','n_','o_','p_','q_','r_']
WORKINGFILE = "data/average.dat.gz"

STARTSEED = 51
ENDSEED = 80




############## CODE ##########



for FOLDER in FOLDERS:
    print FOLDER
    chartData = [0,0,0]
    for seed in range(STARTSEED , ENDSEED + 1):
    
        workingFile = gzip.open(FOLDER+str(seed)+'/'+WORKINGFILE)    
        data = []
        
        for line in workingFile:
            if not line[0] == '#' and not line[0] == '\n':
            
                lineSplit = line.split()
            
                data.append(lineSplit[-2])
    
        point = float(data[-1])
    
        if point == 0.0:
            chartData[0] += 1
        
        elif point == 1.0:
            chartData[2] += 1
        
        else:
            chartData[1] += 1
    
#        print 'Fixed & 0: ' + str(chartData[0]) + '  Indeterminate: ' + str(chartData[1]) + '  Fixed & 1: ' + str(chartData[2])

#        fig = plt.figure()
#        plt.annotate('Folder '+ FOLDER + str(seed) , xy= (32,.95))
#        plt.plot(data)
#        plt.savefig("graphs/h2h_" + FOLDER + str(seed))
    
    print "FINAL RESULTS ", FOLDER
    print 'Fixed & 0: ' + str(chartData[0]) + '  Indeterminate: ' + str(chartData[1]) + '  Fixed & 1: ' + str(chartData[2])
