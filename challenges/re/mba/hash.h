

unsigned long hash(const char *msg, size_t len) {
    unsigned long seed = 0x5ca1ab1ef01dab1e;
    for (int i=0; i < len; i++) {
        seed ^= msg[i];
        seed = (seed << 8) ^ (seed >> 56);
    }
    return seed;
}