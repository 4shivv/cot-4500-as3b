#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test file for Assignment 3b
"""
import unittest
import numpy as np
import sys
import os

# Add the src directory to the path so we can import the main module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main.assignment_3 import (
    gaussian_elimination,
    lu_factorization,
    is_diagonally_dominant,
    is_positive_definite
)

class TestAssignment3(unittest.TestCase):
    
    def test_gaussian_elimination(self):
        aug_matrix = np.array([
            [2, -1, 1, 6],
            [1, 3, 1, 0],
            [-1, 5, 4, -3]
        ], dtype=float)
        
        solution = gaussian_elimination(aug_matrix.copy())
        
        # Check the expected output from the assignment
        expected_first = 2
        expected_second = -1
        self.assertAlmostEqual(solution[0], expected_first)
        self.assertAlmostEqual(solution[1], expected_second)
        self.assertEqual(len(solution), 3)
    
    def test_lu_factorization(self):
        matrix = np.array([
            [1, 1, 0, 3],
            [2, 1, -1, 1],
            [3, -1, -1, 2],
            [-1, 2, 3, -1]
        ], dtype=float)
        
        L, U, det = lu_factorization(matrix)
        
        # Check determinant
        expected_det = 39
        self.assertAlmostEqual(det, expected_det, places=10)
        
        # Check dimensions
        self.assertEqual(L.shape, (4, 4))
        self.assertEqual(U.shape, (4, 4))
        
        # Check L is lower triangular
        for i in range(4):
            for j in range(i+1, 4):
                self.assertEqual(L[i, j], 0)
        
        # Check U is upper triangular
        for i in range(1, 4):
            for j in range(i):
                self.assertAlmostEqual(U[i, j], 0)
    
    def test_diagonally_dominant(self):
        matrix = np.array([
            [9, 0, 5, 2, 1],
            [3, 9, 1, 2, 1],
            [0, 1, 7, 2, 3],
            [4, 2, 3, 12, 2],
            [3, 2, 4, 0, 8]
        ], dtype=float)
        
        result = is_diagonally_dominant(matrix)
        self.assertTrue(result)
        
        # Non-diagonally dominant matrix
        matrix = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], dtype=float)
        
        result = is_diagonally_dominant(matrix)
        self.assertFalse(result)
    
    def test_positive_definite(self):
        matrix = np.array([
            [2, 2, 1],
            [2, 3, 0],
            [1, 0, 2]
        ], dtype=float)
        
        result = is_positive_definite(matrix)
        self.assertTrue(result)
        
        # Non-positive definite matrix
        matrix = np.array([
            [1, 2, 3],
            [2, 0, 4],
            [3, 4, -1]
        ], dtype=float)
        
        result = is_positive_definite(matrix)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
