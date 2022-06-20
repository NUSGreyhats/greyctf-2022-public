package main

import (
    "fmt"
)



// Adapted from https://cs.opensource.google/go/go/+/refs/tags/go1.18.1:src/encoding/base64/base64.go
func Encode(dst, src []byte) []byte {

	encodeTable := []byte("NaRvJT1B/m6AOXL9VDFIbUGkC+sSnzh5jxQ273d4lHPg0wcEpYqruWyfZoM8itKe")
    pad := '-'

    di, si := 0, 0
    n := (len(src) / 3) * 3
    for si < n {
		val := uint(src[si+0])<<16 | uint(src[si+1])<<8 | uint(src[si+2])

		dst[di+0] = encodeTable[val>>18&0x3F]
		dst[di+1] = encodeTable[val>>12&0x3F]
		dst[di+2] = encodeTable[val>>6&0x3F]
		dst[di+3] = encodeTable[val&0x3F]
		si += 3
		di += 4
    }

	remain := len(src) - si
	if remain == 0 {
		return dst
	}

	val := uint(src[si+0]) << 16
	if remain == 2 {
		val |= uint(src[si+1]) << 8
	}

	dst[di+0] = encodeTable[val>>18&0x3F]
	dst[di+1] = encodeTable[val>>12&0x3F]

	switch remain {
	case 2:
		dst[di+2] = encodeTable[val>>6&0x3F]
		dst[di+3] = byte(pad)
	case 1:
		dst[di+2] = byte(pad)
		dst[di+3] = byte(pad)
	}

    return dst;
}

func EncodeLen(n int) int {
    return (n+2) / 3 * 4
}

func main() {
    var src string
    fmt.Scanln(&src)

    buf := make([]byte, EncodeLen(len(src)))
    fmt.Println(string(Encode(buf, []byte(src))))
}
