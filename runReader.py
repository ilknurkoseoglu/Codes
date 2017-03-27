#!/usr/bin/env python

import sys
from ROOT import gROOT

# scenarios and samples
scenarios = ['NoPU','50PU','140PU']
samples   = ['DiBoson','BosonJets','TopJets','TTbar','ML1','ML2','ML3','ML4']
# by historic reason we have as dir names: bjets  diboson  tdr tdrNew tjets  ttbar for snowmass
# by historic reason we have as dir names: bjets  diboson  tdr tdr tjets  ttbar for snowmass2

#samples w.o weight
noWeight  = [ ]

# nTuple input path
base =  '/Volumes/cakir_hdd/snowmass2/'
base2 = '/Volumes/cakir_hdd/snowmass2/'
base3 = '/Volumes/cakir_hdd/snowmass2/'
base4 = '/Volumes/cakir_hdd/snowmass2/'
# Lumi in fb^-1
Lumi=300# changed for 140PU to 3000 it's 206 for signal /media/cakir/cakir_hdd/snowmass2/NoPU/tdr/4/ 


def help():
	print 'First argument analysis:'
	print '   DeepSingle'
	print ' then a list of inputs - read the code'
	sys.exit(0)

from operator import mul
def scale(fac,list):
	return map(mul,len(list)*[fac],list)
 
# choose the analysis and a sample
if len(sys.argv)>1:
	if sys.argv[1]=='DeepSingle':       # single lepton  stop - CMS
   		gROOT.LoadMacro('NTupleAnalyzerilknur.C+') 
		from ROOT import NTupleAnalyzerilknur as reader
        elif sys.argv[1]=='Superpol':  # inclusive hadronic
                gROOT.LoadMacro('readerSuperpol.C+') # used to be ?????
                from ROOT import readerSuperpol as reader
        else: 
		help()
else: 
	help()


#prepare empty dictionaries
do={}
for scene in scenarios:
	do[scene]={}
	for samp in samples:
		do[scene][samp] = 0
# read input line and set flags what to process
flag=False
for e in sys.argv:
	for scene in scenarios:
		for samp in samples:
			if e==scene+'_'+samp: 
 				do[scene][samp] = 1
 				if scene=='140PU': Lumi=Lumi  # Lumi factor in case necessity
				flag=True
if not flag: help()


# prepare empty dictionaries
dirsHT={}
inDir={}
weights={}
for scene in scenarios:
	inDir[scene]={}
#	weight[scene]={}
#for Lumi in Lumi:
#--------------------------------------------- sample properties for processing <<<<<<<<<<<<<<<<<<<<<<<<<<<
#
#------------------------------------------------ diboson
# HT dirs 
dirsHT['DiBoson']  = ['0-300/','300-700/','700-1300/','1300-2100/','2100-100000/']
#    xsec
weights['DiBoson'] = [249.97, 35.23, 4.137, 0.417, 0.0477]
#    multiply all by Lumi
weights['DiBoson'] = scale(Lumi,weights['DiBoson'])
#s
# NoPU
inDir['NoPU']['DiBoson']  = base+'/NoPU/diboson/'
# 50PU
inDir['50PU']['DiBoson']  = base+'/50PU/diboson/'
# 140PU
inDir['140PU']['DiBoson'] = base+'/140PU/diboson/'
#
#------------------------------------------------ boson+jets
# HT dirs 
dirsHT['BosonJets']  = ['0-300/','300-600/','600-1100/','1100-1800/','1800-2700/','2700-3700/','3700-100000/']
#    xsec
weights['BosonJets'] = [34409.92339,2642.85309,294.12311,25.95000,2.42111,0.22690,0.02767]
#    multiply all by Lumi
weights['BosonJets'] = scale(Lumi,weights['BosonJets'])
#
# NoPU
inDir['NoPU']['BosonJets']  = base+'/NoPU/bjets/'
# 50PU
inDir['50PU']['BosonJets']  = base+'/50PU/bjets/'
# 140PU
inDir['140PU']['BosonJets'] = base+'/140PU/bjets/'
#
#---------------------------------------------- ttbar
# HT dirs 
dirsHT['TTbar']  = ['0-600/','600-1100/','1100-1700/','1700-2500/','2500-100000/']
#    xsec
weights['TTbar'] = [530.89358,42.55351,4.48209,0.52795,0.05449]
#    multiply all by Lumi
weights['TTbar'] = scale(Lumi,weights['TTbar'])
#
# NoPU
inDir['NoPU']['TTbar']  = base+'/NoPU/ttbar/'
# 50PU
inDir['50PU']['TTbar']  = base+'/50PU/ttbar/'
# 140PU
inDir['140PU']['TTbar'] = base+'/140PU/ttbar/'
#
#--------------------------------------------- tjets
# HT dirs 
dirsHT['TopJets']  = ['0-500/','500-1000/','1000-1600/','1600-2400/','2400-100000/']
#    xsec
weights['TopJets'] = [109.73602,5.99325,0.37680,0.03462,0.00312]
#    multiply all by Lumi
weights['TopJets'] = scale(Lumi,weights['TopJets'])
#
# NoPU
inDir['NoPU']['TopJets']  = base+'/NoPU/tjets/'
# 50PU
inDir['50PU']['TopJets']  = base+'/50PU/tjets/'
# 140PU
inDir['140PU']['TopJets'] = base+'/140PU/tjets/'
#---------------------------------------------STCs
#--------------------- ML1
dirsHT['ML1']  = ['/']
dirsHT['ML2']  = ['/']
dirsHT['ML3']  = ['/']
dirsHT['ML4']  = ['/']
	
