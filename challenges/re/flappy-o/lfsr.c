#include <stdio.h>
#include <string.h>

unsigned short lfsr1(int n) {
    int i, lsb;
	int seed = 0xabcd;

    for (i=0; i<n; i++) {
        lsb = seed & 1;
        seed >>= 1;
        if (lsb) seed ^= 0x82EE;
    }

	return seed;
}

int lfsr2_seed = 0x1a2b3c4d;
unsigned int lfsr2(int n) {
    int i, lsb;

    for (i=0; i<n; i++) {
        lsb = lfsr2_seed & 1;
        lfsr2_seed >>= 1;
        if (lsb) lfsr2_seed ^= 0x80000DD7;
    }

	return lfsr2_seed;
}

unsigned char flag1[] = "grey{y0u_4r3_pr0_4t_7h1s_g4m3_b6d8745a1cc8d51effb86690bf4b27c9}";
unsigned char flag2[] = "grey{y0u_4r3_v3ry_g00d_4t_7h1s_g4m3_c4n_y0u_t34ch_m3_h0w_t0_b3_g00d_ef4bd282d7a2ab1ebdcc3616dbe7afb}";

unsigned int enc2[] = {0x7caa42eb, 0xcd53fda8, 0xf7420557, 0x5267eec4, 0x793e70ed, 0x68d1aec0, 0x38da23eb, 0x6f1d6fb1, 0x39489b7b, 0xf4f87516, 0xed67bc18, 0x8ad36ba0, 0xaf2a684f, 0x80883171, 0x86ce7d28, 0x438cb016, 0x5784988c, 0x4bb5278b, 0xbfdcd0c6, 0x6dda7789, 0xb0f09aa3, 0x557478be, 0xc372aee8, 0x40a28470, 0xa855383a};

int main() {
    unsigned char enc1[sizeof(flag1)];
    printf("%lu\n", sizeof(flag1));
    for (int i = 0; i < sizeof(flag1)-1; ++i) {
        printf("%02x", lfsr1(i));
        enc1[i] = flag1[i] ^ (lfsr1(i) & 0xff);
    }
    puts("");
    for (int i = 0; i < sizeof(flag1)-1; ++i) {
        printf("\\x%02x", enc1[i]);
    }
    puts("");

    lfsr2_seed = 0x1a2b3c4d;
    // for (int i = 0; i < sizeof(flag2) / 4; ++i) {
    //     lfsr2(10000);
    //     printf("0x%08x, ", lfsr2(lfsr1(i * 10000)) ^ ((unsigned int*)flag2)[i]);
    // }
    for (int i = 1; i <= sizeof(flag2) / 4 * 10000; ++i) {
        lfsr2(1);
        if (i >= 10000 && i % 10000 == 0 && i/10000 <= sizeof(flag2)/4)
            printf("0x%08x, ", lfsr2(lfsr1(i-10000)) ^ ((unsigned int*)flag2)[i/10000-1]);
    }
    puts("");

    unsigned int dec2[sizeof(enc2)] = {};
    lfsr2_seed = 0x1a2b3c4d;
    // for (int i = 0; i < sizeof(flag2) / 4; ++i) {
    //     lfsr2(10000);
    //     dec2[i] = lfsr2(lfsr1(i * 10000)) ^ enc2[i];
    // }
    for (int i = 1; i <= sizeof(enc2) / 4 * 10000+200000; ++i) {
        lfsr2(1);
        if (i % 10000 == 0 && i/10000 <= sizeof(enc2)/4)
            ((unsigned int*)dec2)[i/10000-1] = lfsr2(lfsr1(i-10000)) ^ enc2[i/10000-1];
    }
    printf("%s\n", (char*)dec2);
    return 0;
}