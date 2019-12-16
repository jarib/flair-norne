# flair-norne

Train [Norwegian NER](https://github.com/ltgoslo/norne) for [flair](https://github.com/zalandoresearch/flair)

# Usage

Make sure you're using Python 3, then:

	pip install -r requirements.txt

	bin/fetch-norne.sh
	bin/fetch-vectors.sh

	python train-ner.py