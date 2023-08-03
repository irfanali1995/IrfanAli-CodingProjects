# Readability

![CS50x](https://img.shields.io/badge/CS50x-Readability-blue)

This repository contains my solution to the "Readability" problem from Harvard's CS50x course. The program is written in C and calculates the readability grade level of a given text using the Coleman-Liau index formula.

## Problem Description

The "Readability" problem requires writing a C program that takes input text and calculates the readability grade level. The program calculates the average number of letters per 100 words and the average number of sentences per 100 words. It then uses the Coleman-Liau index formula to determine the readability grade level of the text.

The Coleman-Liau index formula is given by:

index = 0.0588 * L - 0.296 * S - 15.8

Where L is the average number of letters per 100 words, S is the average number of sentences per 100 words.

The program should output the grade level as an integer, which represents the U.S. grade level equivalent to the calculated readability.

## Acknowledgments

The "Readability" problem is part of Harvard's CS50x course. 
