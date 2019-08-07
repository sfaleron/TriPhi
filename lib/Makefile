
# Abbrivations:
# r: .in.mml "raw"  although lengths.in.mml is derived
# m: .mml    "mml"  "raw" is also valid mml, but this is
#                   the final mml with substitutions made
# s: .svg    "svg"

NODE = /usr/bin/env node
LINT = /usr/bin/env xmllint --noout
PY   = /usr/bin/env python

MMLDEPS = bin/mmlproc.py parameters
SVGDEPS = bin/mml2svg.js
ENDDEPS = parameters intermediates/angles.svg bin/relationships.py

STEPDEPS = $(ENDDEPS) intermediates/lengthsL.svg intermediates/lengthsR.svg
TABLDEPS = $(ENDDEPS) intermediates/lengths.svg

#ALLDEPS  = $(TABLDEPS)
ALLDEPS  = $(STEPDEPS)

all: relationships.svg

relationships.svg: $(ALLDEPS)
	$(PY) relationships.py

intermediates/lengths.in.mml: bin/stack-lengths.py \
	src/lengthsL.in.mml src/lengthsR.in.mml
	$(PY) bin/stack-lengths.py

# These dependencies are not handled well by pattern rules, because the
# target and dependency are in distict directories. I'm not sure if there's
# a way to finesse it, but having explicit recipes when the rules are already
# explicit costs very little.
intermediates/lengthsL.mml:         src/lengthsL.in.mml $(MMLDEPS)
	$(PY) bin/mmlproc.py lengthsL
intermediates/lengthsR.mml:         src/lengthsR.in.mml $(MMLDEPS)
	$(PY) bin/mmlproc.py lengthsR
intermediates/lengths.mml: intermediates/lengths.in.mml $(MMLDEPS)
	$(PY) bin/mmlproc.py lengths
intermediates/angles.mml:             src/angles.in.mml $(MMLDEPS)
	$(PY) bin/mmlproc.py angles

intermediates/lengthsL.svg:  intermediates/lengthsL.mml $(SVGDEPS)
intermediates/lengthsR.svg:  intermediates/lengthsR.mml $(SVGDEPS)
intermediates/lengths.svg:    intermediates/lengths.mml $(SVGDEPS)
intermediates/angles.svg:      intermediates/angles.mml $(SVGDEPS)

%.svg: %.mml
	$(NODE) bin/mml2svg $(notdir $*)


.PHONY: rootDeps touchLeaves all \
	    clean    lintAll lintR   \
	    lintLr   lintLm  lintLs  \
	    lintRr   lintRm  lintRs  \
	    lintAr   lintAm  lintAs  \
	    lintLRr  lintLRm lintLRs

clean:
	( cd intermediates; rm -f ../relationships.svg lengths.in.mml \
	lengthsL.mml lengthsL.svg lengthsR.mml lengthsR.svg \
	lengths.mml  lengths.svg	angles.mml   angles.svg )

touchLeaves:
	touch src/lengthsL.in.mml src/lengthsR.in.mml src/angles.in.mml parameters

rootDeps: intermediates/lengthsL.svg intermediates/lengths.svg \
	      intermediates/lengthsR.svg intermediates/angles.svg

lintAll:  lintAll lintR  \
	lintLr  lintLm  lintLs \
	lintRr  lintRm  lintRs \
	lintAr  lintAm  lintAs \
	lintLRr lintLRm lintLRs

lintR:
	$(LINT) relationships.svg            || true

# lengths, left/right
lintLr:
	$(LINT) src/lengthsL.in.mml          || true
lintLm:
	$(LINT) intermediates/lengthsL.mml   || true
lintLs:
	$(LINT) intermediates/lengthsL.svg   || true

lintRr:
	$(LINT) src/lengthsR.in.mml          || true
lintRm:
	$(LINT) intermediates/lengthsR.mml   || true
lintRs:
	$(LINT) intermediates/lengthsR.svg   || true

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
