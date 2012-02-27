
.SECONDEXPANSION:

build: oa-rules.pdf binomdist.pdf

%.pdf: %.tex
	pdflatex $<
	pdflatex $<

binomdist.tex: binomdist.py
	cat $@.top > $@
	python $< >> $@
	cat $@.bottom >> $@

