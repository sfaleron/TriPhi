
# Load left and right length components, then stack them by appending the
# rows from the right component to the end of the left component's table,
# rather than creating a new table and treating them symmetrically.

from __future__ import print_function

import xml.etree.ElementTree as ET

import os.path as osp
import os

from helpers import normPath, writeSix, holdReplace

def stack():
    with open('src/lengthsL.in.mml', 'r') as fLeft, \
         open('src/lengthsR.in.mml', 'r') as fRight:

         # Replace the namespace declaration with a placeholder for later.
         # ETree does some messy stuff that seems to be an attempt to
         # conform to standards. It's already compliant without the mess!

         treeL = ET.ElementTree(ET.fromstring(
             holdReplace.r.sub(holdReplace,  fLeft.read())))

         treeR = ET.ElementTree(ET.fromstring(
             holdReplace.r.sub(holdReplace, fRight.read())))

    rootL  = treeL.getroot()

    tableL = rootL
    while tableL.tag != 'mtable':
        tableL = tableL[0]

    tableR = treeR.getroot()
    while tableR.tag != 'mtable':
        tableR = tableR[0]

    # A space between
    ET.SubElement(tableL, 'mtr')

    tableL.extend(tableR)

    with open('intermediates/lengths.in.mml', 'w') as mmlOut:
        with open('src/lengthsL.in.mml', 'r') as mmlIn:
            mmlTmp = mmlIn.read()
            mmlOut.write(mmlTmp[:mmlTmp.index('<math ')])

        writeSix(mmlOut, ET.tostring(rootL, encoding='utf-8'))

if __name__ == '__main__':
    normPath()
    stack()
