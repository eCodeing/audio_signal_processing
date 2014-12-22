import soundAnalysis as SA
import soundAnalysisEssentia as SAE

### Use descriptors downloaded from freesound.org ###
#SA.clusterSounds('testDownload', nCluster=10, descInput=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

### Use descriptors extracted using using Essentia functions ###
#SAE.clusterSounds('essentiaDownload2', nCluster=10, descInput=[0,1,2,3,4,5,6,7,11])

### Use descriptors extracted using using Essentia functions with silence frames removed ###
SAE.clusterSounds('essentiaDownload3', nCluster=10, descInput=[0,1,2,3,4,5,6,7,11,13,14])

#6,7,11,13,14,1,2
