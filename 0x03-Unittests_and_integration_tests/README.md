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

---

## Task 2: Mock HTTP Calls

### Objective:  
Test that `get_json` returns the expected payload without making real HTTP requests.

### Test Implementation:  
- Added `TestGetJson` class with `test_get_json` method.  
- Uses `@parameterized.expand` for multiple inputs:

| test_url              | test_payload       |
|----------------------|------------------|
| "http://example.com"  | {"payload": True} |
| "http://holberton.io" | {"payload": False} |

- Uses `unittest.mock.patch` to mock `requests.get`.  
- The mocked `.json()` method returns `test_payload`.  
- Assertions:
  - `requests.get` called **exactly once** with `test_url`.  
  - `get_json(test_url)` output equals **mocked payload**.

---

## Task 3: Parameterize and Patch (Memoization)

### Objective:  
Test that the `memoize` decorator caches a method’s result after the first call, preventing repeated executions.

### Test Implementation:  
- Added `TestMemoize` class with `test_memoize` method.  
- Defined an inner class `TestClass` with:
  - `a_method()` → returns 42  
  - `a_property()` → decorated with `@memoize`  

- Used `unittest.mock.patch` to **mock `a_method`**, allowing us to track calls.  
- Steps:
  1. Call `a_property` **twice**.  
  2. Assert both calls return **42**.  
  3. Assert `a_method` was called **only once** using `assert_called_once`.

---

## Task 4: Parameterize and Patch as Decorators

### Objective:

Test the `GithubOrgClient.org` method without making real HTTP requests by using patching and parameterization.

### Test Implementation:

- Created a new test file: `test_client.py`.

- Added the class `TestGithubOrgClient(unittest.TestCase)`.

- Implemented `test_org` to verify that:

  1. `GithubOrgClient.org` returns the correct mocked payload.

  2. `get_json` is called exactly once with the expected GitHub API URL.

  3. Used:

    - `@patch('client.get_json')` to replace real HTTP calls with a mock.

    - `@parameterized.expand` to test multiple organizations (google, abc).

    - Ensured no real HTTP requests were made during testing.

---

## Task 5: Test GithubOrgClient._public_repos_url

### Objective:

Unit-test the private property `_public_repos_url` of `GithubOrgClient` by mocking the org property, which is memoized and therefore behaves like a property.

### Test Implementation:

- Added a test method `test_public_repos_url` in `TestGithubOrgClient` class.

- Used `unittest.mock.patch.object` with PropertyMock to mock the org property.

- Set the mocked property to return a known payload:
  ```
    {"repos_url": "https://api.github.com/orgs/testorg/repos"}
  ```
- Called the private property _public_repos_url and asserted it returned the expected URL.

- Ensured no real HTTP requests were made.

---

## Task 6: Test GithubOrgClient.public_repos

### Objective:

Unit-test the `public_repos` method of `GithubOrgClient` by mocking both the `_public_repos_url` property and the `get_json` function, ensuring no real HTTP requests are made.

### Test Implementation:

- Added a test method `test_public_repos` in `TestGithubOrgClient`.

- Used `@patch("client.get_json")` to mock the JSON response from the API.

- Used `patch.object(GithubOrgClient, "_public_repos_url", new_callable=PropertyMock)` to mock the private property `_public_repos_url`.

- Set fake values:

  - `_public_repos_url → "https://api.fake.com/orgs/testorg/repos"`

  - `get_json → [{"name": "repo1"}, {"name": "repo2"}, {"name": "repo3"}]`

- Called `client.public_repos()` and **asserted**:

  - Returned list of repo names matches the mocked payload.

  - `_public_repos_url` property was accessed once.

  - `get_json` was called once with the fake URL.

---

## Task 7: Test GithubOrgClient.has_license

### Objective:

Unit-test the static method `has_license` of `GithubOrgClient` by checking if a repository dictionary contains a given license key.

### Test Implementation:

- Added a test method `test_has_license` in `TestGithubOrgClient`.

- Used `@parameterized.expand` to test multiple cases in a single method:

```
{"license": {"key": "my_license"}} with "my_license" → should return True

{"license": {"key": "other_license"}} with "my_license" → should return False
```
- Asserted that `has_license(repo, license_key)` returns the expected boolean value for each case.

## How to Run the Tests

1. Ensure you are in the project directory.
2. Run the tests with `unittest`:

```bash
python3 -m unittest test_utils.py
python3 -m unittest test_client.py
```