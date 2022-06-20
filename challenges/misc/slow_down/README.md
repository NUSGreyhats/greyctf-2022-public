# Slow Down

### Challenge Details
A simple program (source code given) that asks for inputs to a hashmap, or reads from it. The goal is to make the hashmap operations slow enough to get the flag.

### Setup instructions
`docker compose up`

### Possible hints
1. What is the time complexity of operations of `unordered_map`?
2. Is it always fast? When does it slow down?

### Key Concepts
Hash collision attacks on hashmaps to adversarially slow down operations.

### Solution
Insert keys tha are multiples of 42043 (prime). See `solve.py`.

### Learning objectives
Data structures and algorithms :P (Possibly) learn about C++ hashmap resize policy (GNU G++ 6.4.0).

### Flag
`grey{h4sHmaP5_r_tH3_k1nG_of_dAt4_strUcTuRe5}`

