1. To find start/end positions of aligned sequences, compile 1.find_position_bam.cpp into binary with g++. The binary should be linked with bamtools library (https://github.com/pezmaster31/bamtools).

In order to change prefix (type of analysis, namely "WT" or "RGEN"), change string in the header of cpp file. Also input bam file should be pre-sorted.

2. Because the input bam file is already pre-sorted one, the reverse index should only be sorted. Running '2.sort.py' will do this.

3. Running '3.count.py' and '4.cut_threshold.py' to count the number of each positions, and cut them with some threshold values.

4. In order to get coverage information from bam file, run '5.coverage.py' with bam file. It needs 'pysam' python package to run properly. Download and install it via pip or easy_install.

5. Run '6.get_depth.py', '7.ana_depth.py', and '8.analysis.py' will give you final results. Before running the scripts, please set desired creteria inside the files.
