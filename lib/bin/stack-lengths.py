
# Load left and right length components, then stack them by appending the
# rows from the right component to the end of the left component's table,
# rather than creating a new table and treating them symmetrically.

from __future__ import print_function

from helpers import normPath, writeSix

def stack():
    with open('src/lengthsL.in.mml', 'r') as fdL, \
         open('src/lengthsR.in.mml', 'r') as fdR:

         wholeL = fdL.read()
         wholeR = fdR.read()

         startL = wholeL. index('<mtr>')
         endL   = wholeL.rindex('</mtable>')
         bodyL  = wholeL[startL:endL]
         head   = wholeL[:startL]

         startR = wholeR. index('<mtr>')
         endR   = wholeR.rindex('</mtable>')
         bodyR  = wholeR[startR:endR]
         tail   = wholeR[endR:]

         wholeOut = '\n'.join([i.strip() for i in (
             head, bodyL, '<mtr></mtr>', bodyR, tail )])

         with open('intermediates/lengths.in.mml', 'w') as mmlOut:
             #writeSix(mmlOut, wholeOut)
             mmlOut.write(wholeOut)

if __name__ == '__main__':
    normPath()
    stack()
