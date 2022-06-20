from Crypto.Util.number import bytes_to_long, getStrongPrime

# m ^ 3 ^ 2 ^ 100

FLAG = b'grey{CubeIsSquarerThanSquare_FjUFynTNUdTyJu5x}'

m = bytes_to_long(FLAG)
p = 147271787827929374875021125075644322658199797362157810465584602627709052665153637157027284239972360505065250939071494710661089022260751215312981674288246413821920620065721158367282080824823494257083257784305248518512283466952090977840589689160607681176791401729705268519662036067738830529129470059752131312559

phi = (p - 1) // 2 - 1

a = pow(2, 100, phi)
b = pow(3, a, p - 1)
c = pow(m, b, p)

print(c)