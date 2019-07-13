
# Abbrivations:
# r: .in.mml "raw"  although lengths.in.mml is derived
# m: .mml    "mml"  "raw" is also valid mml, but this is
#                   the final mml with substituions made
# s: .svg    "svg"

# dependency for "m" targets do not work, except for the derived "r"
# most likely something to do with target and dependency sharing a directory

NODE = /usr/bin/env node
LINT = /usr/bin/env xmllint --noout
PY   = /usr/bin/env python

MMLDEPS = bin/mmlproc.py parameters intermediates/nsDecl
SVGDEPS = bin/mml2svg.js
ENDDEPS = parameters intermediates/angles.svg bin/relationships.py

STEPDEPS = $(ENDDEPS) intermediates/lengthsL.svg intermediates/lengthsR.svg
TABLDEPS = $(ENDDEPS) intermediates/lengths.svg

#ALLDEPS  = $(TABLDEPS)
ALLDEPS  = $(STEPDEPS)

all: relationships.svg

relationships.svg: $(ALLDEPS)
	$(PY) relationships.py

intermediates/nsDecl: src/lengthsL.in.mml src/lengthsR.in.mml src/angles.in.mml
	$(PY) bin/helpers.py

intermediates/lengthsL.mml:         src/lengthsL.in.mml $(MMLDEPS)
intermediates/lengthsL.svg:  intermediates/lengthsL.mml $(SVGDEPS)

intermediates/lengthsR.mml:         src/lengthsR.in.mml $(MMLDEPS)
intermediates/lengthsR.svg:  intermediates/lengthsR.mml $(SVGDEPS)

intermediates/lengths.mml: intermediates/lengths.in.mml $(MMLDEPS)
intermediates/lengths.svg:    intermediates/lengths.mml $(SVGDEPS)

intermediates/angles.mml:             src/angles.in.mml $(MMLDEPS)
intermediates/angles.svg:      intermediates/angles.mml $(SVGDEPS)

intermediates/lengths.in.mml: src/lengthsL.in.mml src/lengthsR.in.mml
	$(PY) bin/stacklengths.py

%.mml: %.in.mml
	$(PY) bin/mmlproc.py $(notdir $*)

%.svg: %.mml
	$(NODE) bin/mml2svg $< $@


.PHONY: all   touchLeaves  \
	clean   lintAll lintR  \
	lintLr  lintLm  lintLs \
	lintRr  lintRm  lintRs \
	lintAr  lintAm  lintAs \
	lintLRr lintLRm lintLRs

clean:
	( cd intermediates; rm -f ../relationships.svg lengths.in.mml \
	lengthsL.mml lengthsL.svg lengthsR.mml lengthsR.svg nsDecl \
	lengths.mml  lengths.svg	angles.mml   angles.svg )

touchLeaves:
	touch src/lengthsL.in.mml src/lengthsR.in.mml src/angles.in.mml parameters

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
