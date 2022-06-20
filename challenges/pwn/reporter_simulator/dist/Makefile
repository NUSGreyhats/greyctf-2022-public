reporter:
	gcc reporter.c -o reporter.o; \
	patchelf --replace-needed libc.so.6 ./libc.so.6 ./reporter.o; \
	patchelf --set-interpreter ./ld.so ./reporter.o; \
	chmod +x ./reporter.o;