#Luminosity fb^-1 den pb^-1 e cevirirsek *1000 faktoru geliyor oyle yapmazsak scale ve 1000 olmadan ayni grafik elde ediliyor
#(xsec1*Lumi)/EventSayi1=weight
"""weights['ML1'] = [(6.92*Lumi)/999999]
weights['ML2'] = [(1.14*Lumi)/999839]
weights['ML3'] = [(1.82*Lumi)/979995]
weights['ML4'] = [(0.61*Lumi)/1940000]
"""
bit=''
if base2=='/nfs/dust/cms/user/cakir/ECFA_SETUP/SAMPLES_191114/STC8_Delphes_Ntuple/':bit='New' 
# NoPU
inDir['NoPU']['ML1'] = base+'NoPU/ML/ML1/'
inDir['NoPU']['ML2'] = base+'NoPU/ML/ML2/'
inDir['NoPU']['ML3'] = base+'NoPU/ML/ML3/'
inDir['NoPU']['ML4'] = base+'NoPU/ML/ML4/'

# 50PU
#weights['ML1'] = [(1.19*Lumi)/1000000]
#weights['ML2'] = [(1.19*Lumi)/899853]
inDir['50PU']['ML1'] = base+'50PU/ML/ML1/'
inDir['50PU']['ML2'] = base+'50PU/ML/ML2/'

#inDir['50PU']['TDR8'] = base2+'/50PU/'
#inDir['50PU']['TDR10'] = base3+'/50PU/'
#inDir['50PU']['SP1'] = base4+'/50PU/'
# 140PU
weights['ML2'] = [(1.19*Lumi)/879858]
inDir['140PU']['ML2'] = base+'140PU/ML/ML2/'
#inDir['140PU']['TDR5'] = base+'/140PU/tdr'+bit+'/5/'
#inDir['140PU']['TDR6'] = base+'/140PU/tdr'+bit+'/6/'
#inDir['140PU']['TDR8'] = base2+'/140PU/'
#--------------------------------------------- end of sample properties

# 
from ROOT import TFile
from glob import glob
from sys import exit
def GetEntries(dirname):
	files = glob(dirname+'/*.root')
	if len(files)>1:
		print 'GetEntries: there is more than 1 root file in '+dirname
		exit(0)
	print dirname,files
	file=TFile(files[0])
	tree = file.Get("delphTree")
	return tree.GetEntries()
		
# do it
for scene in scenarios:
	for samp in samples:
		if do[scene][samp]: 
			f=''
			for i in range(len(dirsHT[samp])):
				entries = GetEntries(inDir[scene][samp]+dirsHT[samp][i])
				f=f+inDir[scene][samp]+dirsHT[samp][i]+' '+str(weights[samp][i]/entries)+' '
			print f,samp,scene
			if samp in noWeight:
				reader(f,scene+'_'+samp,False)
			else:   
				reader(f,scene+'_'+samp)





