#!/bin/env python

data={
"ee_Bv1_2016APV" : "v1/DoubleEG_Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
"ee_Bv2_2016APV" : "v1/DoubleEG_Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v3_NANOAOD_v8.root",
"ee_C_2016APV" : "v1/DoubleEG_Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
"ee_D_2016APV" : "v1/DoubleEG_Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
"ee_E_2016APV" : "v1/DoubleEG_Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
"ee_F_2016APV" : "v1/DoubleEG_Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
"ee_F_2016" : "v1/DoubleEG_Run2016F-UL2016_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"ee_G_2016" : "v1/DoubleEG_Run2016G-UL2016_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"ee_H_2016" : "v1/DoubleEG_Run2016H-UL2016_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"em_Bv1_2016APV" : "v1/MuonEG_Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
"em_Bv2_2016APV" : "v1/MuonEG_Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
"em_C_2016APV" : "v1/MuonEG_Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
"em_D_2016APV" : "v1/MuonEG_Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
"em_E_2016APV" : "v1/MuonEG_Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
"em_F_2016APV" : "v1/MuonEG_Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
"em_F_2016" : "v1/MuonEG_Run2016F-UL2016_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"em_G_2016" : "v1/MuonEG_Run2016G-UL2016_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"em_H_2016" : "v1/MuonEG_Run2016H-UL2016_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"mm_Bv1_2016APV" : "v1/DoubleMuon_Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
"mm_Bv2_2016APV" : "v1/DoubleMuon_Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
"mm_C_2016APV" : "v1/DoubleMuon_Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
"mm_D_2016APV" : "v1/DoubleMuon_Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
"mm_E_2016APV" : "v1/DoubleMuon_Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
"mm_F_2016APV" : "v1/DoubleMuon_Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
"mm_F_2016" : "v1/DoubleMuon_Run2016F-UL2016_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"mm_G_2016" : "v1/DoubleMuon_Run2016G-UL2016_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
"mm_H_2016" : "v1/DoubleMuon_Run2016H-UL2016_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"ee_B_2017" : "v1/DoubleEG_Run2017B-UL2017_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"ee_C_2017" : "v1/DoubleEG_Run2017C-UL2017_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"ee_D_2017" : "v1/DoubleEG_Run2017D-UL2017_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"ee_E_2017" : "v1/DoubleEG_Run2017E-UL2017_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"ee_F_2017" : "v1/DoubleEG_Run2017F-UL2017_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"mm_B_2017" : "v1/DoubleMuon_Run2017B-UL2017_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"mm_C_2017" : "v1/DoubleMuon_Run2017C-UL2017_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"mm_D_2017" : "v1/DoubleMuon_Run2017D-UL2017_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"mm_E_2017" : "v1/DoubleMuon_Run2017E-UL2017_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"mm_F_2017" : "v1/DoubleMuon_Run2017F-UL2017_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"em_B_2017" : "v1/MuonEG_Run2017B-UL2017_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"em_C_2017" : "v1/MuonEG_Run2017C-UL2017_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"em_D_2017" : "v1/MuonEG_Run2017D-UL2017_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"em_E_2017" : "v1/MuonEG_Run2017E-UL2017_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"em_F_2017" : "v1/MuonEG_Run2017F-UL2017_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"eg_A_2018" : "v1/EGamma_Run2018A-UL2018_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"eg_B_2018" : "v1/EGamma_Run2018B-UL2018_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"eg_C_2018" : "v1/EGamma_Run2018C-UL2018_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"eg_D_2018" : "v1/EGamma_Run2018D-UL2018_MiniAODv2_NanoAODv9-v3_NANOAOD_v8.root",
"em_A_2018" : "v1/MuonEG_Run2018A-UL2018_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"em_B_2018" : "v1/MuonEG_Run2018B-UL2018_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"em_C_2018" : "v1/MuonEG_Run2018C-UL2018_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"em_D_2018" : "v1/MuonEG_Run2018D-UL2018_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"mm_A_2018" : "v1/DoubleMuon_Run2018A-UL2018_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"mm_B_2018" : "v1/DoubleMuon_Run2018B-UL2018_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"mm_C_2018" : "v1/DoubleMuon_Run2018C-UL2018_MiniAODv2_NanoAODv9-v1_NANOAOD_v8.root",
"mm_D_2018" : "v1/DoubleMuon_Run2018D-UL2018_MiniAODv2_NanoAODv9-v2_NANOAOD_v8.root",
}

