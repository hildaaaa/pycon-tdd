# Getting Started With Test Driven Development in Python

## Background Info

### Why TDD?
Some benefits of practicing TDD include:
- Test coverage
- Bug prevention
- Confidence in refactoring
- Ease in debugging
- Helps define how the code should be used
- Only write necessary code

### What is TDD?
1. Writing tests before writing code
2. Write the minimum amount of code necessary to make tests pass
3. Rinse and repeat

#### Red - Green - Refactor
1. Write a test, see your code fail for the right reasons to make sure you’re testing the right thing (Red)
2. Make the test pass by writing the minimum amount of code necessary to make the tests pass (Green)
3. Refactor your code when the tests are green and ensure the tests still pass after refactoring
4. Repeat Steps 1-3 till your functionality is complete

#### Python test frameworks
In python, there are many testing frameworks available. Unittest and Pytest are the more commonly used ones. Feel free to use whichever test framework you are comfortable with. However the code examples provided by us will be in unittest.

## The Challenge

**You are given strings of different lengths. If the number of vowels are more than 30% of the string length then insert ‘mummy’ for each continuous set of vowels.**

For example `<input>` -> `<output>`,
- his -> hmummys
- hear -> hmummyr

The challenge for you today is to complete the above problem with a TDD (Red-Green-Refactor) approach. 

### Prerequisites:
- Python 3 installed
- Any text editor of your choice
- Basic knowledge of Python

#### Tip: 
- Have a plan of what scenarios you wish to test. Try to come up with all the edge cases yourself!
  - If you are stuck, you can refer to this [link](test-scenarios.md) to see the complete list of scenarios you can test for.
- Use the guidelines in Red - Green - Refactor to solve the problem.
- Strive to give your test methods have a meaningful name describing the scenario you are testing and its expected behaviour if possible
- If you are new to python and not sure where to start, you can refer to this [link](step-by-step-guide.md) for a step by step guide on getting started.
