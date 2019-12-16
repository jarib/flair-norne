#!/bin/bash

URL="http://vectors.nlpl.eu/repository/11/120.zip"
OUT="vectors"

wget "$URL" -O "$OUT.zip"
unzip -d "$OUT" "$OUT.zip"
rm "$OUT".zip

python bin/convert_word2vec.py "$OUT/model.txt" "$OUT/model.w2v"
