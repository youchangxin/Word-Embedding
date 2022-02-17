import logging
import sys
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


# define output
class Word2vec:
    def __init__(self, text_path=None, dim=300, skip_gram=False, hs=False, window=None, min_coun=None, weight=None):

        logger = logging.getLogger()
        logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
        logging.root.setLevel(level=logging.INFO)
        logger.info("running %s" % ' '.join(sys.argv))

        if weight is not None:
            self.model = Word2Vec.load(weight)
        else:
            self.model = Word2Vec(LineSentence(text_path), vector_size=dim, window=window, min_count=min_coun,
                                  workers=multiprocessing.cpu_count(), sg=skip_gram, hs=hs)

        self.output_model = "output/wiki.zh.text.model"
        self.output_vector = "output/wiki.zh.text.vector"
        self.model.save(self.output_model)
        self.model.save_word2vec_format(self.output_vector, binary=False)

