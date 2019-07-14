
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


class HoldReplace(object):
    _r = re.compile(r'(<math .*(xmlns\s*=\s*\".*?\"))')

    nsFile  = 'intermediates/nsDecl'
    _nsDecl = None

    # Alas, unassigned/boolean attributes are only an HTML feature!
    placeholder  = '_nsDecl=""'

    @property
    def r(self):
        return self._r

    @property
    def nsDecl(self):
        return self._nsDecl

    def __call__(self, m):
        self.store = self._store
        self._nsDecl = m.group(2)
        return m.group(1).replace(m.group(2), self.placeholder)

    def _store(self):
        with open(self.nsFile, 'w') as f:
            f.write(self._nsDecl)

    def subst(self, s):
        with open(self.nsFile, 'r') as f:
            return s.replace(self.placeholder, f.read())


holdReplace = HoldReplace()

def writeSix(f, s):
    return f.write(s if six.PY2 else s.decode('utf-8'))

if __name__ == '__main__':
    with open('src/angles.in.mml', 'r') as f:
        holdReplace.r.search(f.read()))
        holdReplace.store()
