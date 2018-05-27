# Getting Started With Test Driven Development in Python

## Why TDD?
Some benefits of practicing TDD include:
- Immediate feedback on if your code is working, so you can find bugs faster
- Confidence in refactoring
- Helps define how the code should be used
- Encourages writing only the necessary code required

## What is TDD?
1. Writing tests before writing code
2. Write the minimum amount of code necessary to make tests pass
3. Rinse and repeat

## Red-Green-Refactor
Red-green-refactor is a framework that developers use to build a test suite, write implementation code, and optimize their codebase in short development cycles.

### Red
1. Write a test
2. Run the test and see your test fail for the right reason (Red)
   
### Green
1. Write the minimum amount of code necessary to make the tests pass
2. Run the tests, and see that all tests should pass (Green)

### Refactor
Change the code to remove duplication in your project and to improve the design while ensuring that all tests still pass.

## Python test frameworks
In python, there are many testing frameworks available. Unittest and Pytest are the more commonly used ones. Feel free to use whichever test framework you are comfortable with. However the code examples provided by us will be in unittest.

# The Challenge

You are given strings of different lengths. If the number of **vowels** are **more than 30%** of the string length then insert ‘mummy’ for each **continuous** set of vowels.

For example `<input>` -> `<output>`,
- his -> hmummys
- hear -> hmummyr

The challenge for you today is to complete the above problem with a TDD (Red-Green-Refactor) approach. 

## Prerequisites:
- Python 3 installed
- Any text editor of your choice
- Basic knowledge of Python

## Steps:
1. Understand the requirements and have a plan of what scenarios you wish to test for.
   - Hint: The key criteria have been highlighted in **bold**. Test for scenarios that fulfill and don't fulfill the criteria to be "mummified"
   - Plan the list of inputs and their expected outputs for each of the test scenarios you can think of.
2. Follow the steps of [Red-Green-Refactor](#red-green-refactor) and finish implementing the solution.
   - The first test method has been set up for you. You may choose to clone the repo or start from scratch by yourself. (It's easy!)
     - The tests are written in `test_string_mummifier.py` while the implementation is written in `string_mummifier.py`
   - You can run all tests with this command while in the project directory: `python3 -m unittest test_string_mummifier.py`. Or if you are using an IDE like PyCharm, you should be able to run tests from the IDE itself by right clicking the test name and selecting 'Run unittests for ...'
   - If you are unfamiliar with python, we recommend that you start from referring to our step by step guide [here](step-by-step-guide.md)
4. Repeat the Red-Green-Refactor steps till your functionality is complete.

## Tip:
- If you are stuck with coming up with a list of test scenarios, you can refer to this [link](test-scenarios.md) to see the complete list we have come up with.
- Strive to give each of your test methods a meaningful name describing the scenario you are testing and its expected behaviour if possible
- Finally, have fun!

## Got Feedback?
We'd sure love to hear what you think about this workshop! Just fill in [this form](https://goo.gl/forms/huDZd1VlFSICOZIa2) and share your thoughts!