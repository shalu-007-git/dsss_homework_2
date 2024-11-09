import unittest
from math_quiz import select_integer, maths_operations, maths_result


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = select_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        expected_operators = ['+', '-', '*']
        for _ in range(100):
            operator = maths_operations()
            self.assertIn(operator, expected_operators, "Invalid operator returned by maths_operations")


    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (11, 4, '-', '11 - 4', 7),
                (5, 2, '*', '5 * 2', 10),
                (8, 1, '+', '8 + 1', 9)

            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = maths_result(num1, num2, operator)
                self.assertEqual(problem, expected_problem,
                                 f"Expected problem '{expected_problem}' but got '{problem}'")
                self.assertEqual(answer, expected_answer, f"Expected answer '{expected_answer}' but got '{answer}'")


if __name__ == "__main__":
    unittest.main()
