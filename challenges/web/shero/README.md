# shero

### Challenge Details

harder version of [regex_hero_2](https://github.com/NUSGreyhats/internal-ctf/tree/master/challenges/regex_hero_2) with less allowed character. ``!preg_match('#[^cat -/:-@\[-`\{-~]#', $file)`` (36 characters allowed) -> `!preg_match('#[^.cat!? /\|\-\[\]\(\)\$]#', $file)` (15 characters allowed)

### Key Concepts

bash/sh tricks

### Solution

similar idea as [regex_hero_2](https://github.com/NUSGreyhats/internal-ctf/tree/master/challenges/regex_hero_2), refer to [sol.py](./sol.py)

### Learning Objectives

bash/sh tricks

### Flag

grey{r35p3c7_70_5h_m4573r_0dd14e9bc3172d16}

### Credit

credit to [SaneBow](https://github.com/SaneBow) for contributing this challenge idea and solution.
