morpion_minmax.so: morpion_minmax.h morpion_minmax.c
	gcc -o morpion_minmax.so -shared -fPIC -Wall morpion_minmax.c -I/usr/include/python2.7 -lpython2.7

clean:
	rm -f morpion_minmax.so
