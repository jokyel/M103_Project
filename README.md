# M103 Project

This is the repository for our project in MATH 103, where we create a Python program for students to have hands-on experience on the following basic ciphers:
  - Caesar cipher
  - Affine cipher
  - Vigenère cipher

You can access the program [here](https://m103project-ciphers.streamlit.app)!

## Instruction Manual

The webpage has these elements:
  - A dropdown that includes the three ciphers (Caesar, Affine, Vigenère) the user may use;
  - A text field where the user can input a plaintext;
  - An option to either encrypt or decrypt the text; and
  - A button to process the text and encrypt/decrypt the plaintext with the set parameters.

Each dropdown option the user chooses will change the webpage's elements.
  - If the user chooses to do a Caesar cipher, the user can either input the "shift" integer, or use the increment buttons to the right of the text box to increase or decrease the shift integer by 1.
  - If the user chooses to do an Affine cipher, the user can input two shift integers, A and B.
      - A is a dropdown element, where the choices are integers coprime with 26.
      - B is a textbox element, where the user can either input an integer, or use the increment buttons, similar to the Caesar cipher's "shift" integer input.
  - If the user chooses to do a Vigenère cipher, the user is required to input a string key of at least length 2. Should the user not input a string key, it would return an error forcing the user to input one. Intrinsically, this is because the code would ultimately return an error regarding the divisibility of zero. Similarly, a key of only length 1 will just be equivalent to the Caesar cipher, with the "shift" integer being the alphabetical index of the letter in the key.

## Overview of the ciphers

Take note of the following:
  - Each letter in the alphabet has a unique index, from 0 to 25. A = 0, B = 1, C = 2, … Z = 25. For the purpose of simplifying the program, letter casing is negligible; A = a = 0.
  - "Plaintext" refers to the original text, while "ciphertext" refers to the encrypted text.
  - To avoid complications with indexing, the ciphers WILL IGNORE any non-alphabetical characters in the plaintext, ciphertext, and key, like numbers and special characters.
    - For example, if a person were to use a Caesar cipher with plaintext `a1b2c3`, and the "shift" integer is 3, the program will only return `d1e2f3`.

### Caesar cipher

Widely regarded as one of the most basic and historically significant ciphers, the Caesar cipher is a building block in classical cryptography. The key idea is that an encoded text is encrypted by having its characters "shifted" to the right by a number of letters in the alphabet. If the shift is to the left, the "shift" integer is negative.

For example, let's say we have a plaintext `abc`. The person encrypting can shift the letters by 3, so that it is encrypted as `def`.
The idea of the "shift" is to add the index of each character in the text by a specified number. In the plaintext `abc`:

  - a -> 0
  - b -> 1
  - c -> 2

Once shifted by 3, it then becomes:

  - a -> 0 + 3 = 3 -> d
  - b -> 1 + 3 = 4 -> e
  - c -> 2 + 3 = 5 -> f

The shift is of modulo 26. So a shift by 27, by modular arithmetic, is just a shift by 1 (27 ≡ 1 mod 26).

Deciphering a text using the Caesar cipher can be done by reverting the "shift". For example, with the ciphertext `def`, this can be shifted back by 3:

  - d -> 3 - 3 = 0 -> a
  - e -> 4 - 3 = 1 -> b
  - f -> 5 - 3 = 2 -> c

So the result is the plaintext `abc`.

### Affine cipher

Similar to the Caesar cipher, the Affine cipher shifts each letter's index by a specified amount, but utilizes multiplicative and additive shifting. The person encrypting uses two numbers, A and B, such that

  - E(x) = Ax + B mod 26
  - D(x) = A<sup>-1</sup>(x-B) mod 26

where x is the index of a character in the alphabet, and A<sup>-1</sup> is the modular inverse of A. Note that A must be coprime with 26 to allow the ciphering process to be reversible, since the modular inverse of A mod M only exists if A and M are coprime.

For example, we have a plaintext `abcde`. If A = 5 and B = 10, then

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

Note that the modular inverse of A = 5 is A<sup>-1</sup> = 21.

### Vigenère cipher

The Vigenère cipher, at its core, uses a key. However, the idea of it is that it is a combination of multiple Caesar ciphers. The person can input plaintext, and then input a key. The cipher itself will use the indeces of each letter in the key to shift each character of the text correspondingly. The formula is

E<sub>i</sub> = (T<sub>i</sub> + K<sub>i</sub>) mod 26

where T<sub>i</sub> is the index of the ith letter in the text, and K<sub>i</sub> is the index of the ith letter in the key, corresponding to the alphabet. Note that a = 0, b = 1, … z = 26. The resulting E<sub>i</sub> is the index of the ith letter of the ciphertext.

For decryption, the formula is

D<sub>i</sub> = (C<sub>i</sub> - K<sub>i</sub>) mod 26

where C<sub>i</sub> is the index of the ith letter in the encrypted text, and K<sub>i</sub> is the index of the ith letter in the key, corresponding to the alphabet. The resulting D<sub>i</sub> is the plaintext.

For example, with plaintext `abcd` and key `efgh`:

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

The resulting ciphertext is `egik`. For decryption, with the same key:

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

Which results in the plaintext `abcd`.

Note that the key's length does not necessarily have to be equal to the plaintext's length. For example, if the plaintext is `abcd` and the key is `ab`, then the cipher will use `abab` as the key. Similarly, if the plaintext is `abcd` and the key is `efghi`, then the cipher will use `efgh` as the key.
