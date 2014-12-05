# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3Bis --eventcontent RAWSIM -s DIGI,L1,DIGI2RAW --datatier GEN-SIM-RAW --filein file:SingleElectronPt35_GENSIM.root -n 10 --conditions START72_V1::All --pileup AVE_20_BX_25ns --pileup_input file:MinBias_13TeV_GENSIM.root --customise_commands=process.ecal_sim_parameter_map.binOfMaximum=7 --geometry Extended2015 --magField 38T_PostLS1 --eventcontent RAWSIM --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('reDIGI2RAW')
from SimCalorimetry.EcalSimProducers.ecalSimParameterMap_cff import *
ecal_sim_parameter_map.binOfMaximum = cms.int32(7)




# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

sr_tag = 'EcalSRSettings_beam2015_option1_v00_mc'
if sr_tag != '' :
    process.GlobalTag.toGet = cms.VPSet(
        cms.PSet(record = cms.string("EcalSRSettingsRcd"),
                 tag = cms.string(sr_tag),
                 #             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_34X_ECAL")  
                 #              connect = cms.untracked.string("frontier://FrontierPrep/CMS_COND_ECAL") 
                 connect = cms.untracked.string('sqlite_file:/afs/cern.ch/work/a/amartell/Simulation/CMSSW_7_2_0_pre4/src/SimCalorimetry/EcalSimProducers/test/python_standard/' + sr_tag + '.db')
                 )
        )


#process.MessageLogger = cms.Service("MessageLogger",
#                                    destinations = cms.untracked.vstring('detailedInfo')
#                                    )


# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring(
#        'file:SingleElectronPt35_GENSIM.root'
        LISTOFFILES
        )
#    fileNames = cms.untracked.vstring('/store/group/comm_ecal/localreco/cmssw_720p4_zeromaterial//photongun_nopu_0.root')
#    fileNames = cms.untracked.vstring('photongun_pu25_ave40file:SingleElectronPt35_GENSIM.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('step3Bis nevts:10'),
    name = cms.untracked.string('Applications')
)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'START72_V1::All', '')

# Other statements  
process.mix.input.nbPileupEvents.averageNumber = cms.double(40.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-13)
process.mix.maxBunch = cms.int32(2)
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_7_2_0_pre4/RelValMinBias_13/GEN-SIM/POSTLS172_V3-v2/00000/006314AA-CE24-E411-833E-02163E00EB33.root','/store/relval/CMSSW_7_2_0_pre4/RelValMinBias_13/GEN-SIM/POSTLS172_V3-v2/00000/1E01717F-CC24-E411-A721-0025B3244016.root','/store/relval/CMSSW_7_2_0_pre4/RelValMinBias_13/GEN-SIM/POSTLS172_V3-v2/00000/38FC8926-CA24-E411-8255-02163E00E972.root','/store/relval/CMSSW_7_2_0_pre4/RelValMinBias_13/GEN-SIM/POSTLS172_V3-v2/00000/4EA16A99-CF24-E411-83B1-02163E00F31B.root','/store/relval/CMSSW_7_2_0_pre4/RelValMinBias_13/GEN-SIM/POSTLS172_V3-v2/00000/50FB1A02-FB24-E411-8190-02163E00E91A.root','/store/relval/CMSSW_7_2_0_pre4/RelValMinBias_13/GEN-SIM/POSTLS172_V3-v2/00000/8C3A6B7A-D024-E411-AE1F-02163E00E62A.root','/store/relval/CMSSW_7_2_0_pre4/RelValMinBias_13/GEN-SIM/POSTLS172_V3-v2/00000/9A41925E-D324-E411-985A-02163E00E862.root','/store/relval/CMSSW_7_2_0_pre4/RelValMinBias_13/GEN-SIM/POSTLS172_V3-v2/00000/F0A92209-CB24-E411-9E53-02163E00FDC2.root'])


# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
#    fileName = cms.untracked.string('step3Bis_DIGI_L1_DIGI2RAW_PU.root'),
    fileName = cms.untracked.string('OUTPUTFILENAME.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-RAW')
    )
)

# Additional output definition


# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.endjob_step,process.RAWSIMoutput_step)


# Customisation from command line
process.ecal_sim_parameter_map.binOfMaximum=7

# Customisation from command line
process.ecal_sim_parameter_map.binOfMaximum=7


process.RAWSIMoutput.outputCommands.append('keep *_rawDataCollector_*_*')
process.RAWSIMoutput.outputCommands.append('keep *_simEcalUnsuppressedDigis_*_*')
process.RAWSIMoutput.outputCommands.append('keep *_*_ebDigis_*')
process.RAWSIMoutput.outputCommands.append('keep *_*_eeDigis_*')
process.RAWSIMoutput.outputCommands.append('keep *_*_EcalRecHitsEB_*')
process.RAWSIMoutput.outputCommands.append('keep *_*_EcalRecHitsEE_*')
process.RAWSIMoutput.outputCommands.append('keep *_*_EcalRecHitsES_*')
process.RAWSIMoutput.outputCommands.append('keep *_simEcalPreshowerDigis_*_*')
process.RAWSIMoutput.outputCommands.append('keep *_ecalPreshowerDigis_*_*')
process.RAWSIMoutput.outputCommands.append('keep PileupSummaryInfos_*_*_*')