mc={
"DYM10_2016APV" : "v1/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"DYM10_2016"    : "v1/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"DYM10_2017"    : "v1/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"DYM10_2018"    : "v1/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"DYM50_2016APV" : "v1/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"DYM50_2016"    : "v1/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"DYM50_2017"    : "v1/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"DYM50_2018"    : "v1/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"GGZZ2e2m_2016APV" : "v1/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
"GGZZ2e2m_2016" : "v1/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"GGZZ2e2m_2017" : "v1/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
"GGZZ2e2m_2018" : "v1/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
"GGZZ2e2t_2016APV" : "v1/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
"GGZZ2e2t_2016" : "v1/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"GGZZ2e2t_2017" : "v1/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
"GGZZ2e2t_2018" : "v1/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
"GGZZ2m2t_2016APV" : "v1/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
"GGZZ2m2t_2016" : "v1/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"GGZZ2m2t_2017" : "v1/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
"GGZZ2m2t_2018" : "v1/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
"GGZZ4e_2016APV" : "v1/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
"GGZZ4e_2016" : "v1/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2_NANOAODSIM_v8.root",
"GGZZ4e_2017" : "v1/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
"GGZZ4e_2018" : "v1/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
"GGZZ4m_2016APV" : "v1/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
"GGZZ4m_2016" : "v1/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2_NANOAODSIM_v8.root",
"GGZZ4m_2017" : "v1/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
"GGZZ4m_2018" : "v1/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
"GGZZ4t_2016APV" : "v1/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
"GGZZ4t_2016" : "v1/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"GGZZ4t_2017" : "v1/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
"GGZZ4t_2018" : "v1/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
"GGZHWW_WW2l_2016APV": "v1/GluGluZH_HToWWTo2L2Nu_M125_13TeV_powheg_pythia8_TuneCP5_PSweights_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
"GGZHWW_WW2l_2016": "v1/GluGluZH_HToWWTo2L2Nu_M125_13TeV_powheg_pythia8_TuneCP5_PSweights_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2_NANOAODSIM_v8.root",
"GGZHWW_WW2l_2017" : "v1/GluGluZH_HToWWTo2L2Nu_M125_13TeV_powheg_pythia8_TuneCP5_PSweights_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
"GGZHWW_WW2l_2018" : "v1/GluGluZH_HToWWTo2L2Nu_M125_13TeV_powheg_pythia8_TuneCP5_PSweights_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
"ZHWW_4l_2016APV" : "v1/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
"ZHWW_4l_2016" : "v1/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2_NANOAODSIM_v8.root",
"ZHWW_4l_2017" : "v1/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
"ZHWW_4l_2018" : "v1/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
"SSWW_2016APV" : "v1/SSWW_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"SSWW_2016" : "v1/SSWW_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"SSWW_2017" : "v1/SSWW_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"SSWW_2018" : "v1/SSWW_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"ST_schan_lep_2016APV" : "v1/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"ST_schan_lep_2016" : "v1/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"ST_schan_lep_2017" : "v1/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"ST_schan_lep_2018" : "v1/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"ST_antitop_tchan_2016APV" : "v1/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"ST_antitop_tchan_2016" : "v1/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"ST_antitop_tchan_2017" : "v1/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"ST_antitop_tchan_2018" : "v1/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"ST_top_tchan_2016APV" : "v1/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"ST_top_tchan_2016" : "v1/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"ST_top_tchan_2017" : "v1/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"ST_top_tchan_2018" : "v1/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"ST_antitop_nohad_tW_2016APV" : "v1/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"ST_antitop_nohad_tW_2016" : "v1/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"ST_antitop_nohad_tW_2017" : "v1/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"ST_antitop_nohad_tW_2018" : "v1/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"ST_top_nohad_tW_2016APV" : "v1/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"ST_top_nohad_tW_2016" : "v1/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"ST_top_nohad_tW_2017" : "v1/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"ST_top_nohad_tW_2018" : "v1/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"TT2l_2016APV" : "v1/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"TT2l_2016" : "v1/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"TT2l_2017" : "v1/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"TT2l_2018" : "v1/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"TThad_2016APV" : "v1/TTToHadronic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"TThad_2016" : "v1/TTToHadronic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"TThad_2017" : "v1/TTToHadronic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"TThad_2018" : "v1/TTToHadronic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"TT1l_2016APV" : "v1/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"TT1l_2016" : "v1/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"TT1l_2017" : "v1/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"TT1l_2018" : "v1/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"TTWlv_2016APV" : "v1/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
"TTWlv_2016" : "v1/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"TTWlv_2017" : "v1/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"TTWlv_2018" : "v1/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"TTWqq_2016APV" : "v1/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
"TTWqq_2016" : "v1/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"TTWqq_2017" : "v1/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"TTWqq_2018" : "v1/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"TTZll_M10_2016APV" : "v1/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"TTZll_M10_2016" : "v1/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"TTZll_M10_2017" : "v1/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"TTZll_M10_2018" : "v1/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"TTZll_M1_2016APV": "v1/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"TTZll_M1_2016": "v1/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"TTZll_M1_2017": "v1/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"TTZll_M1_2018" : "v1/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"TTZqq_2016APV" : "v1/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"TTZqq_2016" : "v1/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"TTZqq_2017" : "v1/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"TTZqq_2018" : "v1/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"Wlv_2016APV" : "v1/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
"Wlv_2016" : "v1/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"Wlv_2017" : "v1/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"Wlv_2018" : "v1/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
#
#
#
# "WWlvqq_2018" : "v1/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"WWlvlv_2016APV" : "v1/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"WWlvlv_2016" : "v1/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"WWlvlv_2017" : "v1/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
"WWlvlv_2018" : "v1/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
#
#
#
# "WW4q_2018" : "v1/WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
"WWW_2l_2016APV" : "v1/WWW_4F_DiLeptonFilter_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
"WWW_2l_2016" : "v1/WWW_4F_DiLeptonFilter_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"WWW_2l_2017" : "v1/WWW_4F_DiLeptonFilter_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"WWW_2l_2018" : "v1/WWW_4F_DiLeptonFilter_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
# "WWW_2016APV" : "v1/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
# "WWW_2016" : "v1/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
# "WWW_2017" : "v1/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
# "WWW_2018" : "v1/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
# "WWW_ext_2016APV" : "v1/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1_NANOAODSIM_v8.root",
# "WWW_ext_2016" : "v1/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v1_NANOAODSIM_v8.root",
# "WWW_ext_2017" : "v1/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2_NANOAODSIM_v8.root",
# "WWW_ext_2018" : "v1/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2_NANOAODSIM_v8.root",
# Does not seem to have been produced for APV why?
"WWZ_4l_2016" : "v1/WWZJetsTo4L2Nu_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2_NANOAODSIM_v8.root",
"WWZ_4l_2017" : "v1/WWZJetsTo4L2Nu_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
"WWZ_4l_2018" : "v1/WWZJetsTo4L2Nu_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
"WWZ_2016APV" : "v1/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
# "WWZ_2016" : "v1/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
# "WWZ_2017" : "v1/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
# "WWZ_2018" : "v1/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
# "WWZ_ext_2016APV" : "v1/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1_NANOAODSIM_v8.root",
# "WWZ_ext_2016" : "v1/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v1_NANOAODSIM_v8.root",
# "WWZ_ext_2017" : "v1/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2_NANOAODSIM_v8.root",
# "WWZ_ext_2018" : "v1/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2_NANOAODSIM_v8.root",
# "WW_2016APV" : "v1/WW_TuneCP5_13TeV-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
# "WW_2016" : "v1/WW_TuneCP5_13TeV-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
# "WW_2017" : "v1/WW_TuneCP5_13TeV-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
# "WW_2018" : "v1/WW_TuneCP5_13TeV-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
#
#
#
# "WZ1l2q_2018" : "v1/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
#
#
#
# "WZ1l3v_2018" : "v1/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"WZ2q2l_2016APV" : "v1/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
"WZ2q2l_2016" : "v1/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2_NANOAODSIM_v8.root",
"WZ2q2l_2017" : "v1/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
"WZ2q2l_2018" : "v1/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"WZ3l1v_2016APV" : "v1/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"WZ3l1v_2016" : "v1/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"WZ3l1v_2017" : "v1/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
"WZ3l1v_2018" : "v1/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
"WZZ_2016APV" : "v1/WZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"WZZ_2016" : "v1/WZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"WZZ_2017" : "v1/WZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"WZZ_2018" : "v1/WZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
# "WZZ_ext_2016APV" : "v1/WZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1_NANOAODSIM_v8.root",
# "WZZ_ext_2016" : "v1/WZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v1_NANOAODSIM_v8.root",
# "WZZ_ext_2017" : "v1/WZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2_NANOAODSIM_v8.root",
# "WZZ_ext_2018" : "v1/WZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2_NANOAODSIM_v8.root",
# "WZ_2016APV" : "v1/WZ_TuneCP5_13TeV-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
# "WZ_2016" : "v1/WZ_TuneCP5_13TeV-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
# "WZ_2017" : "v1/WZ_TuneCP5_13TeV-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
# "WZ_2018" : "v1/WZ_TuneCP5_13TeV-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"ZZ2l2v_2016APV" : "v1/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"ZZ2l2v_2016" : "v1/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"ZZ2l2v_2017" : "v1/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"ZZ2l2v_2018" : "v1/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"ZZ2l2q_2016APV" : "v1/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"ZZ2l2q_2016" : "v1/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"ZZ2l2q_2017" : "v1/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"ZZ2l2q_2018" : "v1/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
#
#
#
#"ZZ2q2v_2018" : "v1/ZZTo2Q2Nu_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"ZZ4l_2016APV" : "v1/ZZTo4L_TuneCP5_13TeV_powheg_pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"ZZ4l_2016" : "v1/ZZTo4L_TuneCP5_13TeV_powheg_pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"ZZ4l_2017" : "v1/ZZTo4L_TuneCP5_13TeV_powheg_pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
"ZZ4l_2018" : "v1/ZZTo4L_TuneCP5_13TeV_powheg_pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
#
#
#
#"ZZ4q_2018" : "v1/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"ZZZ_2016APV" : "v1/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"ZZZ_2016" : "v1/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"ZZZ_2017" : "v1/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"ZZZ_2018" : "v1/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
# "ZZZ_ext_2016APV" : "v1/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1_NANOAODSIM_v8.root",
# "ZZZ_ext_2016" : "v1/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v1_NANOAODSIM_v8.root",
# "ZZZ_ext_2017" : "v1/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2_NANOAODSIM_v8.root",
# "ZZZ_ext_2018" : "v1/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2_NANOAODSIM_v8.root",
# "ZZ_2016APV" : "v1/ZZ_TuneCP5_13TeV-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
# "ZZ_2016" : "v1/ZZ_TuneCP5_13TeV-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
# "ZZ_2017" : "v1/ZZ_TuneCP5_13TeV-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
# "ZZ_2018" : "v1/ZZ_TuneCP5_13TeV-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"tZq_2016APV" : "v1/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"tZq_2016" : "v1/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"tZq_2017" : "v1/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"tZq_2018" : "v1/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"ttHNonbb_2016APV" : "v1/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"ttHNonbb_2016" : "v1/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"ttHNonbb_2017" : "v1/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"ttHNonbb_2018" : "v1/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"ttHbb_2016APV" : "v1/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
"ttHbb_2016" : "v1/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
"ttHbb_2017" : "v1/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
"ttHbb_2018" : "v1/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
"VHToNonbb_2016APV" : "v1/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
"VHToNonbb_2016" : "v1/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2_NANOAODSIM_v8.root",
"VHToNonbb_2017" : "v1/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
"VHToNonbb_2018" : "v1/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
"WWZ_EFT_2018" : "v1/WWZ_RunIISummer20UL18NanoAODv9_FourleptonFilter_FilterFix_merged.root",
"WZZ_EFT_2018" : "v1/WZZ_RunIISummer20UL18NanoAODv9_FourleptonFilter_FilterFix_merged.root",
"ZZZ_EFT_2018" : "v1/ZZZ_RunIISummer20UL18NanoAODv9_FourleptonFilter_FilterFix_merged.root",
}

