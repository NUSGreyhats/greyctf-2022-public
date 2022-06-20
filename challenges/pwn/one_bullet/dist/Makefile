one_bullet:
	gcc one_bullet.c -o one_bullet.o -lseccomp; \
	patchelf --replace-needed libc.so.6 ./libc-2.31.so ./one_bullet.o; \
	patchelf --set-interpreter ./ld-2.31.so ./one_bullet.o; \
	chmod +x ./one_bullet.o;