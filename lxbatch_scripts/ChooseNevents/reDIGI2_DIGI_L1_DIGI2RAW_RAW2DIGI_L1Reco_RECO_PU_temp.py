# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: reDIGI2 --eventcontent RECOSIM -s DIGI,L1,DIGI2RAW,RAW2DIGI,L1Reco,RECO --filein inFile.root --datatier GEN-SIM-RECO --conditions POSTLS172_V1::All --pileup AVE_20_BX_25ns --pileup_input file:pippo.root --geometry Extended2015 --magField 38T_PostLS1 -n 10 --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

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
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(45)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    firstEvent = cms.untracked.uint32(FIRSTEVENT),
    fileNames = cms.untracked.vstring(
#        LISTOFFILES
#        '/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/E83F4585-527A-E411-BF52-0025905A60EE.root'

'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/0C521985-527A-E411-90DB-003048FFD76E.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/0EA3FE83-527A-E411-8112-003048FFCBB0.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/10975F82-527A-E411-89F5-002590596468.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/1A15EF83-527A-E411-9D9D-003048FFD770.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/2014B5D6-527A-E411-9F03-0025905964BC.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/241AEAD8-527A-E411-9E08-003048FFD75C.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/28C0B189-537A-E411-834F-003048FFD730.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/2AAB2589-527A-E411-8E55-00259059649C.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/2C588B88-527A-E411-A463-003048FFD7A2.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/326F5588-527A-E411-AF55-003048FFCC2C.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/32A985D7-527A-E411-8916-0025905A60DA.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/3685A7DA-527A-E411-81DB-0025905938B4.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/4063030B-527A-E411-BFBF-00259059649C.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/40E0A284-527A-E411-AF09-003048FFD79C.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/4E5CCC8A-527A-E411-9F10-0025905A606A.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/50A5D883-527A-E411-AA9C-0025905A60C6.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/5C13D71F-527A-E411-8E0F-003048FFCC1E.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/60331A09-527A-E411-97AD-002618FDA287.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/66508B87-537A-E411-8EA3-0025905A607A.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/68BCD786-537A-E411-A787-0025905964A2.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/6EEA2686-537A-E411-B7AF-003048FFD76E.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/8006420C-527A-E411-B764-003048FFD744.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/8018EF88-527A-E411-A9BD-003048FFCB9E.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/808C7BDD-527A-E411-A4B0-002590596484.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/822552DA-527A-E411-914F-0025905938B4.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/8A26C284-527A-E411-933A-0025905964BA.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/8E295ABE-567A-E411-9B36-0025905938AA.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/928D8985-527A-E411-AC32-003048FFCB96.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/9C51B388-527A-E411-A841-003048FFCB8C.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/9CF19384-537A-E411-9936-003048FFD7D4.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/9EA51FDA-527A-E411-98DE-0025905938B4.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/A2CA5BD4-527A-E411-9FCB-0025905A6118.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/A4B0F2C4-567A-E411-9B84-0025905964C4.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/A4FDDAD9-527A-E411-A958-0025905938B4.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/A8777CDD-527A-E411-8D6A-0025905938A4.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/AEACA6D7-527A-E411-84CF-0025905A60B4.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/B87C760B-527A-E411-8B52-003048FFD760.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/BAF54AD4-527A-E411-BF1F-0025905A6118.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/BCA819EC-527A-E411-A6AF-0025905964A6.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/C0C2B987-537A-E411-8044-003048FFD740.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/C41D6DDA-527A-E411-9A6A-0025905964B2.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/D2689414-527A-E411-A204-003048FFCC18.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/DCB5F687-527A-E411-BE53-003048FFD728.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/E83F4585-527A-E411-BF52-0025905A60EE.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/EED9440E-527A-E411-991F-003048FFD7C2.root',
'/store/relval/CMSSW_7_4_0_pre1/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_MCRUN2_73_V5-v1/00000/FABB1AD6-527A-E411-A34D-002590593902.root'
        )
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('reDIGI2 nevts:10'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RECOSIMEventContent.outputCommands,
#    fileName = cms.untracked.string('reDIGI2_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_RECO_PU.root'),
   fileName = cms.untracked.string('OUTPUTFILENAME'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-RECO')
    )
)

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(20.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/1042C35F-4D7A-E411-AE8E-0025905A60A8.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/16FC1C5F-4D7A-E411-A692-003048FFD7BE.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/1E2081D6-597A-E411-9D86-0025905A6060.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/261FC65F-4D7A-E411-8285-0025905A48BA.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/30711069-4D7A-E411-BA3B-0025905A60D0.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/429BCE5F-4D7A-E411-A8B1-0025905A48BA.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/4433D15E-4D7A-E411-9C08-0025905A606A.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/4A354664-4D7A-E411-965F-0025905A60B6.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/542054D5-5B7A-E411-9ED2-003048FFD736.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/5CA2CB5F-4D7A-E411-BA61-0025905A48BA.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/68BA1169-4D7A-E411-AE31-0025905A60D0.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/6C7C0F69-4D7A-E411-9E0F-0025905A60D0.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/728B016F-547A-E411-9A5D-0025905A6118.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/7663CB61-4D7A-E411-AD9F-0025905A6090.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/844E4D7F-557A-E411-9891-002590593902.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/906FA962-4D7A-E411-B405-0025905A60E4.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/A499F2E2-597A-E411-A0B1-0025905938A4.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/AE509F5E-4D7A-E411-8F09-0025905A606A.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/B26CD55D-4D7A-E411-9276-003048FF9AA6.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/BA317361-4D7A-E411-B493-0025905A6090.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/C449BB6A-4D7A-E411-A70B-003048FFCBB0.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/CC575B64-4D7A-E411-87E7-0025905A60B6.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/CC909C5D-4D7A-E411-8A2D-0025905A606A.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/CC9AC561-4D7A-E411-A75E-0025905A6090.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/CEDB5363-4D7A-E411-915B-003048FFD7BE.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/E065955D-4D7A-E411-8E72-0025905A606A.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/E8DFF55C-4D7A-E411-A164-0025905A60D2.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/EC019E79-537A-E411-87A1-0025905A6068.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/EEF6384F-5A7A-E411-8124-003048FFCBA8.root','/store/relval/CMSSW_7_4_0_pre1/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V5-v1/00000/F8E73C5D-4D7A-E411-A5B9-0025905A60D2.root'])

#from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'POSTLS172_V1::All', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_73_V5::All', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.RECOSIMoutput_step)



process.RECOSIMoutput.outputCommands.append('keep *_rawDataCollector_*_*')
process.RECOSIMoutput.outputCommands.append('keep *_simEcalUnsuppressedDigis_*_*')
process.RECOSIMoutput.outputCommands.append('keep *_*_ebDigis_*')
process.RECOSIMoutput.outputCommands.append('keep *_*_eeDigis_*')
process.RECOSIMoutput.outputCommands.append('keep *_*_EcalRecHitsEB_*')
process.RECOSIMoutput.outputCommands.append('keep *_*_EcalRecHitsEE_*')
process.RECOSIMoutput.outputCommands.append('keep *_*_EcalRecHitsES_*')
process.RECOSIMoutput.outputCommands.append('keep *_simEcalPreshowerDigis_*_*')
process.RECOSIMoutput.outputCommands.append('keep *_ecalPreshowerDigis_*_*')
process.RECOSIMoutput.outputCommands.append('keep PileupSummaryInfos_*_*_*')
