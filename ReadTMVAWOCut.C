void ReadTMVAWOCut(TString variable,TString id)
{

  //Open file
  TFile *file =TFile::Open("TMVA.root");
  TestTree->Draw(variable,"classID=="+id);
         if(id=="1")
          {
                 TFile *f= new TFile("/home/cakir/Work/Programs/DeepLearning/TMVA-v4.2.0/test/SR0_Test_50PU_ML1/TMVAPloWOCut/"+variable+"_SR0_ForBckg.root","CREATE");
          }
         else if(id=="0")
          {
                  TFile *f= new TFile("/home/cakir/Work/Programs/DeepLearning/TMVA-v4.2.0/test/SR0_Test_50PU_ML1/TMVAPloWOCut/"+variable+"_SR0_ForSignal.root","CREATE");
          }
  //check htemp!!
  TH1F *h = (TH1F*)c1->GetPrimitive("htemp");
  h->Write();
}
