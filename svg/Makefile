
INKSC = env inkscape

BASE = ../src/options.py ../src/math.py ../src/keyattr.py
FIGR = ../figure.py     ../src/__init__.py ../src/layers.py ../src/phiglyph.svg $(BASE)
UNIT = ../unitpair.py   $(BASE)

all: *.svg *.png

figure_std.svg:  $(FIGR)
	python2 ../figure.py > $@

figure_flip.svg: $(FIGR)
	python2 ../figure.py :flip > $@

unitpair.svg:    $(UNIT)
	python2 ../unitpair.py > $@

%.png: %.svg
	$(INKSC) -e $@ $<
