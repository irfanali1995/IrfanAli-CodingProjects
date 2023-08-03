# Caesar Cipher Encryption and Decryption Program

This program, named "caesar", is an implementation of Caesar's cipher encryption algorithm. It was created as part of the CS50x class, a course offered by Harvard University. The program is designed to encrypt messages using Caesar's cipher and can also be used to decrypt the encrypted messages.


## Introduction

Caesar's cipher is a simple encryption technique where each letter in the plaintext is shifted a certain number of places down the alphabet. This shift value is referred to as "key" (k) in the program. The program accepts a single command-line argument, a non-negative integer "k," which specifies the number of positions each letter will be shifted for encryption or decryption.

## Usage

To use the "caesar" program, follow these steps:

1. Clone this repository to your local machine or download the "caesar.c" file.
2. Compile the program using a C compiler.
3. Run the compiled program from the command line, providing a non-negative integer "k" as a command-line argument.
4. The program will prompt you to enter the plaintext message.
5. The program will display the encrypted ciphertext, preserving the case of the letters and leaving non-alphabetical characters unchanged.

## How It Works

The program takes a non-negative integer "k" as a command-line argument, which represents the encryption key. The value of "k" determines how many positions each alphabetical character should be shifted for encryption or decryption.

For encryption, each alphabetical character in the plaintext is rotated "k" positions forward in the alphabet. The case (uppercase/lowercase) of the letters is preserved, and non-alphabetical characters remain unchanged.

For decryption, the same process is applied, but this time the characters are rotated "k" positions backward in the alphabet, effectively undoing the encryption.

## Examples

Example 1: Encryption
Command:
```bash
./caesar 3
plaintext: Hello, World!
ciphertext: Khoor, Zruog!
```
Example 2: Decryption
command:
```bash
./decrypt_caesar 3
ciphertext: Khoor, Zruog!
decrypt: Hello, World!
```
Note : This project was done as part of Harvard CS50x course , all license belong to them. 












