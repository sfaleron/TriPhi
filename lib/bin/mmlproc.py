
from   six.moves.configparser import ConfigParser
import os.path as osp
import six

from helpers import normPath, holdReplace

def proc(key):
    cfg = ConfigParser()

    loader = cfg.read_file if six.PY3 else cfg.readfp

    loader(open('parameters', 'r'))

    substs   = cfg.items(key)
    entities = cfg.items('entities')

    src = None
    for i in range(len(substs)):
        k,v = substs[i]
        if k == 'src':
            src = v
            break

    baseIn  = osp.join( src,            key)
    baseOut = osp.join('intermediates', key)

    with  open(baseOut   +    '.mml', 'w') as fOut:
        with open(baseIn + '.in.mml', 'r') as fIn:
            s = holdReplace.subst(fIn.read())

            for k,v in substs:
                s = s.replace('_{}_'.format(k.upper()), v)

            for k,v in entities:
                s = s.replace('_{}_'.format(k.upper()), '&{};'.format(v))

        fOut.write(s)

if __name__ == '__main__':
    import sys
    normPath()
    proc(sys.argv[1])
