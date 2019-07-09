
NODE = /usr/bin/env node

all: lengths.svg angles.svg

relations.svg: relations.mml
	$(NODE) mml2svg relations.mml relations.svg

%.svg: %.mml
	$(NODE) mml2svg $< $@
