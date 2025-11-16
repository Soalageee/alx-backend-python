# 0x03 – Unittests and Integration Tests  

---

## Task 0: Parameterize a Unit Test

### Overview
This task focuses on writing a **unit test** for the `access_nested_map` function located in `utils.py`.  
The goal is to ensure that the function correctly accesses values in nested dictionaries using a sequence of keys, and to practice **parameterizing tests** with multiple inputs.

### Function Being Tested
**`access_nested_map(nested_map: Mapping, path: Sequence) -> Any`**

- **Parameters:**
  - `nested_map`: A dictionary or nested dictionary
  - `path`: A sequence (list or tuple) of keys
- **Returns:** The value located at the specified key path
- **Example:**
```python
nested_map = {"a": {"b": {"c": 1}}}
access_nested_map(nested_map, ["a", "b", "c"])  # returns 1
```

### Test Implementation

- File: `test_utils.py`

- Class: `TestAccessNestedMap(unittest.TestCase)`

- Test Method: `test_access_nested_map`

- Decorated with `@parameterized.expand` to run multiple test cases automatically:

| nested_map          | path        | expected     |
|--------------------|------------|-------------|
| {"a": 1}           | ("a",)     | 1           |
| {"a": {"b": 2}}    | ("a",)     | {"b": 2}    |
| {"a": {"b": 2}}    | ("a", "b") | 2           |

- Each test case verifies that the function returns the expected value using assertEqual.

---

## Task 1: Parameterize a Unit Test for Exceptions

### Objective: 
Test that `access_nested_map` raises a `KeyError` when given invalid paths, and verify the error message matches the missing key.

### Test Implementation:
- Added `test_access_nested_map_exception` to `TestAccessNestedMap`.  
- Decorated with `@parameterized.expand` for multiple inputs:

| nested_map       | path        | expected_key |
|-----------------|------------|-------------|
| {}               | ("a",)     | "a"         |
| {"a": 1}         | ("a", "b") | "b"         |

- Uses `with self.assertRaises(KeyError) as context:` to catch exceptions.  
- Checks `context.exception.args[0]` to confirm the exception message is correct.

## How to Run the Tests

1. Ensure you are in the project directory.
2. Run the tests with `unittest`:

```bash
python3 -m unittest test_utils.py
```