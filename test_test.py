"""
Comprehensive unit tests for test.py functions.
Tests cover happy paths, edge cases, and failure conditions.
"""
import unittest
import sys
from io import StringIO

# Import functions from test.py
from test import (
    calculate_sum,
    calculate_average_v2,
    safe_average,
    print_stats,
    debug_print,
    calculate_average,
    print_average
)


class TestCalculateSum(unittest.TestCase):
    """Test suite for calculate_sum function."""

    def test_sum_positive_integers(self):
        """Test sum with positive integers."""
        result = calculate_sum([1, 2, 3, 4, 5])
        self.assertEqual(result, 15)

    def test_sum_negative_integers(self):
        """Test sum with negative integers."""
        result = calculate_sum([-1, -2, -3])
        self.assertEqual(result, -6)

    def test_sum_mixed_integers(self):
        """Test sum with mixed positive and negative integers."""
        result = calculate_sum([10, -5, 3, -8, 20])
        self.assertEqual(result, 20)

    def test_sum_single_element(self):
        """Test sum with single element list."""
        result = calculate_sum([42])
        self.assertEqual(result, 42)

    def test_sum_empty_list(self):
        """Test sum with empty list."""
        result = calculate_sum([])
        self.assertEqual(result, 0)

    def test_sum_zeros(self):
        """Test sum with all zeros."""
        result = calculate_sum([0, 0, 0, 0])
        self.assertEqual(result, 0)

    def test_sum_floats(self):
        """Test sum with floating point numbers."""
        result = calculate_sum([1.5, 2.5, 3.0])
        self.assertAlmostEqual(result, 7.0)

    def test_sum_large_numbers(self):
        """Test sum with large numbers."""
        result = calculate_sum([1000000, 2000000, 3000000])
        self.assertEqual(result, 6000000)

    def test_sum_with_none_raises_error(self):
        """Test that sum with None raises TypeError."""
        with self.assertRaises(TypeError):
            calculate_sum([1, 2, None, 4])

    def test_sum_with_string_raises_error(self):
        """Test that sum with string raises TypeError."""
        with self.assertRaises(TypeError):
            calculate_sum([1, 2, "3", 4])

    def test_sum_very_large_list(self):
        """Test sum with very large list."""
        large_list = list(range(1, 1001))
        result = calculate_sum(large_list)
        self.assertEqual(result, 500500)

    def test_sum_alternating_signs(self):
        """Test sum with alternating positive/negative."""
        result = calculate_sum([1, -1, 2, -2, 3, -3])
        self.assertEqual(result, 0)


