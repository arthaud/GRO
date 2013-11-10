morpion_minmax.so: morpion_minmax.h morpion_minmax.c
	gcc -o morpion_minmax.so -shared -fPIC -Wall morpion_minmax.c -I/usr/include/python2.7 -lpython2.7

clean:
	rm -f morpion_minmax.so
	rm -f rapport_jeux.aux
	rm -f rapport_jeux.log
	rm -f rapport_jeux.lol
	rm -f rapport_jeux.out
	rm -f rapport_jeux.pdf
	rm -f rapport_jeux.toc

rapport_jeux.pdf: pdf
pdf:
	pdflatex rapport_jeux.tex
