parcel: codegen.py all.c all.h parcel.c
	python3 codegen.py
	gcc -no-pie parcel.c all.c -o parcel
	upx parcel