#!/bin/bash

URL="http://vectors.nlpl.eu/repository/11/120.zip"
OUT="vectors"

wget "$URL" -O "$OUT.zip"
unzip -d "$OUT" "$OUT.zip"

python bin/convert_word2vec.py vectors/model.txt vectors/model.w2v