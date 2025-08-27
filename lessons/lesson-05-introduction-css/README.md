# Lesson 5: Introduction to CSS

## Learning Objectives
By the end of this lesson, students will be able to:
- Understand the role of CSS in web development and its relationship to HTML
- Master CSS syntax including selectors, properties, and values
- Apply different methods of including CSS in HTML documents
- Use various types of CSS selectors to target HTML elements
- Implement basic styling properties for colors, fonts, and text
- Understand the CSS cascade, specificity, and inheritance principles
- Debug and troubleshoot CSS using browser developer tools

## Key Concepts

### 1. What is CSS?
- **Cascading Style Sheets**: Language for describing the presentation of HTML documents
- **Separation of concerns**: HTML for content structure, CSS for visual presentation
- **Consistency**: Apply consistent styling across multiple pages
- **Maintainability**: Centralized styling makes updates easier
- **Accessibility**: Proper CSS improves user experience across devices

### 2. CSS Syntax
- **Rule structure**: Selector + Declaration block
- **Selectors**: Target HTML elements for styling
- **Properties**: Aspects of elements to style (color, font-size, margin)
- **Values**: Specific settings for properties
- **Declarations**: Property-value pairs
- **Comments**: `/* Comment text */` for code documentation

### 3. Ways to Include CSS

#### Inline CSS
- Styles applied directly to HTML elements using `style` attribute
- Highest specificity but least maintainable
- Best for testing or one-off styles

#### Internal CSS
- Styles defined within `<style>` tags in HTML document head
- Affects only the current HTML document
- Good for page-specific styles

#### External CSS
- Styles defined in separate `.css` files
- Linked to HTML using `<link>` element
- Most maintainable and reusable approach
- Best practice for production websites

### 4. CSS Selectors

#### Basic Selectors
- **Element selectors**: Target HTML tag types (`p`, `h1`, `div`)
- **Class selectors**: Target elements with specific class (`.classname`)
- **ID selectors**: Target element with specific ID (`#idname`)
- **Universal selector**: Target all elements (`*`)

#### Attribute Selectors
- Target elements based on attributes and values
- Examples: `[href]`, `[type="text"]`, `[class*="nav"]`

#### Pseudo-classes and Pseudo-elements
- **Pseudo-classes**: Target elements in specific states (`:hover`, `:focus`)
- **Pseudo-elements**: Target parts of elements (`::before`, `::after`)

### 5. Basic Styling Properties

#### Color Properties
- **color**: Text color
- **background-color**: Background color
- **Color values**: Hex, RGB, HSL, named colors

#### Typography Properties
- **font-family**: Font typeface
- **font-size**: Text size
- **font-weight**: Text thickness
- **line-height**: Space between lines
- **text-align**: Text alignment

#### Text Properties
- **text-decoration**: Underline, strikethrough, etc.
- **text-transform**: Uppercase, lowercase, capitalize
- **letter-spacing**: Space between characters
- **word-spacing**: Space between words

### 6. CSS Cascade and Specificity
- **Cascade**: How conflicting CSS rules are resolved
- **Specificity**: Priority system for CSS rules
- **Inheritance**: How properties pass from parent to child elements
- **!important**: Override normal specificity (use sparingly)

## Practical Exercise: Personal Website Styling

### Project Description
Transform the semantic HTML personal website from previous lessons by applying comprehensive CSS styling to create an attractive, professional-looking site.

### Tasks
1. **Setup CSS Architecture**
   - Create external CSS file and link to HTML document
   - Organize CSS with comments and logical sections
   - Implement CSS reset or normalize styles

2. **Typography System**
   - Choose and implement web font families
   - Establish font size hierarchy for headings and body text
   - Set line height and spacing for optimal readability
   - Apply appropriate text colors and contrast ratios

3. **Color Scheme Implementation**
   - Develop cohesive color palette (primary, secondary, accent colors)
   - Apply colors to text, backgrounds, and accent elements
   - Ensure accessibility with proper contrast ratios
   - Use CSS custom properties (variables) for color consistency

4. **Basic Layout Styling**
   - Style navigation menus with hover effects
   - Add spacing and padding to content sections
   - Style lists, tables, and form elements
   - Create visual hierarchy through typography and spacing

5. **Interactive Elements**
   - Add hover effects for links and buttons
   - Style form inputs with focus states
   - Implement visual feedback for user interactions
   - Use pseudo-classes for enhanced interactivity

6. **CSS Organization and Best Practices**
   - Use meaningful class names following naming conventions
   - Avoid inline styles and minimize use of IDs for styling
   - Comment code sections and document design decisions
   - Validate CSS and test across different browsers

### Deliverables
- External CSS file with comprehensive styling
- Updated HTML with appropriate classes and semantic structure
- Cohesive visual design with consistent typography and colors
- Interactive elements with hover and focus states
- Well-organized, commented CSS code following best practices
- Documentation explaining design choices and color palette

## Code Examples
Check the `code_examples/` folder for:
- CSS syntax and structure examples
- Different methods of including CSS
- Selector variations and specificity demonstrations
- Typography and color implementation examples
- Interactive element styling techniques

## Additional Resources
- [CSS Basics - MDN](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
- [CSS Selectors - MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)
- [CSS Specificity Calculator](https://specificity.keegan.st/)
- [WebAIM Color Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Google Fonts](https://fonts.google.com/)
- [CSS-Tricks](https://css-tricks.com/) - Comprehensive CSS resource

## Self-Assessment Questions
1. What are the three ways to include CSS in an HTML document? What are the pros and cons of each?
2. How does CSS specificity determine which styles are applied when rules conflict?
3. What is the difference between a class selector and an ID selector?
4. How do you ensure your color choices meet accessibility standards?
5. What is the cascade in CSS and how does inheritance work?
6. When should you use pseudo-classes vs pseudo-elements?
7. How do you organize CSS code for maintainability in larger projects?

## Next Lesson Preview
In Lesson 6, we'll dive deeper into the CSS Box Model and positioning, learning how to control element spacing, dimensions, and layout positioning to create more sophisticated page layouts.