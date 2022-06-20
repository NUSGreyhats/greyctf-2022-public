manipulation:
	g++ manipulation.cpp -o manipulation.o; \
	patchelf --set-interpreter ./ld-2.23.so ./manipulation.o; \
	patchelf --replace-needed libc.so.6 ./libc-2.23.so ./manipulation.o