process={
"DYM10"               : "Other",
"DYM50"               : "Other",
"GGZZ2e2m"            : "ZZ",
"GGZZ2e2t"            : "ZZ",
"GGZZ2m2t"            : "ZZ",
"GGZZ4e"              : "ZZ",
"GGZZ4m"              : "ZZ",
"GGZZ4t"              : "ZZ",
"GGZHWW_WW2l"         : "WWZ",
"ZHWW_4l"             : "WWZ",
"SSWW"                : "Other",
"ST_schan_lep"        : "Other",
"ST_antitop_tchan"    : "Other",
"ST_top_tchan"        : "Other",
"ST_antitop_nohad_tW" : "Other",
"ST_top_nohad_tW"     : "Other",
"TT2l"                : "Other",
"TThad"               : "Other",
"TT1l"                : "Other",
"TTWlv"               : "Other",
"TTWqq"               : "Other",
"TTZll_M10"           : "TTZ",
"TTZll_M1"            : "TTZ",
"TTZqq"               : "TTZ",
"Wlv"                 : "Other",
"WWlvlv"              : "Other",
"WWW_2l"              : "WWW",
"WWZ_4l"              : "WWZ",
"WWZ"                 : "WWZ",
"WZ2q2l"              : "WZ",
"WZ3l1v"              : "WZ",
"WZZ"                 : "WZZ",
"ZZ2l2v"              : "ZZ",
"ZZ2l2q"              : "ZZ",
"ZZ4l"                : "ZZ",
"ZZZ"                 : "ZZZ",
"tZq"                 : "Other",
"ttHNonbb"            : "Higgs",
"ttHbb"               : "Higgs",
"VHToNonbb"           : "Higgs",
}

