#!/bin/bash

mkdir -p scripts
mkdir -p models

cp "../code/preproc/histeq.py" "scripts/"
cp "../results/crossval/vgglike-p-32-0.15/drop_fc-0.3/model_best.t7" "models/vgg.t7"
cp "../results/crossval/resnet34/drop-0.1/model_best.t7" "models/resnet.t7"
cp "../results/crossval/tiny-inception-32-32/drop-0.2/model_best.t7" "models/inception.t7"
