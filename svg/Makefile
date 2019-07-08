
# Python2 is chosen for its more compact default representation of floats

INKSC = /usr/bin/env inkscape
PY    = /usr/bin/env python2

BASE  = ../src/math.py  ../src/keyattr.py ../src/options.py
FIGR  =   ../figure.py ../src/__init__.py  ../src/layers.py ../lib/phiglyph.svg $(BASE)
UNIT  = ../unitpair.py $(BASE)

all:  *.svg *.png

figure_std.svg:  $(FIGR)
	$(PY) ../figure.py > $@

figure_flip.svg: $(FIGR)
	$(PY) ../figure.py :flip > $@

unitpair.svg:    $(UNIT)
	$(PY) ../unitpair.py > $@

%.png: %.svg
	$(INKSC) -e $@ $<