class TestCalculateAverageV2(unittest.TestCase):
    """Test suite for calculate_average_v2 function."""

    def test_average_positive_integers(self):
        """Test average with positive integers."""
        result = calculate_average_v2([10, 20, 30])
        self.assertEqual(result, 20.0)

    def test_average_negative_integers(self):
        """Test average with negative integers."""
        result = calculate_average_v2([-10, -20, -30])
        self.assertEqual(result, -20.0)

    def test_average_mixed_numbers(self):
        """Test average with mixed positive and negative numbers."""
        result = calculate_average_v2([10, -10, 20, -20])
        self.assertEqual(result, 0.0)

    def test_average_single_element(self):
        """Test average with single element."""
        result = calculate_average_v2([42])
        self.assertEqual(result, 42.0)

    def test_average_floats(self):
        """Test average with floating point numbers."""
        result = calculate_average_v2([1.5, 2.5, 3.5, 4.5])
        self.assertEqual(result, 3.0)

    def test_average_empty_list_raises_error(self):
        """Test that average of empty list raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            calculate_average_v2([])

    def test_average_with_none_raises_error(self):
        """Test that average with None raises TypeError."""
        with self.assertRaises(TypeError):
            calculate_average_v2([1, 2, None, 4])

    def test_average_large_numbers(self):
        """Test average with large numbers."""
        result = calculate_average_v2([1000000, 2000000, 3000000])
        self.assertEqual(result, 2000000.0)

    def test_average_all_zeros(self):
        """Test average with all zeros."""
        result = calculate_average_v2([0, 0, 0])
        self.assertEqual(result, 0.0)

    def test_average_precision(self):
        """Test average with numbers requiring precision."""
        result = calculate_average_v2([1, 2, 3])
        self.assertAlmostEqual(result, 2.0)

    def test_average_repeated_values(self):
        """Test average with repeated values."""
        result = calculate_average_v2([5, 5, 5, 5, 5])
        self.assertEqual(result, 5.0)

    def test_average_two_elements(self):
        """Test average with two elements."""
        result = calculate_average_v2([10, 20])
        self.assertEqual(result, 15.0)


class TestSafeAverage(unittest.TestCase):
    """Test suite for safe_average function."""

    def test_safe_average_valid_list(self):
        """Test safe_average with valid number list."""
        result = safe_average([10, 20, 30])
        self.assertEqual(result, 20.0)

    def test_safe_average_empty_list_returns_zero(self):
        """Test that safe_average returns 0 for empty list."""
        result = safe_average([])
        self.assertEqual(result, 0)

    def test_safe_average_with_none_returns_zero(self):
        """Test that safe_average returns 0 when list contains None."""
        result = safe_average([1, 2, None, 4])
        self.assertEqual(result, 0)

    def test_safe_average_single_element(self):
        """Test safe_average with single element."""
        result = safe_average([100])
        self.assertEqual(result, 100.0)

    def test_safe_average_negative_numbers(self):
        """Test safe_average with negative numbers."""
        result = safe_average([-5, -10, -15])
        self.assertEqual(result, -10.0)

    def test_safe_average_mixed_numbers(self):
        """Test safe_average with mixed numbers."""
        result = safe_average([100, -50, 25, -25])
        self.assertEqual(result, 12.5)

    def test_safe_average_with_strings_returns_zero(self):
        """Test that safe_average returns 0 when list contains strings."""
        result = safe_average([1, 2, "three", 4])
        self.assertEqual(result, 0)

    def test_safe_average_with_non_iterable_returns_zero(self):
        """Test that safe_average returns 0 for non-iterable input."""
        result = safe_average(42)
        self.assertEqual(result, 0)

    def test_safe_average_floats(self):
        """Test safe_average with floating point numbers."""
        result = safe_average([1.1, 2.2, 3.3])
        self.assertAlmostEqual(result, 2.2)

    def test_safe_average_large_list(self):
        """Test safe_average with large list."""
        numbers = list(range(1, 101))
        result = safe_average(numbers)
        self.assertEqual(result, 50.5)

    def test_safe_average_with_dict_returns_zero(self):
        """Test safe_average with dictionary returns 0."""
        result = safe_average({"key": "value"})
        self.assertEqual(result, 0)

    def test_safe_average_with_string_returns_zero(self):
        """Test safe_average with string returns 0."""
        result = safe_average("not a list")
        self.assertEqual(result, 0)


class TestPrintStats(unittest.TestCase):
    """Test suite for print_stats function."""

    def test_print_stats_normal_list(self):
        """Test print_stats with normal number list."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_stats([1, 2, 3, 4, 5])
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Sum: 15", output)
        self.assertIn("Average: 3.0", output)
        self.assertIn("Count: 5", output)
        self.assertIn("Max: 5", output)
        self.assertIn("Min: 1", output)

    def test_print_stats_single_element(self):
        """Test print_stats with single element."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_stats([42])
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Sum: 42", output)
        self.assertIn("Average: 42.0", output)
        self.assertIn("Count: 1", output)
        self.assertIn("Max: 42", output)
        self.assertIn("Min: 42", output)

    def test_print_stats_negative_numbers(self):
        """Test print_stats with negative numbers."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_stats([-10, -5, -1])
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Sum: -16", output)
        self.assertIn("Min: -10", output)
        self.assertIn("Max: -1", output)

    def test_print_stats_mixed_numbers(self):
        """Test print_stats with mixed positive and negative numbers."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_stats([10, -5, 0, 15, -10])
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Sum: 10", output)
        self.assertIn("Count: 5", output)
        self.assertIn("Max: 15", output)
        self.assertIn("Min: -10", output)

    def test_print_stats_floats(self):
        """Test print_stats with floating point numbers."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_stats([1.5, 2.5, 3.5])
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Sum: 7.5", output)
        self.assertIn("Max: 3.5", output)
        self.assertIn("Min: 1.5", output)

    def test_print_stats_with_none_handles_error(self):
        """Test print_stats behavior when list contains None."""
        # This will cause errors in max/min due to None
        with self.assertRaises(TypeError):
            print_stats([1, 2, None, 4])

    def test_print_stats_empty_list_raises_error(self):
        """Test print_stats with empty list raises ValueError."""
        with self.assertRaises(ValueError):
            print_stats([])

    def test_print_stats_all_zeros(self):
        """Test print_stats with all zeros."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_stats([0, 0, 0])
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Sum: 0", output)
        self.assertIn("Average: 0.0", output)
        self.assertIn("Max: 0", output)
        self.assertIn("Min: 0", output)

    def test_print_stats_large_numbers(self):
        """Test print_stats with large numbers."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_stats([1000000, 2000000, 3000000])
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Sum: 6000000", output)
        self.assertIn("Max: 3000000", output)
        self.assertIn("Min: 1000000", output)

    def test_print_stats_output_format(self):
        """Test that print_stats outputs in correct format."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_stats([5, 10, 15])
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        lines = output.strip().split('\n')
        
        self.assertEqual(len(lines), 5)
        self.assertTrue(lines[0].startswith("Sum:"))
        self.assertTrue(lines[1].startswith("Average:"))
        self.assertTrue(lines[2].startswith("Count:"))
        self.assertTrue(lines[3].startswith("Max:"))
        self.assertTrue(lines[4].startswith("Min:"))

    def test_print_stats_two_elements(self):
        """Test print_stats with two elements."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_stats([100, 200])
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Sum: 300", output)
        self.assertIn("Average: 150.0", output)
        self.assertIn("Count: 2", output)


