
# Load left and right length components, then stack them by appending the
# rows from the right component to the end of the left component's table,
# rather than creating a new table and treating them symmetrically.

import xml.etree.ElementTree as ET
import six

import os.path as osp
import os

os.chdir(osp.join(osp.dirname(osp.abspath(__file__)), '..'))

tagMatch = lambda s, tag: tag == s[s.rfind('}')+1:]

def stack():
    psrL = ET.XMLParser()
    psrL.entity.update(phi=chr(0x9c3) if six.PY3 else unichr(0x3c6))

    psrR = ET.XMLParser()
    psrR.entity.update(phi=chr(0x9c3) if six.PY3 else unichr(0x3c6))

    treeL = ET.parse('src/lengthsL.in.mml', parser=psrL)
    treeR = ET.parse('src/lengthsR.in.mml', parser=psrR)

    rootL  = treeL.getroot()

    tableL = rootL
    while not tagMatch(tableL.tag, 'mtable'):
        tableL = tableL[0]

    tableR = treeR.getroot()
    while not tagMatch(tableR.tag, 'mtable'):
        tableR = tableR[0]

    # A space between
    ET.SubElement(tableL, 'mtr')

    tableL.extend(tableR)

    with open('intermediates/lengths.in.mml', 'w') as mmlOut:
        with open('src/lengthsL.in.mml', 'r') as mmlIn:
            mmlTmp = mmlIn.read()
            mmlOut.write(mmlTmp[:mmlTmp.index('<math ')])

        mmlOut.write(ET.tostring(rootL, encoding='utf-8').replace('ns0:', ''))

if __name__ == '__main__':
    stack()


# proposed fix: remove xmlns from input!
# increment the HEAD pulled off, add </math> at the end
# might have to remove it from both inputs?
# poke mom/liz about stuff to bring
