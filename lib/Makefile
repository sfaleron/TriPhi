
# Abbrivations:
# r: .in.mml "raw"  although lengths.in.mml is derived
# m: .mml    "mml"  "raw" is also valid mml, but this is
#                   the final mml with substituions made
# s: .svg    "svg"

NODE = /usr/bin/env node
LINT = /usr/bin/env xmllint --noout
PY   = /usr/bin/env python

MMLDEPS = bin/mmlproc.py parameters
SVGDEPS = bin/mml2svg.js


all: relationships.svg

relationships.svg:  parameters intermediates/angles.svg bin/relationships.py \
	intermediates/lengthsL.svg intermediates/lengthsR.svg
	$(PY) relationships.py

intermediates/lengthsL.mml:         src/lengthsL.in.mml $(MMLDEPS)
intermediates/lengthsL.svg:  intermediates/lengthsL.mml $(SVGDEPS)

intermediates/lengthsR.mml:         src/lengthsR.in.mml $(MMLDEPS)
intermediates/lengthsR.svg:  intermediates/lengthsR.mml $(SVGDEPS)

intermediates/angles.mml:             src/angles.in.mml $(MMLDEPS)
intermediates/angles.svg:      intermediates/angles.mml $(SVGDEPS)

intermediates/lengths.mml: intermediates/lengths.in.mml $(MMLDEPS)
intermediates/lengths.svg:    intermediates/lengths.mml $(SVGDEPS)

intermediates/lengths.in.mml: \
	intermediates/lengthsL.in.mml intermediates/lengthsR.in.mml
	$(PY) bin/stacklengths.py

%.mml: %.in.mml
	$(PY) bin/mmlproc.py $*

%.svg: %.mml
	$(NODE) bin/mml2svg $< $@


.PHONY: lintR                   \
	    lintLr  lintLm  lintLs  \
	    lintRr  lintRm  lintRs  \
		lintAr  lintAm  lintAs  \
	    lintLRr lintLRm lintLRs


lintR:
	$(LINT) relationships.svg || true

# lengths, left/right

lintLr:
	$(LINT) intermediates/lengthsL.in.mml || true

lintLm:
	$(LINT) intermediates/lengthsL.mml    || true

lintLs:
	$(LINT) intermediates/lengthsL.svg    || true

lintRr:
	$(LINT) intermediates/lengthsR.in.mml || true

lintRm:
	$(LINT) intermediates/lengthsR.mml    || true

lintRs:
	$(LINT) intermediates/lengthsR.svg    || true


# left/right lengths, stacked as a single column

lintLRr:
	$(LINT) intermediates/lengths.in.mml || true

lintLRm:
	$(LINT) intermediates/lengths.mml    || true

lintLRs:
	$(LINT) intermediates/lengths.svg    || true


# angles

lintAr:
	$(LINT) src/angles.in.mml            || true

lintAm:
	$(LINT) intermediates/angles.mml     || true

lintAs:
	$(LINT) intermediates/angles.svg     || true