years=["2016APV", "2016", "2017", "2018"]

files_all={
        "WWW":[],
        "WWZ":[],
        "WZZ":[],
        "ZZZ":[],
        "Higgs":[],
        "ZZ":[],
        "TTZ":[],
        "WZ":[],
        "Other":[],
}

files_2016APV={
        "WWW":[],
        "WWZ":[],
        "WZZ":[],
        "ZZZ":[],
        "Higgs":[],
        "ZZ":[],
        "TTZ":[],
        "WZ":[],
        "Other":[],
}

files_2016={
        "WWW":[],
        "WWZ":[],
        "WZZ":[],
        "ZZZ":[],
        "Higgs":[],
        "ZZ":[],
        "TTZ":[],
        "WZ":[],
        "Other":[],
}

files_2017={
        "WWW":[],
        "WWZ":[],
        "WZZ":[],
        "ZZZ":[],
        "Higgs":[],
        "ZZ":[],
        "TTZ":[],
        "WZ":[],
        "Other":[],
}

files_2018={
        "WWW":[],
        "WWZ":[],
        "WZZ":[],
        "ZZZ":[],
        "Higgs":[],
        "ZZ":[],
        "TTZ":[],
        "WZ":[],
        "Other":[],
}

for proc in process.keys():
    for year in years:
        key = proc+"_"+year
        if "WWZ_4l_2016APV" == key: continue
        if "WWZ_2016" == key: continue
        if "WWZ_2017" == key: continue
        if "WWZ_2018" == key: continue
        files_all[process[proc]].append(mc[key])
        if year == "2016APV": files_2016APV[process[proc]].append(mc[key])
        if year == "2016": files_2016[process[proc]].append(mc[key])
        if year == "2017": files_2017[process[proc]].append(mc[key])
        if year == "2018": files_2018[process[proc]].append(mc[key])

