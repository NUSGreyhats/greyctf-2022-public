

# Challenge Details

There are 2 encoders with 2 encoded files. Figure out how the encoder performs the encoding and reverse the encoding to get flag.

# Setup instructions

Download the challenge files and Reverse engineer them to find a way to get the correct answer to challenges.

# Possible hints

Hints is given for haskell reverse engineering in distrib file.

# Key Concepts

Reverse engineering runtime binary.

# Solution

Haskell: xorshift32 with time as seed
Golang: base64 with custom charset

# Learning objectives

Reverse engineering runtime binary

# Flag

haskell: flag{Funct1on41_P4rad1s3_iZ_Fun}
golang: flag{B4s3d_G0Ph3r_r333333}
