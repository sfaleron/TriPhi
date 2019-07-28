
# Python2 is chosen for its more compact default representation of floats

INKSC = /usr/bin/env inkscape
PY    = /usr/bin/env python2

BASE  = ../src/math.py  ../src/keyattr.py ../src/options.py
FIGR  =   ../figure.py ../src/__init__.py  ../src/layers.py ../lib/phiglyph.svg $(BASE)
UNIT  = ../unitpair.py $(BASE)

all: figure.svg unitpair.svg fourdeep.svg

bitmaps: figure.png unitpair.png fourdeep.svg

figure.svg:  $(FIGR)
	$(PY) ../figure.py > $@

unitpair.svg:    $(UNIT)
	$(PY) ../unitpair.py > $@

fourdeep.svg:    $(UNIT)
	$(PY) ../tiles.py 4 > $@

%.png: %.svg
	$(INKSC) -e $@ $<
