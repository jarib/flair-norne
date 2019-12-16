from typing import List


from flair.data import Corpus
from flair.datasets import ColumnCorpus
from flair.embeddings import WordEmbeddings, StackedEmbeddings, TokenEmbeddings
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer



# define columns
columns = {0: 'text', 1: 'lemma', 2: 'pos', 3: "ner"}

# this is the folder in which train, test and dev files reside
data_folder = './norne'

# init a corpus using column format, data folder and the names of the train, dev and test files
corpus = ColumnCorpus(data_folder, columns,
                              train_file='train.txt',
                              test_file='test.txt',
                              dev_file='dev.txt')

tag_type = 'ner'

tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)
print(tag_dictionary.idx2item)


embedding_types: List[TokenEmbeddings] = [

    WordEmbeddings('./vectors/model.w2v'),

    # comment in this line to use character embeddings
    # CharacterEmbeddings(),

    # comment in these lines to use flair embeddings
    # FlairEmbeddings('news-forward'),
    # FlairEmbeddings('news-backward'),
]

embeddings = StackedEmbeddings(embeddings=embedding_types)

tagger = SequenceTagger(hidden_size=256,
                        embeddings=embeddings,
                        tag_dictionary=tag_dictionary,
                        tag_type=tag_type,
                        use_crf=True)

trainer: ModelTrainer = ModelTrainer(tagger, corpus)

# 7. start training
print('training')
trainer.train('./models/flair-norne',
              learning_rate=0.1,
              mini_batch_size=32,
              max_epochs=150)


# 8. plot weight traces (optional)
from flair.visual.training_curves import Plotter
plotter = Plotter()
plotter.plot_weights('./models/flair-norne/weights.txt')
