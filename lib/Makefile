
NODE = /usr/bin/env node
LINT = /usr/bin/env xmllint

all: lengths.svg angles.svg

relations.svg: relations.mml
	$(NODE) mml2svg relations.mml relations.svg

%.svg: %.mml
	$(NODE) mml2svg $< $@

.PHONY: lintl linta

lintl:
	$(LINT) lengths.mml || true

linta:
	$(LINT)  angles.mml || true
