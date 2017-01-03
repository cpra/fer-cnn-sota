
Material for paper [Facial Expression Recognition using Convolutional Neural Networks: State of the Art](https://arxiv.org/abs/1612.02903). The `scripts/` folder contains a script that was used for applying histogram equalization to the FER2013 dataset. The `models/` folder contains trained Torch7 models (Table IV in the paper):

File | Architecture | Depth | FER2013 Test Accuracy
---- | ------------ | ----- | ---------------------
`vgg.t7` | VGG | 10 | 72.7%
`inception.t7` | Inception/GoogLeNet | 16 | 71.6%
`resnet.t7` | Resnet-34 | 33 | 72.4%

Author: Christopher Pramerdorfer, TU Wien  
Licence: zlib
