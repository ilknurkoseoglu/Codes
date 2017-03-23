#!/usr/bin/python

import sys
from ROOT import gROOT
from ROOT import TFile
from ROOT import TKey
def GetKeyNames( self ):
	return [key.GetName() for key in MyFile.GetListOfKeys()]
TFile.GetKeyNames = GetKeyNames

MyFile=TFile("DeepSingle+DelphMET_NoPU_DiBoson_his.root")
keyList = MyFile.GetKeyNames()
print "\nKeys in file:", keyList

        # scenarios and samples
conditions=['TreeSR0','TreeSR1','TreeSR2','TreeSR3','TreeSR','TreeSR5','TreeSR6','TreeSR7','TreeSR8','TreeSR9','TreeSR10','TreeB0','TreeB1','TreeB2','TreeB3']
gROOT.ProcessLine(".L denemeStack.C")
for samp in keyList:
            print "Key :", samp
            if not samp=='TreeSR0' or samp=='TreeB0' or samp=='TreeSR1' or samp=='TreeSR2' or samp=='TreeSR3' or samp=='TreeSR4' or samp=='TreeSR5' or samp=='TreeSR6' or samp=='TreeSR7' or samp=='TreeSR8' or samp=='TreeSR9' or samp=='TreeSR10' or samp=='TreeB1' or samp=='TreeB2' or samp=='TreeB3':
                        from ROOT import denemeStack
                        denemeStack(samp)
            else:
                        break
                        print "THE END"
                       
                        
