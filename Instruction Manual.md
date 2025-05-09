# M103_Project

This is the repository for our project in MATH 103, where we create a Python program for students to have hands-on experience on the following basic ciphers:
  - Caesar cipher
  - Affine cipher
  - Vigenère cipher

## Brief Overview of the ciphers

### Caesar cipher

Widely regarded as one of the most basic and historically significant ciphers, the Caesar cipher is a building block in classical cryptography. The key idea is that an encoded text is encrypted by having its characters "shifted" by a number of letters in the alphabet.

For example, let's say we have a text `abc`. The person encrypting can shift the letters by 3, so that the text is encrypted as `def`.

Each letter has an index in the alphabet, from 0 to 25. A -> 0, B -> 1, … , Z -> 25.
The idea of the "shift" is to add the index of each character in the text by a specified number. In the text `abc`:
  - a -> 0
  - b -> 1
  - c -> 2
Once shifted by 3, it then becomes:
  - a -> 0 + 3 = 3 -> d
  - b -> 1 + 3 = 4 -> e
  - c -> 2 + 3 = 5 -> f

The shift is of modulo 26. So a shift by 27, by modular arithmetic, is just a shift by 1 (27 ≡ 1 mod 26).

### Affine cipher

Similar to the Caesar cipher, the Affine cipher shifts each letter's index by a specified amount, but utilizes multiplicative and additive shifting. The person encrypting uses two numbers, a and b, such that

  - E(x) = ax + b mod 26
  - D(x) = a^-1(x-b) mod 26

where x is the index of a character in the alphabet, and a^-1 is the modular inverse of a. Note that a must be coprime with 26, otherwise the cipher is not reversible.

For example, we have a text `abcde`. If a = 5 and b = 10, then

  - a -> 0 : 5(0) + 10 ≡ 10 mod 26 -> k
  - b -> 1 : 5(1) + 10 ≡ 15 mod 26 -> p
  - c -> 2 : 5(2) + 10 ≡ 20 mod 26 -> u
  - d -> 3 : 5(3) + 10 ≡ 25 mod 26 -> z
  - e -> 4 : 5(4) + 10 ≡ 30 ≡ 4 mod 26 -> e

So, `abcde` is encrypted to `kpuze`. Deciphering `kpuze` becomes:

  - k -> 10 : 21(10 - 10) ≡ 0 mod 26 -> a
  - p -> 15 : 21(15 - 10) ≡ 1 mod 26 -> b
  - u -> 20 : 21(20 - 10) ≡ 2 mod 26 -> c
  - z -> 25 : 21(25 - 10) ≡ 3 mod 26 -> d
  - e -> 4 : 21(4 - 10) ≡ -126 ≡ 4 mod 26 -> e

Note that the modular inverse of a = 5 is a^-1 = 21.

### Vigenère cipher

The Vigenère cipher, at its core, uses a key. However, the idea of it is that it is a combination of multiple Caesar ciphers. The person can input a text, and then input a key. The cipher itself will use the indeces of each letter in the key to shift each character of the text correspondingly. The formula is

E_i = (T_i + K_i) mod 26

where T_i is the index of the ith letter in the text, and K_i is the index of the ith letter in the key, corresponding to the alphabet. Note that a = 0, b = 1, … z = 26. The resulting E_i is the index of the ith letter of the encrypted text.

For decryption, the formula is

D_i = (C_i - K_i) mod 26

where C_i is the index of the ith letter in the encrypted text, and K_i is the index of the ith letter in the key, corresponding to the alphabet.

For example, with text `abcd` and key `efgh`:

- a = 0; e = 4
  - E = (0 + 4) ≡ 4 mod 26
  - a -> e
- b = 1; f = 5
  - E = (1 + 5) ≡ 6 mod 26
  - b -> g
- c = 2; g = 6
  - E = (2 + 6) ≡ 8 mod 26
  - c -> i
- d = 3; h = 7
  - E = (3 + 7) ≡ 10 mod 26
  - d -> k

The resulting text is `egik`. For decryption, with the same key:

- e = 4; e = 4
  - D = (4 - 4) ≡ 0 mod 26
  - e -> a
- g = 6; f = 5
  - D = (6 - 5) ≡ 1 mod 26
  - g -> b
- i = 8; g = 6
  - D = (8 - 6) ≡ 2 mod 26
  - i -> c
- k = 10; h = 7
  - D = (10 - 7) ≡ 3 mod 26
  - k -> d

Which results in `abcd`.
