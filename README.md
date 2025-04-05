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

### Running the tests

To run the tests:

```bash
python -m unittest src/test/test_assignment_3.py
```

## Expected Output

When running the main script, you should see the following output:

```
2.0
-1.0
[ 2. -1.  1.]
38.99999999999999
[[1. 0. 0. 0.]
 [2. 1. 0. 0.]
 [3. 4. 1. 0.]
 [-1. -3. 0. 1.]]
[[1.         1.         0.         3.        ]
 [0.        -1.        -1.        -5.        ]
 [0.         0.         3.        13.        ]
 [0.         0.         0.       -13.        ]]
True
True
```

This matches the expected output from the assignment description.

## Author

Shivaganesh Nagamandla