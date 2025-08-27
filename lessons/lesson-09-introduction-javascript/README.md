# Lesson 9: Introduction to JavaScript

## Learning Objectives
By the end of this lesson, students will be able to:
- Understand JavaScript's role in web development and its relationship to HTML/CSS
- Declare and use variables with proper naming conventions
- Work with different JavaScript data types (strings, numbers, booleans, arrays, objects)
- Perform calculations and comparisons using JavaScript operators
- Use template literals for dynamic string creation
- Debug JavaScript code using browser developer tools
- Write clean, readable JavaScript code following best practices

## Key Concepts

### 1. What is JavaScript?
- **Programming language**: Adds interactivity and dynamic behavior to websites
- **Client-side scripting**: Runs in the user's browser
- **Dynamic typing**: Variables can hold different types of values
- **Interpreted language**: No compilation step required
- **ECMAScript**: The standard that JavaScript implements

### 2. Including JavaScript in HTML
- **Inline JavaScript**: Using onclick and other event attributes (not recommended)
- **Internal JavaScript**: Using `<script>` tags in HTML document
- **External JavaScript**: Linking to separate .js files (best practice)
- **Script placement**: Before closing `</body>` tag for performance

### 3. Variables and Constants
- **var**: Function-scoped, can be redeclared (avoid in modern JavaScript)
- **let**: Block-scoped, can be reassigned
- **const**: Block-scoped, cannot be reassigned (use for values that won't change)
- **Naming conventions**: camelCase, descriptive names, no reserved words

### 4. Data Types

#### Primitive Types
- **String**: Text data ("hello", 'world', \`template\`)
- **Number**: Integer and floating-point numbers (42, 3.14)
- **Boolean**: True or false values
- **Undefined**: Variable declared but not assigned
- **Null**: Intentional absence of value
- **Symbol**: Unique identifiers (advanced topic)

#### Reference Types
- **Arrays**: Ordered lists of values [1, 2, 3]
- **Objects**: Key-value pairs {name: "John", age: 30}
- **Functions**: Reusable blocks of code (covered in next lesson)

### 5. Operators

#### Arithmetic Operators
- **Addition (+)**: Add numbers or concatenate strings
- **Subtraction (-)**: Subtract numbers
- **Multiplication (*)**: Multiply numbers
- **Division (/)**: Divide numbers
- **Modulo (%)**: Remainder after division
- **Exponentiation (**)**: Raise to a power

#### Comparison Operators
- **Equal (==)**: Loose equality (type coercion)
- **Strict equal (===)**: Strict equality (no type coercion)
- **Not equal (!=)**: Loose inequality
- **Strict not equal (!==)**: Strict inequality
- **Greater than (>)**: Numeric comparison
- **Less than (<)**: Numeric comparison
- **Greater than or equal (>=)**
- **Less than or equal (<=)**

#### Logical Operators
- **AND (&&)**: Both conditions must be true
- **OR (||)**: At least one condition must be true
- **NOT (!)**: Opposite of the condition

### 6. Template Literals
- **Backtick syntax**: Using \` instead of quotes
- **Variable interpolation**: ${variable} syntax
- **Multi-line strings**: Natural line breaks
- **Expression evaluation**: ${expression} can contain calculations

## Practical Exercise: Interactive Personal Information Display

### Project Description
Create an interactive webpage that collects and displays personal information using JavaScript variables, operators, and data types. This project will demonstrate fundamental JavaScript concepts in a practical context.

### Tasks
1. **Variable Declaration and Usage**
   - Create variables for personal information (name, age, city, hobbies)
   - Use appropriate variable types (const for unchanging values, let for changing values)
   - Demonstrate different data types with meaningful examples
   - Follow proper naming conventions

2. **Data Type Manipulation**
   - Work with strings (concatenation, length, case conversion)
   - Perform mathematical calculations with numbers
   - Use boolean values for conditional logic
   - Create and manipulate arrays of information
   - Build objects to represent structured data

3. **Operator Usage**
   - Use arithmetic operators for age calculations and statistics
   - Implement comparison operators for data validation
   - Apply logical operators for complex conditions
   - Demonstrate operator precedence and parentheses usage

4. **Template Literals and Dynamic Content**
   - Create formatted output using template literals
   - Build multi-line strings for complex data display
   - Use expression interpolation for dynamic calculations
   - Generate HTML content dynamically

5. **Console Output and Debugging**
   - Use console.log() for debugging and testing
   - Display different data types in the console
   - Practice reading error messages and debugging
   - Use browser developer tools effectively

### Deliverables
- HTML page with embedded JavaScript functionality
- External JavaScript file demonstrating best practices
- Interactive features using JavaScript variables and operators
- Well-commented code explaining each concept
- Console output demonstrating different data types and operations
- Documentation explaining the code structure and decisions

## Code Examples
Check the `code_examples/` folder for:
- Variable declaration and scoping examples
- Data type demonstrations and type checking
- Operator usage and precedence examples
- Template literal patterns and use cases
- Debugging techniques and console usage

## Additional Resources
- [JavaScript Basics - MDN](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
- [JavaScript Data Types - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
- [JavaScript Variables - MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
- [Template Literals - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
- [JavaScript.info - Modern JavaScript Tutorial](https://javascript.info/)

## Self-Assessment Questions
1. What's the difference between let, const, and var?
2. When should you use strict equality (===) vs loose equality (==)?
3. What are the different data types in JavaScript and how do you check them?
4. How do template literals improve string handling in JavaScript?
5. What's the difference between undefined and null?
6. How do logical operators work with truthy and falsy values?
7. What are some JavaScript naming conventions and why are they important?

## Next Lesson Preview
In Lesson 10, we'll build on these JavaScript fundamentals by learning about control flow including conditionals, loops, functions, and more complex data structures.