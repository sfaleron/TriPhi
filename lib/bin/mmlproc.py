
import os.path as osp
import six

from helpers import normPath, loadCfg, holdReplace

def proc(key):
    cfg = loadCfg('parameters')

    substs   = cfg.items(key)
    entities = cfg.items('entities')

    baseIn   = osp.join(cfg.get('srcDir', key), key)
    baseOut  = osp.join( 'intermediates',       key)

    with  open(baseOut   +    '.mml', 'w') as fOut:
        with open(baseIn + '.in.mml', 'r') as fIn:
            #s = holdReplace.substOut(fIn.read())
            s = fIn.read()

            for k,v in substs:
                s = s.replace('_{}_'.format(k.upper()), v)

            for k,v in entities:
                s = s.replace('_{}_'.format(k.upper()), '&{};'.format(v))

        fOut.write(s)

if __name__ == '__main__':
    import sys
    normPath()
    proc(sys.argv[1])
