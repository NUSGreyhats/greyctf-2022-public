blockchain:
	g++ blockchain.cpp -o blockchain.o -no-pie; \
	patchelf --replace-needed libc.so.6 ./libc.so.6 ./blockchain.o; \
	patchelf --set-interpreter ./ld.so ./blockchain.o; \
	chmod +x blockchain.o