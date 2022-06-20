# Challenge Details

Sing me a song and I would consider giving you the flag.

# Setup instructions

Use ./generate_distrib.sh to generate the challenge files. cat test.in | ./chall.sh to test if it is correct.

# Possible hints

1. Not all function calls are captured in xrefs.

# Key Concepts

Reverse engineer binaries that hides its control flow and filtering irrelevant library code to locate user code.

# Solution

1. unpack using upx (this should be obvious)
2. locate user code
3. Realise it's doing an rc4 using a dynamically constructed key and then use a custom encoding to shuffle the lower and higher part of a byte.
4. Since both rc4 and the encodings are reversible, just invoke them on the chunk of ciphertext stored in global variable (.bss) and should get flag.

# Learning objectives

Unpacking binaries
Deal with complex binaries without symbols to locate user code.

# Flag

flag{<3_N3v3r_G0nn4_G1v3_u_Up_<3}
