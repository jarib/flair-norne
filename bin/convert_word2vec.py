#!/usr/bin/env python

import gensim
import sys

with open(sys.argv[1]) as src:
    print('loading')
    kv = gensim.models.KeyedVectors.load_word2vec_format(src, binary=False)
    print('saving')
    kv.save(sys.argv[2])


