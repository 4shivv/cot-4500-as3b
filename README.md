# COT-4500 Assignment 3b

## Description

This assignment implements numerical methods for solving systems of linear equations and performing matrix operations. The assignment covers Chapters 5 and 6, focusing on elimination methods and matrix properties.

Key implementations include:
- Gaussian elimination with backward substitution
- LU Factorization
- Checking if a matrix is diagonally dominant 
- Checking if a matrix is positive definite

## Requirements

This project uses only NumPy as its external dependency. You can install it using the requirements.txt file:

```bash
pip install -r requirements.txt
```

## Directory Structure

```
cot-4500-as3b/
│
├── src/
│   ├── main/
│   │   ├── __init__.py
│   │   └── assignment_3.py
│   └── test/
│       ├── __init__.py
│       └── test_assignment_3.py
│
├── requirements.txt
└── README.md
```

## How to Run

### Running the main assignment

To run the main script from the command line:

```bash
python src/main/assignment_3.py
```

## Author

Shivaganesh Nagamandla