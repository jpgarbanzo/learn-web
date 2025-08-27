# Lesson 10: JavaScript Control Flow

## Learning Objectives
By the end of this lesson, students will be able to:
- Use conditional statements (if/else, switch) to control program flow
- Implement different types of loops (for, while, forEach) for repetitive tasks
- Create and call functions with parameters and return values
- Work with complex data structures (arrays and objects) effectively
- Apply scope and hoisting concepts in practical scenarios
- Handle errors gracefully using try/catch statements
- Build interactive programs that respond to user input and make decisions

## Key Concepts

### 1. Conditional Statements
- **if/else statements**: Basic decision making
- **else if**: Multiple conditions
- **Ternary operator**: Concise conditional expressions
- **Switch statements**: Multiple value comparisons
- **Truthy and falsy**: JavaScript's concept of "true" and "false" values

### 2. Loops
- **for loop**: Counter-based iteration
- **while loop**: Condition-based iteration
- **do-while loop**: Execute at least once
- **for...in loop**: Iterate over object properties
- **for...of loop**: Iterate over iterable objects
- **forEach**: Array method for iteration
- **Loop control**: break and continue statements

### 3. Functions
- **Function declarations**: Named functions that are hoisted
- **Function expressions**: Functions assigned to variables
- **Arrow functions**: Modern, concise function syntax
- **Parameters and arguments**: Passing data to functions
- **Return values**: Getting results from functions
- **Scope**: Function scope vs block scope vs global scope

### 4. Arrays (Advanced)
- **Array methods**: push(), pop(), shift(), unshift()
- **Search methods**: indexOf(), includes(), find(), filter()
- **Transformation methods**: map(), reduce(), sort()
- **Array destructuring**: Extracting values from arrays
- **Spread operator**: Expanding arrays

### 5. Objects (Advanced)
- **Property access**: Dot notation vs bracket notation
- **Adding and deleting properties**: Dynamic object manipulation
- **Object methods**: Functions as object properties
- **Object destructuring**: Extracting values from objects
- **Object.keys(), Object.values(), Object.entries()**

### 6. Error Handling
- **try/catch blocks**: Handling runtime errors
- **throw statement**: Creating custom errors
- **finally block**: Code that always runs
- **Error types**: Different kinds of JavaScript errors

## Practical Exercise: Interactive Task Management Application

### Project Description
Build a complete task management application that demonstrates control flow, functions, and data manipulation. Users can add, complete, filter, and manage tasks through an interactive interface.

### Tasks
1. **Task Data Management**
   - Create functions to add, edit, and delete tasks
   - Use arrays to store task collections
   - Implement task objects with properties (id, text, completed, priority, dueDate)
   - Handle data persistence using localStorage (if covered)

2. **Control Flow Implementation**
   - Use conditional statements for task filtering and validation
   - Implement loops for displaying and processing task lists
   - Create switch statements for handling different user actions
   - Apply error handling for invalid user input

3. **Interactive Functions**
   - Build functions for task creation with input validation
   - Create task filtering functions (all, completed, pending)
   - Implement search functionality using array methods
   - Add task sorting capabilities (by date, priority, alphabetical)

4. **User Interface Logic**
   - Handle user input and form submissions
   - Provide feedback for user actions (success/error messages)
   - Implement keyboard shortcuts and accessibility features
   - Create responsive interactions based on task states

5. **Advanced Features**
   - Task statistics calculation (total, completed, overdue)
   - Batch operations (mark all complete, delete completed)
   - Task categories and tagging system
   - Export functionality for task data

### Deliverables
- Fully functional task management application
- Clean, well-organized JavaScript code with proper function structure
- Error handling for edge cases and user input validation
- Interactive features demonstrating all control flow concepts
- Code documentation explaining logic and decision-making processes
- Testing examples showing different scenarios and edge cases

## Code Examples
Check the `code_examples/` folder for:
- Conditional statement patterns and best practices
- Loop variations and use case examples
- Function declaration and usage examples
- Array and object manipulation techniques
- Error handling patterns and debugging strategies

## Additional Resources
- [JavaScript Control Flow - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
- [JavaScript Functions - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
- [Array Methods - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Working with Objects - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects)
- [JavaScript Loops and Iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration)

## Self-Assessment Questions
1. What's the difference between function declarations and function expressions?
2. When should you use a for loop vs forEach vs map?
3. How does variable scope work in JavaScript functions?
4. What are truthy and falsy values, and how do they affect conditionals?
5. How do you handle errors gracefully in JavaScript?
6. What's the difference between for...in and for...of loops?
7. How do arrow functions differ from regular functions?

## Next Lesson Preview
In Lesson 11, we'll learn DOM manipulation and event handling, enabling our JavaScript code to interact with HTML elements and respond to user interactions.