# for key in files_all:
#     print(key)
#     for f in files_all[key]:
#         print(f)

# for key in files_2018:
#     inputs = ",".join(files_2018[key])
#     print("rm -f {}.root; ./doAnalysis -i {} -t t -o {}.root".format(key, inputs, key))

for key in files_all:
    inputs = ",".join(files_all[key])
    print("rm -f outputs/{}.root; mkdir -p outputs; ./doAnalysis -i {} -t t -o outputs/{}.root > outputs/{}.log 2>&1".format(key, inputs, key, key))

print("rm -f outputs/data.root; mkdir -p outputs; ./doAnalysis -i \\\"v1/*Run201*.root\\\" -t t -o outputs/data.root > outputs/data.log 2>&1")

# VVV all combined
inputs = ",".join(files_all["WWW"] + files_all["WWZ"] + files_all["WZZ"] + files_all["ZZZ"])
print("rm -f outputs/VVV.root; mkdir -p outputs; ./doAnalysis -i {} -t t -o outputs/VVV.root > outputs/VVV.log 2>&1".format(inputs))

# Special handling of some extra backgrounds
rewgt_suffixs = {
133:"m3p0",
134:"m1p5",
135:"m1p0",
136:"m0p8",
137:"m0p4",
138:"m0p2",
139:"0p2",
140:"0p4",
141:"0p8",
142:"1p0",
143:"1p5",
144:"3p0",
}
for rewgt_idx in rewgt_suffixs.keys():
    inputs = mc["WWZ_EFT_2018"]
    fname = "WWZ_EFT_FT0_{}".format(rewgt_suffixs[rewgt_idx])
    print("rm -f outputs/{}.root; mkdir -p outputs; ./doAnalysis -i {} -e {} -t t -o outputs/{}.root > outputs/{}.log 2>&1".format(fname, inputs, rewgt_idx, fname, fname))
