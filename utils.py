import logging
import os.path
import sys
from gensim.corpora import WikiCorpus


def wikiCorpus(path):
    prefixPath = os.path.dirname(path)
    output = prefixPath + "/wiki_zh.text"

    logger = logging.getLogger(prefixPath)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
    space = " "
    i = 0
    wiki = WikiCorpus(path, dictionary={})
    with open(output, mode='w', encoding='utf-8') as f:
        for text in wiki.get_texts():
            f.write(space.join(text) + "\n")
            i = i + 1
            if i % 10000 == 0:
                logger.info("Saved " + str(i) + " articles")
    logger.info("Finished Saved " + str(i) + " articles")


if __name__ == '__main__':
    wikiCorpus("/Volumes/Seagate/DataSet/zhwiki.xml.bz2")
