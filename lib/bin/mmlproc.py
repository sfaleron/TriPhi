
import os.path as osp
import six

from helpers import normPath, loadCfg

def proc(key):
    cfg = loadCfg('parameters')

    substs   = cfg.items(key)

    baseIn   = osp.join('intermediates'  if key == 'lengths' else 'src', key)
    baseOut  = osp.join('intermediates', key)

    with  open(baseOut   +    '.mml', 'w') as fOut:
        with open(baseIn + '.in.mml', 'r') as fIn:
            s = fIn.read()

            for k,v in substs:
                s = s.replace('_{}_'.format(k.upper()), v)

        fOut.write(s)

if __name__ == '__main__':
    import sys
    normPath()
    proc(sys.argv[1])
