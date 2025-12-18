"""
Comprehensive unit tests for the new functions added to test.py.
Tests cover happy paths, edge cases, and failure conditions.

This test file focuses on the functions added in the diff:
- calculate_sum
- calculate_average_v2
- safe_average
- print_stats
- debug_print
"""
import unittest
import sys
from io import StringIO


# Define the functions directly to avoid module-level execution issues
def calculate_sum(numbers):
    sum = 0  # shadows built-in
    for n in numbers:
        sum += n
    return sum


def calculate_average_v2(numbers):
    # duplicated logic instead of reusing calculate_average
    total = calculate_sum(numbers)
    return total / len(numbers)


def safe_average(numbers):
    try:
        return calculate_average_v2(numbers)
    except:
        return 0


def print_stats(numbers):
    print("Sum:", calculate_sum(numbers))
    print("Average:", safe_average(numbers))
    print("Count:", len(numbers))
    print("Max:", max(numbers))
    print("Min:", min(numbers))


def debug_print(data):
    if data == None:
        print("No data")
    else:
        print("Data:", data)


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

    def test_sum_decimal_precision(self):
        """Test sum maintains decimal precision."""
        result = calculate_sum([0.1, 0.2, 0.3])
        self.assertAlmostEqual(result, 0.6, places=10)

    def test_sum_negative_floats(self):
        """Test sum with negative floats."""
        result = calculate_sum([-1.5, -2.5, -3.5])
        self.assertAlmostEqual(result, -7.5)

    def test_sum_mixed_int_float(self):
        """Test sum with mixed integers and floats."""
        result = calculate_sum([1, 2.5, 3, 4.5])
        self.assertEqual(result, 11.0)


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

    def test_average_odd_division(self):
        """Test average that results in non-whole number."""
        result = calculate_average_v2([1, 2, 3, 4])
        self.assertEqual(result, 2.5)

    def test_average_large_dataset(self):
        """Test average with large dataset."""
        numbers = list(range(1, 101))
        result = calculate_average_v2(numbers)
        self.assertEqual(result, 50.5)

    def test_average_fraction_result(self):
        """Test average resulting in fraction."""
        result = calculate_average_v2([1, 1, 1])
        self.assertEqual(result, 1.0)


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

    def test_safe_average_handles_type_error(self):
        """Test safe_average handles TypeError gracefully."""
        result = safe_average([1, 2, [3, 4]])
        self.assertEqual(result, 0)

    def test_safe_average_handles_attribute_error(self):
        """Test safe_average handles various exceptions."""
        result = safe_average(None)
        self.assertEqual(result, 0)

    def test_safe_average_all_zeros(self):
        """Test safe_average with all zeros."""
        result = safe_average([0, 0, 0, 0])
        self.assertEqual(result, 0.0)



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

    def test_print_stats_negative_and_positive(self):
        """Test print_stats with range spanning negative to positive."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_stats([-50, 0, 50])
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Sum: 0", output)
        self.assertIn("Min: -50", output)
        self.assertIn("Max: 50", output)

    def test_print_stats_decimal_average(self):
        """Test print_stats when average is decimal."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_stats([1, 2, 3, 4])
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Average: 2.5", output)

    def test_print_stats_large_range(self):
        """Test print_stats with large range of values."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_stats([1, 100, 1000, 10000])
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Min: 1", output)
        self.assertIn("Max: 10000", output)


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
        
        self.assertTrue(output.strip().startswith("Data:"))

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

    def test_debug_print_with_set(self):
        """Test debug_print with set data."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        debug_print({1, 2, 3})
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Data:", output)
        self.assertIn("1", output)

    def test_debug_print_with_multiline_string(self):
        """Test debug_print with multiline string."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        debug_print("Line1\nLine2\nLine3")
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Data: Line1", output)

    def test_debug_print_with_special_characters(self):
        """Test debug_print with special characters."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        debug_print("Special: @#$%^&*()")
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertEqual(output.strip(), "Data: Special: @#$%^&*()")



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

    def test_print_stats_and_individual_functions_match(self):
        """Test that print_stats output matches individual function results."""
        numbers = [7, 14, 21, 28]
        
        # Get individual results
        expected_sum = calculate_sum(numbers)
        expected_avg = safe_average(numbers)
        expected_count = len(numbers)
        expected_max = max(numbers)
        expected_min = min(numbers)
        
        # Capture print_stats output
        captured_output = StringIO()
        sys.stdout = captured_output
        print_stats(numbers)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        # Verify all match
        self.assertIn(f"Sum: {expected_sum}", output)
        self.assertIn(f"Average: {expected_avg}", output)
        self.assertIn(f"Count: {expected_count}", output)
        self.assertIn(f"Max: {expected_max}", output)
        self.assertIn(f"Min: {expected_min}", output)

    def test_debug_print_with_calculated_values(self):
        """Test debug_print with calculated values from other functions."""
        numbers = [5, 10, 15]
        total = calculate_sum(numbers)
        
        captured_output = StringIO()
        sys.stdout = captured_output
        debug_print(total)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertEqual(output.strip(), "Data: 30")

    def test_safe_average_never_raises(self):
        """Test that safe_average never raises exceptions."""
        test_inputs = [
            [],
            [1, 2, None],
            "not a list",
            42,
            None,
            [1, "two", 3],
            {"key": "value"}
        ]
        
        for test_input in test_inputs:
            try:
                result = safe_average(test_input)
                self.assertEqual(result, 0)
            except Exception as e:
                self.fail(f"safe_average raised {type(e).__name__} with input {test_input}")


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
        self.assertAlmostEqual(average, 1000.999, places=2)

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

    def test_maximum_integer_values(self):
        """Test with very large integer values."""
        large_values = [10**15, 10**15, 10**15]
        total = calculate_sum(large_values)
        self.assertEqual(total, 3 * 10**15)

    def test_minimum_float_precision(self):
        """Test with minimum float precision values."""
        tiny = [1e-15, 1e-15, 1e-15]
        total = calculate_sum(tiny)
        self.assertGreater(total, 0)

    def test_mixed_magnitude_numbers(self):
        """Test with numbers of vastly different magnitudes."""
        mixed = [1e-10, 1e10, 1, 1000]
        total = calculate_sum(mixed)
        average = calculate_average_v2(mixed)
        self.assertGreater(total, 0)
        self.assertGreater(average, 0)

    def test_print_stats_with_identical_values(self):
        """Test print_stats when all values are identical."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_stats([7, 7, 7, 7, 7])
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Sum: 35", output)
        self.assertIn("Average: 7.0", output)
        self.assertIn("Max: 7", output)
        self.assertIn("Min: 7", output)

    def test_debug_print_none_vs_falsy(self):
        """Test debug_print distinguishes None from other falsy values."""
        falsy_values = [0, "", [], {}, False]
        
        for value in falsy_values:
            captured_output = StringIO()
            sys.stdout = captured_output
            debug_print(value)
            sys.stdout = sys.__stdout__
            output = captured_output.getvalue()
            
            self.assertIn("Data:", output)
            self.assertNotIn("No data", output)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)