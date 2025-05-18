# 🧮 Python Number Analyzer & Calculator

A command-line Python program that:

1. Takes a list of numbers from the user and performs statistical and bitwise operations
2. Accepts two numbers and performs a selected arithmetic or math operation
3. Generates a random percentage just for fun!

---

## 📦 Features

### 1. 🔢 List Number Analyzer
- Accepts comma-separated numbers
- Converts inputs to integers and stores in a NumPy array
- Outputs:
  - Original list
  - Sum, average, max, min
  - Bitwise OR, AND, XOR of all numbers

### 2. 🧮 Two-Number Calculator
- Accepts two numbers and an operation
- Supported operations:
  - Arithmetic: `+`, `-`, `*`, `/`, `%`
  - Math functions: `pow`, `abs`, `floor`, `ceil`
  - Bitwise AND (only if both numbers are integers)

### 3. 🎲 Random Percentage Generator
- Generates a random float between `0.0` and `1.0`
- Prints its value and corresponding percentage

---

## 📋 Requirements

- Python 3.6+
- NumPy

Install NumPy if you don’t have it:
```bash
pip install numpy
