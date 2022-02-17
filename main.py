import model.word2vec
import os
import argparse
import sys


def parse_opt():
    parser = argparse.ArgumentParser()

    # Word2Vec parameter
    parser.add_argument('--data', type=str, default='dataset/wiki_zh.text', help='corpus text path')
    parser.add_argument('--dim', type=int, default=300, help='dimension of word embedding')
    parser.add_argument('--skip_gram', action='store_true', help='skip-gram; otherwise CBOW')
    parser.add_argument('--hs', action='store_true', help='hierarchical softmax will be used, Otherwise, Negtive Sampling')
    parser.add_argument('--window', type=int, default=5, help='Maximum distance between current and predicted word')
    parser.add_argument('--min_count', type=int, default=5, help='filter the words that frequency lower than this')
    parser.add_argument('--weight', type=str, default=None, help='model weights path')

    opt = parser.parse_args()
    return opt


def main(opt):

    wv = model.word2vec.Word2vec(text_path=opt.data, dim=opt.dim, skip_gram=opt.skip_gram, hs=opt.hs, window=opt.window,
                                 min_coun=opt.min_count, weight=opt.weight)


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
