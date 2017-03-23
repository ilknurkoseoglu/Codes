#!/usr/bin/python

import sys
from ROOT import gROOT
from ROOT import TFile
from ROOT import TKey


# scenarios and samples
Vb=['HT','MT','MET','METOHT'] #variables
SOB=["1","0"] #signal or background
gROOT.ProcessLine(".L ReadTMVAWOCut.C")
for variable in Vb:
	for sb in SOB:
		from ROOT import ReadTMVAWOCut
              	ReadTMVAWOCut(variable,sb)
