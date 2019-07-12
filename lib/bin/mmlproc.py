
from   six.moves.configparser import ConfigParser
import os.path as osp

import os
import sys
import six
key = sys.argv[1]

os.chdir(osp.dirname(osp.abspath(__file__)))



cfg = ConfigParser()

loader = cfg.read_file if six.PY3 else cfg.readfp

loader(open('parameters.cfg', 'r'))

substs = cfg.items(key)

with open(key+'.mml', 'w') as fOut:
    with open(key+'.in.mml', 'r') as fIn:
        s = fIn.read()
        for k,v in substs:
            s = s.replace('%{}%'.format(k.upper()), v)

    fOut.write(s)
