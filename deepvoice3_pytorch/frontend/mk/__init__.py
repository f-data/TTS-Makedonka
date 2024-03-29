# coding: utf-8
from deepvoice3_pytorch.frontend.text.symbols import symbols

#import nltk
from random import random

n_vocab = len(symbols)

#_arphabet = nltk.corpus.cmudict.dict()


def _maybe_get_arpabet(word, p):
    try:
        phonemes = word
        phonemes = " ".join(phonemes)
    except KeyError:
        return word

    return '{%s}' % word


def mix_pronunciation(text, p):
    text = ' '.join(_maybe_get_arpabet(word, p) for word in text.split(' '))
    return text


def text_to_sequence(text, p=0.0):
    if p > 0:
        text = mix_pronunciation(text, p)
    from deepvoice3_pytorch.frontend.text import text_to_sequence
    text = text_to_sequence(text, ["transliteration_cleaners"])
    return text


from deepvoice3_pytorch.frontend.text import sequence_to_text
