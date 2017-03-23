#!/usr/bin/python

import sys
from ROOT import gROOT
from ROOT import TFile
from ROOT import TKey

keyList=["hNel","hNbjet","hNbjet_2","hNel_2","hNlep","hNlep_2","hNmu","hNmu_2","hNtj","hNtj_2"]
print "\nKeys in file:", keyList

# scenarios and samples
conditions=['TreeSR0','TreeSR1','TreeSR2','TreeSR3','TreeSR','TreeSR5','TreeSR6','TreeSR7','TreeSR8','TreeSR9','TreeSR10','TreeB0','TreeB1','TreeB2','TreeB3']
gROOT.ProcessLine(".L denemeStack2.C")
for samp in keyList:
            print "Key :", samp
            if not samp=='TreeSR0' or samp=='TreeB0' or samp=='TreeSR1' or samp=='TreeSR2' or samp=='TreeSR3' or samp=='TreeSR4' or samp=='TreeSR5' or samp=='TreeSR6' or samp=='TreeSR7' or samp=='TreeSR8' or samp=='TreeSR9' or samp=='TreeSR10' or samp=='TreeB1' or samp=='TreeB2' or samp=='TreeB3':
                        from ROOT import denemeStack2
                        denemeStack2(samp)
            else:
                        break
                        print "THE END"
                       
                        
