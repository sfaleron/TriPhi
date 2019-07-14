
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


# Replace the namespace declaration with a placeholder for later.
# ETree does some messy stuff that seems to be an attempt to
# conform to standards. It's already compliant without the mess!

class HoldReplace(object):
    _r = re.compile(r'(<math .*(xmlns\s*=\s*\".*?\"))')

    nsFile  = 'intermediates/nsDecl'
    _nsDecl = None

    # Alas, unassigned/boolean attributes are only an HTML feature!
    placeholder  = '_nsDecl=""'

    @property
    def nsDecl(self):
        return self._nsDecl

    @property
    def store(self):
        if self._store is None:
            raise ValueError('No declaration set')
        else:
            return self._store()

    def acquire(self, s):
        m = self._r.search(s)
        if m:
            self._nsDecl = m.group(2)
        else:
            raise ValueError('No declaration found')

    def _replace(self, m):
        self._nsDecl = m.group(2)
        return m.group(1).replace(m.group(2), self.placeholder)

    def store(self):
        if self._nsDecl is None:
            raise ValueError('No declaration set')
        else:
            with open(self.nsFile, 'w') as f:
                f.write(self._nsDecl)

    def substIn(self, s):
        return self._r.sub(self._replace, s)

    def substOut(self, s):
        with open(self.nsFile, 'r') as f:
            return s.replace(self.placeholder, f.read())


holdReplace = HoldReplace()

def writeSix(f, s):
    return f.write(s if six.PY2 else s.decode('utf-8'))

if __name__ == '__main__':
    with open('src/angles.in.mml', 'r') as f:
        holdReplace.acquire(f.read())
        holdReplace.store()