for rewgt_idx in rewgt_suffixs.keys():
    inputs = mc["WWZ_EFT_2018"]
    fname = "WWZ_EFT_FT0_{}".format(rewgt_suffixs[rewgt_idx])
    print("rm -f outputs/{}.root; mkdir -p outputs; ./doAnalysis -i {} -e {} -t t -o outputs/{}.root > outputs/{}.log 2>&1".format(fname, inputs, rewgt_idx, fname, fname))

    inputs = mc["WZZ_EFT_2018"]
    inputs = mc["ZZZ_EFT_2018"]









##-------------------------------============================-------------------------------------
##-------------------------------============================-------------------------------------
##-------------------------------============================-------------------------------------


# "" : "v1/TTZZ_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
# "" : "v1/TTZZ_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
# "" : "v1/TTZZ_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
# "" : "v1/TTZZ_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
# "" : "v1/TTHH_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
# "" : "v1/TTHH_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2_NANOAODSIM_v8.root",
# "" : "v1/TTHH_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
# "" : "v1/TTHH_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
# "" : "v1/TTTJ_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
# "" : "v1/TTTJ_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2_NANOAODSIM_v8.root",
# "" : "v1/TTTJ_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
# "" : "v1/TTTJ_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
# "" : "v1/TTTT_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
# "" : "v1/TTTT_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2_NANOAODSIM_v8.root",
# "" : "v1/TTTT_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
# "" : "v1/TTTT_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
# "" : "v1/TTTW_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
# "" : "v1/TTTW_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
# "" : "v1/TTTW_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
# "" : "v1/TTWH_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
# "" : "v1/TTWH_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2_NANOAODSIM_v8.root",
# "" : "v1/TTWH_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
# "" : "v1/TTWH_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",
# "" : "v1/TTWW_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
# "" : "v1/TTWW_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
# "" : "v1/TTWW_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
# "" : "v1/TTWW_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
# "" : "v1/TTWZ_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1_NANOAODSIM_v8.root",
# "" : "v1/TTWZ_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1_NANOAODSIM_v8.root",
# "" : "v1/TTWZ_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1_NANOAODSIM_v8.root",
# "" : "v1/TTWZ_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1_NANOAODSIM_v8.root",
# "" : "v1/TTZH_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2_NANOAODSIM_v8.root",
# "" : "v1/TTZH_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2_NANOAODSIM_v8.root",
# "" : "v1/TTZH_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2_NANOAODSIM_v8.root",
# "" : "v1/TTZH_TuneCP5_13TeV-madgraph-pythia8_RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2_NANOAODSIM_v8.root",

