
from   six.moves.configparser import ConfigParser
import os.path as osp
import os

import six
import re

def loadCfg(fileName):
    with open(fileName, 'r') as f:
        psr = ConfigParser()

        if six.PY3:
            psr.read_file(f)
        else:
            psr.readfp(f)

        return psr

def normPath():
    os.chdir(osp.join(osp.dirname(osp.abspath(__file__)), '..'))

def writeSix(f, s):
    return f.write(s if six.PY2 else s.decode('utf-8'))

if __name__ == '__main__':
    with open('src/angles.in.mml', 'r') as f:
        holdReplace.acquire(f.read())
        holdReplace.store()
