
# Take the length and angles SVGs and create a merged document with each as a
# column in a table with borders.

from   six.moves.configparser import ConfigParser
import os.path as osp
import os

os.chdir(osp.dirname(osp.abspath(__file__)))


cfg = ConfigParser()

loader = cfg.read_file if six.PY3 else cfg.readfp

loader(open('parameters', 'r'))

params = dict(cfg.items('table'))
