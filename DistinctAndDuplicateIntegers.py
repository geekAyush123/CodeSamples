# Function that you will complete
from typing import List
def AddDistinctDuplicate(a, b, c, d):
    elements = [a, b, c, d]
    frequency = {}

    # Store element frequencies in the dictionary
    for element in elements:
        frequency[element] = frequency.get(element, 0) + 1

    distinct_sum = 0
    duplicate = 0

    # Calculate sum of distinct numbers and find the duplicate
    for entry in frequency.items():
        if entry[1] == 1:
            distinct_sum += entry[0]
        else:
            duplicate = entry[0]

    return distinct_sum - duplicate
# Test cases to validate the implementation
def test_AddDistinctDuplicate():
    # Test case 1
    a, b, c, d = 5, 4, 4, 9
    expected_output = 10
    result = AddDistinctDuplicate(a, b, c, d)
    print(f"Test 1 - Expected: {expected_output}, Got: {result}")
    
    # Test case 2
    a, b, c, d = -1, 3, 8, -6
    expected_output = 4
    result = AddDistinctDuplicate(a, b, c, d)
    print(f"Test 2 - Expected: {expected_output}, Got: {result}")
    
    # Test case 3
    a, b, c, d = 2, 2, 2, 2
    expected_output = 0
    result = AddDistinctDuplicate(a, b, c, d)
    print(f"Test 3 - Expected: {expected_output}, Got: {result}")
    
    # Test case 4
    a, b, c, d = 10, 10, 5, 5
    expected_output = 0
    result = AddDistinctDuplicate(a, b, c, d)
    print(f"Test 4 - Expected: {expected_output}, Got: {result}")
    
    # Test case 5
    a, b, c, d = 1, 2, 3, 4
    expected_output = 10
    result = AddDistinctDuplicate(a, b, c, d)
    print(f"Test 5 - Expected: {expected_output}, Got: {result}")

# Run the test cases
test_AddDistinctDuplicate()