class TestDebugPrint(unittest.TestCase):
    """Test suite for debug_print function."""

    def test_debug_print_with_none(self):
        """Test debug_print with None value."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        debug_print(None)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertEqual(output.strip(), "No data")

    def test_debug_print_with_string(self):
        """Test debug_print with string data."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        debug_print("Hello")
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertEqual(output.strip(), "Data: Hello")

    def test_debug_print_with_integer(self):
        """Test debug_print with integer data."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        debug_print(42)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertEqual(output.strip(), "Data: 42")

    def test_debug_print_with_zero(self):
        """Test debug_print with zero (falsy but not None)."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        debug_print(0)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertEqual(output.strip(), "Data: 0")

    def test_debug_print_with_empty_string(self):
        """Test debug_print with empty string (falsy but not None)."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        debug_print("")
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertEqual(output.strip(), "Data: ")

    def test_debug_print_with_list(self):
        """Test debug_print with list data."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        debug_print([1, 2, 3])
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertEqual(output.strip(), "Data: [1, 2, 3]")

    def test_debug_print_with_dict(self):
        """Test debug_print with dictionary data."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        debug_print({"key": "value"})
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertEqual(output.strip(), "Data: {'key': 'value'}")

    def test_debug_print_with_boolean_true(self):
        """Test debug_print with boolean True."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        debug_print(True)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertEqual(output.strip(), "Data: True")

    def test_debug_print_with_boolean_false(self):
        """Test debug_print with boolean False (falsy but not None)."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        debug_print(False)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertEqual(output.strip(), "Data: False")

    def test_debug_print_with_float(self):
        """Test debug_print with float data."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        debug_print(3.14)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertEqual(output.strip(), "Data: 3.14")

    def test_debug_print_with_empty_list(self):
        """Test debug_print with empty list (falsy but not None)."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        debug_print([])
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertEqual(output.strip(), "Data: []")

    def test_debug_print_with_empty_dict(self):
        """Test debug_print with empty dict (falsy but not None)."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        debug_print({})
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertEqual(output.strip(), "Data: {}")

    def test_debug_print_with_negative_number(self):
        """Test debug_print with negative number."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        debug_print(-999)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertEqual(output.strip(), "Data: -999")

    def test_debug_print_with_tuple(self):
        """Test debug_print with tuple data."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        debug_print((1, 2, 3))
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertEqual(output.strip(), "Data: (1, 2, 3)")



class TestCalculateAverage(unittest.TestCase):
    """Test suite for calculate_average function (original function)."""

    def test_calculate_average_basic(self):
        """Test basic average calculation."""
        result = calculate_average([10, 20, 30])
        self.assertEqual(result, 20.0)

    def test_calculate_average_single_element(self):
        """Test average with single element."""
        result = calculate_average([42])
        self.assertEqual(result, 42.0)

    def test_calculate_average_negative_numbers(self):
        """Test average with negative numbers."""
        result = calculate_average([-10, -20, -30])
        self.assertEqual(result, -20.0)

    def test_calculate_average_empty_list_raises_error(self):
        """Test that average of empty list raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            calculate_average([])

    def test_calculate_average_with_none_raises_error(self):
        """Test that average with None raises TypeError."""
        with self.assertRaises(TypeError):
            calculate_average([10, 20, None, 40])

    def test_calculate_average_floats(self):
        """Test average with floating point numbers."""
        result = calculate_average([1.5, 2.5, 3.5])
        self.assertAlmostEqual(result, 2.5)

    def test_calculate_average_mixed_numbers(self):
        """Test average with mixed positive and negative."""
        result = calculate_average([100, -50, 50, -100])
        self.assertEqual(result, 0.0)

    def test_calculate_average_all_same_values(self):
        """Test average when all values are the same."""
        result = calculate_average([7, 7, 7, 7])
        self.assertEqual(result, 7.0)

    def test_calculate_average_two_values(self):
        """Test average with two values."""
        result = calculate_average([5, 15])
        self.assertEqual(result, 10.0)


class TestPrintAverage(unittest.TestCase):
    """Test suite for print_average function."""

    def test_print_average_valid_numbers(self):
        """Test print_average with valid numbers - has string concatenation bug."""
        # This will raise TypeError due to string + float concatenation issue
        with self.assertRaises(TypeError):
            print_average([10, 20, 30])

    def test_print_average_with_none_raises_error(self):
        """Test that print_average with None raises TypeError."""
        with self.assertRaises(TypeError):
            print_average([10, 20, None, 40])

    def test_print_average_empty_list_raises_error(self):
        """Test that print_average with empty list raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            print_average([])

    def test_print_average_single_value(self):
        """Test print_average with single value - has string concatenation bug."""
        with self.assertRaises(TypeError):
            print_average([100])


