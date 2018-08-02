import unittest
from unittest import TestCase
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from src.fibo import fibo
from src.facts import calc
# global table
class TestFibo(TestCase):
    def setUp(self):
        self.table = {}
    def correct_fibo(self, a, table):
        if a == 0:
            return 0
        if a == 1:
            return 1
        if a == 2:
            return 1
        if a in table:
            return table[a]
        else:
            table[a] = self.correct_fibo(a - 1, table) + self.correct_fibo(a - 2, table)
            return table[a]
    def test_correct_for_1(self):
        table = {}
        self.assertEqual(self.correct_fibo(1, table), fibo(1))
    def test_correct_4(self):
        table = {}
        self.assertEqual(self.correct_fibo(4, table), fibo(4))
    def test_factorial_of_6(self):
        self.assertEqual(720, calc(6))
