
#### Steps for python beginners:
1. Create a test file called `test_string_mummifier.py` (You will use this file to write tests for your solution)
   1. In this file import TestCase from unittest
   
   ```
   from unittest import TestCase
   ```
   
   2. Create a python class `TestStringMummifier` that inherits from TestCase
   
   ```
   from unittest import TestCase
   
   class StringMummifierTestCase(TestCase):
       pass
   ```
   
   3. Create a method prefixed with `test_` (this because the unittest framework picks up only test methods beginning with `test_`
Your test method should have a meaningful name describing the scenario you are testing and its expected behaviour if possible. For e.g. `test_should_not_mummify_empty_string`

   ```
   from unittest import TestCase
   
   class StringMummifierTestCase(TestCase):
       def test_should_not_mummify_empty_string(self):
           pass
   ```

   4. In the test method, you may structure the test in the below format:
      - Arrange (Initialize any variables you require)
      - Act (Invoke the method you are testing)
      - Assert (Check that your expectations are met)

   - Tip: Utilise the self.assertEqual() to validate the method’s outputs against what you expect

    ```
    from unittest import TestCase
    
    from string_mummifier import StringMummifier
    
    
    class StringMummifierTestCase(TestCase):
       def test_should_not_mummify_empty_string(self):
           word = "";
    
           mummifier = StringMummifier();
           mummified_word = mummifier.mommify(word);
    
           self.assertEqual("", mummified_word);
    
    ```

2. Create a file called string_mummifier.py
You will use this file to write the code for your solution

   1. Create a python class StringMummifier and a method in the class called mummify that takes in a word
    
    ```
    class StringMummifier:
        def mummify(self, word):
            return None
    ```

3. Run the test

   1. In your project folder, you can run `python3 -m unittest test_string_mummifier.py`
  
   2. See that the test fails (Red Stage!)
   
4. Fix the test by implementing the simplest possible logic in the mummify method

   ```python
   class StringMummifier:
   
      def mummify(self, word):
          return ""

   ```

5. Run the test

   1. See that the test passes (Green Stage!)

6. Refactor your solution if required

7. Repeat the below steps:
   1. Writing a new test, see that it fails (Red)
   2. Write the functionality to fix the test, and tests should pass (Green)
   3. Refactor where necessary

  