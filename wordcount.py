import os
import re


def get_context(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.read()
        f.close()
    return lines


def pickup_names(fname):
    allnames = []
    context = get_context(fname)
    names = re.findall(r'^\\input{(.*?)}', context, re.MULTILINE)
    while len(names) > 0:
        allnames.extend(names)
        names_local = []
        for fn in names:
            context_local = get_context(fn)
            # names_local = re.findall(r'^\\input{(.*?)}', context_local, re.MULTILINE)
            names_local.extend(re.findall(
                r'^\\input{(.*?)}', context_local, re.MULTILINE))
        names = names_local
    return allnames

def word_in_file(fname):
    hanzi_regex = re.compile(r'[\u4E00-\u9FA5]')
    nbrOfWords = 0
    with open(fname, 'r', encoding='utf-8') as f:
        words = f.read()
        f.close()
        hanzi_list = hanzi_regex.findall(words)
        nbrOfWords = len(hanzi_list)
    return nbrOfWords


if __name__ == "__main__":
    rootFile = 'remember.tex'
    allFiles = pickup_names(rootFile)
    totalWords = 0
    for fn in allFiles:
        totalWords += word_in_file(fn)
    print("总字数为：",totalWords)

