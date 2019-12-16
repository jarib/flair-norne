#!/bin/bash

mkdir -p norne

curl -L https://raw.githubusercontent.com/ltgoslo/norne/master/ud/nob/no_bokmaal-ud-dev.conllu > norne/dev.conllu
curl -L https://raw.githubusercontent.com/ltgoslo/norne/master/ud/nob/no_bokmaal-ud-train.conllu > norne/train.conllu
curl -L https://raw.githubusercontent.com/ltgoslo/norne/master/ud/nob/no_bokmaal-ud-test.conllu > norne/test.conllu

python bin/preprocess.py norne/dev.conllu > norne/dev.txt
python bin/preprocess.py norne/train.conllu > norne/train.txt
python bin/preprocess.py norne/test.conllu > norne/test.txt
