import soundAnalysis as SA
import soundAnalysisEssentia as SAE

### Use descriptors downloaded from freesound.org ###
#SA.descriptorPairScatterPlot('testDownload', descInput=(1,3))

### Use descriptors extracted using using Essentia functions ###
#SAE.descriptorPairScatterPlot('essentiaDownload2', descInput=(1,3))

### Use descriptors extracted using using Essentia functions with silence frames removed ###
SAE.descriptorPairScatterPlot('essentiaDownload3', descInput=(1,3))

#SA.showDescriptorMapping()