class TestIntegration(unittest.TestCase):
    """Integration tests for related functions."""

    def test_calculate_sum_and_average_consistency(self):
        """Test that sum and average are mathematically consistent."""
        numbers = [10, 20, 30, 40, 50]
        total = calculate_sum(numbers)
        average = calculate_average_v2(numbers)
        
        expected_average = total / len(numbers)
        self.assertEqual(average, expected_average)

    def test_safe_average_wraps_calculate_average_v2(self):
        """Test that safe_average properly wraps calculate_average_v2."""
        numbers = [5, 10, 15, 20]
        
        normal_result = calculate_average_v2(numbers)
        safe_result = safe_average(numbers)
        
        self.assertEqual(normal_result, safe_result)

    def test_safe_average_catches_exceptions(self):
        """Test that safe_average catches exceptions from calculate_average_v2."""
        # Empty list causes ZeroDivisionError in calculate_average_v2
        result = safe_average([])
        self.assertEqual(result, 0)

    def test_print_stats_uses_other_functions(self):
        """Test that print_stats integrates with calculate_sum and safe_average."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        numbers = [10, 20, 30]
        print_stats(numbers)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        expected_sum = calculate_sum(numbers)
        expected_avg = safe_average(numbers)
        
        self.assertIn(f"Sum: {expected_sum}", output)
        self.assertIn(f"Average: {expected_avg}", output)

    def test_all_functions_with_same_input(self):
        """Test multiple functions with the same input for consistency."""
        numbers = [1, 2, 3, 4, 5]
        
        total = calculate_sum(numbers)
        avg_v2 = calculate_average_v2(numbers)
        safe_avg = safe_average(numbers)
        
        self.assertEqual(total, 15)
        self.assertEqual(avg_v2, 3.0)
        self.assertEqual(safe_avg, 3.0)
        self.assertEqual(avg_v2, safe_avg)

    def test_calculate_average_vs_calculate_average_v2(self):
        """Test that both average functions produce same results."""
        numbers = [5, 10, 15, 20, 25]
        
        result1 = calculate_average(numbers)
        result2 = calculate_average_v2(numbers)
        
        self.assertEqual(result1, result2)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""

    def test_very_large_list(self):
        """Test functions with very large lists."""
        large_list = list(range(1, 10001))
        
        total = calculate_sum(large_list)
        self.assertEqual(total, 50005000)
        
        average = calculate_average_v2(large_list)
        self.assertEqual(average, 5000.5)

    def test_very_small_numbers(self):
        """Test functions with very small decimal numbers."""
        small_numbers = [0.0001, 0.0002, 0.0003]
        
        total = calculate_sum(small_numbers)
        self.assertAlmostEqual(total, 0.0006, places=4)
        
        average = safe_average(small_numbers)
        self.assertAlmostEqual(average, 0.0002, places=4)

    def test_repeated_values(self):
        """Test functions with repeated values."""
        repeated = [5, 5, 5, 5, 5]
        
        total = calculate_sum(repeated)
        self.assertEqual(total, 25)
        
        average = calculate_average_v2(repeated)
        self.assertEqual(average, 5.0)

    def test_alternating_signs(self):
        """Test with alternating positive and negative numbers."""
        alternating = [1, -1, 2, -2, 3, -3]
        
        total = calculate_sum(alternating)
        self.assertEqual(total, 0)
        
        average = calculate_average_v2(alternating)
        self.assertEqual(average, 0.0)

    def test_single_large_value_with_small_values(self):
        """Test average with one large value and many small values."""
        numbers = [1000000] + [1] * 999
        
        average = calculate_average_v2(numbers)
        self.assertAlmostEqual(average, 1999.0, places=1)

    def test_precision_with_division(self):
        """Test precision issues with division."""
        numbers = [1, 2, 3]
        average = calculate_average_v2(numbers)
        
        # Should be 2.0
        self.assertAlmostEqual(average, 2.0)

    def test_negative_zero(self):
        """Test behavior with negative zero."""
        numbers = [-0.0, 0.0, 0.0]
        total = calculate_sum(numbers)
        
        self.assertEqual(total, 0.0)

    def test_infinity_handling(self):
        """Test behavior with infinity values."""
        with self.assertRaises(OverflowError):
            # Python will handle this, but let's test extreme values
            calculate_sum([10**308, 10**308])


if __name__ == '__main__':
    unittest.main(verbosity=2)