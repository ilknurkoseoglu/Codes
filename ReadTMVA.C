void ReadTMVA(TString variable,TString method,Float_t cut,TString id)
{
  //convert float to string
  TString Scut=" ";
  Scut=Form("%f",cut);

  // get first 4 char of string
  TString FScut=" ";
  TString SB=" ";
  FScut=Scut(0,5);

  //Open file
  TFile *file =TFile::Open("TMVA.root");
  TestTree->Draw(variable,method+"<"+Scut+" && classID=="+id);
 	 if(id=="1")
 	  {
 	         TFile *f= new TFile("/home/cakir/Work/Programs/DeepLearning/TMVA-v4.2.0/test/SR0_Test_50PU_ML1/"+variable+"_"+method+"_"+FScut+"_SR0_50PUForBckg.root","CREATE");
 	  }
 	 else if(id=="0")
 	  {
 	 	  TFile *f= new TFile("/home/cakir/Work/Programs/DeepLearning/TMVA-v4.2.0/test/SR0_Test_50PU_ML1/"+variable+"_"+method+"_"+FScut+"_SR0_50PUForSignal.root","CREATE");
 	  }
  //check htemp!!
  TH1F *h = (TH1F*)c1->GetPrimitive("htemp");
  h->Write();
}
