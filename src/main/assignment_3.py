#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 3b: Numerical methods for linear systems and matrix operations
"""
import numpy as np
from typing import Tuple, List

def gaussian_elimination(augmented_matrix: np.ndarray) -> np.ndarray:
    """
    Solves a system of linear equations using Gaussian elimination
    and backward substitution.
    
    Args:
        augmented_matrix: Matrix in augmented form [A|b]
    
    Returns:
        The solution vector x
    """
    n = augmented_matrix.shape[0]  # Number of equations/unknowns
    
    # Forward elimination
    for i in range(n):
        # Find pivot in column i, starting from row i
        pivot = augmented_matrix[i, i]
        
        # Make pivot 1
        augmented_matrix[i] = augmented_matrix[i] / pivot
        
        # Eliminate all other entries in column i
        for j in range(i + 1, n):
            factor = augmented_matrix[j, i]
            augmented_matrix[j] = augmented_matrix[j] - factor * augmented_matrix[i]
    
    # Backward substitution
    solution = np.zeros(n)
    for i in range(n-1, -1, -1):
        solution[i] = augmented_matrix[i, -1]
        for j in range(i+1, n):
            solution[i] -= augmented_matrix[i, j] * solution[j]
    
    return solution

def lu_factorization(matrix: np.ndarray) -> Tuple[np.ndarray, np.ndarray, float]:
    """
    Performs LU factorization on a square matrix.
    
    Args:
        matrix: Input square matrix
    
    Returns:
        A tuple containing:
        - L: Lower triangular matrix
        - U: Upper triangular matrix
        - determinant: Determinant of the matrix
    """
    n = matrix.shape[0]
    L = np.identity(n)
    U = matrix.copy().astype(float)
    
    for i in range(n):
        for j in range(i+1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j, i:] = U[j, i:] - factor * U[i, i:]
    
    # Calculate determinant as product of diagonal elements of U
    det = np.prod(np.diag(U))
    
    return L, U, det

def is_diagonally_dominant(matrix: np.ndarray) -> bool:
    """
    Determines if a square matrix is diagonally dominant.
    A matrix is diagonally dominant if for each row, the absolute value
    of the diagonal entry is greater than or equal to the sum of the
    absolute values of all other entries in that row.
    
    Args:
        matrix: Input square matrix
    
    Returns:
        True if the matrix is diagonally dominant, False otherwise
    """
    n = matrix.shape[0]
    
    for i in range(n):
        diagonal = abs(matrix[i, i])
        sum_of_others = sum(abs(matrix[i, j]) for j in range(n) if j != i)
        
        if diagonal < sum_of_others:
            return False
    
    return True

def is_positive_definite(matrix: np.ndarray) -> bool:
    """
    Determines if a square matrix is positive definite.
    A symmetric matrix is positive definite if all its eigenvalues are positive.
    
    Args:
        matrix: Input square matrix (assumed to be symmetric)
    
    Returns:
        True if the matrix is positive definite, False otherwise
    """
    try:
        # Check if all eigenvalues are positive
        eigenvalues = np.linalg.eigvals(matrix)
        return np.all(eigenvalues > 0)
    except:
        return False

def main():
    # Question 1: Gaussian elimination
    aug_matrix = np.array([
        [2, -1, 1, 6],
        [1, 3, 1, 0],
        [-1, 5, 4, -3]
    ], dtype=float)
    
    solution = gaussian_elimination(aug_matrix.copy())
    print(solution[0])  # Print first element of solution
    print(solution[1])  # Print second element of solution
    print(solution)     # Print entire solution
    
    # Question 2: LU Factorization
    matrix = np.array([
        [1, 1, 0, 3],
        [2, 1, -1, 1],
        [3, -1, -1, 2],
        [-1, 2, 3, -1]
    ], dtype=float)
    
    L, U, det = lu_factorization(matrix)
    print(det)  # Print determinant
    print(L)    # Print L matrix
    print(U)    # Print U matrix
    
    # Question 3: Determine if matrix is diagonally dominant
    matrix = np.array([
        [9, 0, 5, 2, 1],
        [3, 9, 1, 2, 1],
        [0, 1, 7, 2, 3],
        [4, 2, 3, 12, 2],
        [3, 2, 4, 0, 8]
    ], dtype=float)
    
    result = is_diagonally_dominant(matrix)
    print(result)
    
    # Question 4: Determine if matrix is positive definite
    matrix = np.array([
        [2, 2, 1],
        [2, 3, 0],
        [1, 0, 2]
    ], dtype=float)
    
    result = is_positive_definite(matrix)
    print(result)

if __name__ == "__main__":
    main()
