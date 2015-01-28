#!/bin/bash
if [ ! -d "bamtools" ]; then
  git clone https://github.com/pezmaster31/bamtools
fi

if [ ! -d "bamtools_build" ]; then
  mkdir bamtools_build
fi

if [ ! -f "bamtools_build/lib/libbamtools.a" ]; then
  cd bamtools_build
  cmake ../bamtools
  make
  cd ..
fi

g++ -O3 1.find_position_bam.cpp -o 1.find_position_bam -Ibamtools/include -Lbamtools/lib -lbamtools -lz
