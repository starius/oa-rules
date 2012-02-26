
.SECONDEXPANSION:

build: oa-rules.pdf

%.pdf: %.tex
	pdflatex $<
	pdflatex $<

