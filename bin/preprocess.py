import re
import sys

name_re = re.compile(r".*name=(\S+)")

for line in open(sys.argv[1], "r"):
    line = line.strip()

    if not line:
        print("")
    elif not line.startswith("#"):
        parts = line.split("\t")
        text = parts[1]
        lemma = parts[2]
        pos = parts[3]
        ner = parts[9]

        print(" ".join([text, lemma, pos, name_re.match(ner)[1]]))
