import os
import logging
import os.path
import sys
import multiprocessing
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


# define output

def word2vec(text_path, vector_size=400, window=5):
    prefixPath = os.path.dirname(text_path)
    out_model = prefixPath + 'wiki.zh.text.model'
    out_vector = prefixPath + 'wiki.zh.text.vector'

    logger = logging.getLogger(prefixPath)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    model = Word2Vec(LineSentence(text_path), vector_size=vector_size, window=window, min_count=5,
                     workers=multiprocessing.cpu_count())

    # OUPUT
    model.save("../output/wiki.zh.text.model")
    model.save_word2vec_format("../output/wiki.zh.text.vector", binary=False)
