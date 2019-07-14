
# Take the length and angles SVGs and create a merged document with each as a
# column in a table with borders.

from helpers import normPath, loadCfg

if __name__ == '__main__':
    cfg    = loadCfg('parameters')
    params = dict(cfg.items('table'))
