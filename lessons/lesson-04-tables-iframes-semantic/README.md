# Lesson 4: Tables, Iframes, and Semantic Markup

## Learning Objectives
By the end of this lesson, students will be able to:
- Create well-structured HTML tables for tabular data presentation
- Implement accessible table features including headers and captions
- Use iframes to embed external content responsibly
- Apply semantic HTML5 elements to create meaningful document structure
- Understand the importance of semantic markup for accessibility and SEO
- Design page layouts using semantic elements effectively

## Key Concepts

### 1. HTML Tables
- **Purpose**: Present tabular data in rows and columns
- **Basic structure**: `<table>`, `<tr>`, `<td>`, `<th>`
- **Semantic elements**: `<thead>`, `<tbody>`, `<tfoot>`, `<caption>`
- **Accessibility**: Proper headers, scope attributes, and descriptions
- **Styling considerations**: Separating content from presentation

### 2. Table Components
- **table**: Container for all table content
- **caption**: Describes the table's content and purpose
- **thead**: Groups header content
- **tbody**: Groups main table data
- **tfoot**: Groups footer content (summaries, totals)
- **tr**: Table row
- **th**: Header cell (use scope attribute for accessibility)
- **td**: Data cell

### 3. Iframes (Inline Frames)
- **Purpose**: Embed external content within a webpage
- **Security considerations**: Sandbox attributes and content policies
- **Responsive design**: Making iframes adapt to different screen sizes
- **Accessibility**: Providing meaningful titles and descriptions
- **Common uses**: Maps, videos, widgets, embedded applications

### 4. Semantic HTML5 Elements
- **Document structure**: `<header>`, `<nav>`, `<main>`, `<footer>`
- **Content sectioning**: `<section>`, `<article>`, `<aside>`
- **Text semantics**: `<mark>`, `<time>`, `<figure>`, `<figcaption>`
- **Interactive elements**: `<details>`, `<summary>`

### 5. Semantic Benefits
- **Accessibility**: Screen readers understand content structure
- **SEO**: Search engines better understand page content
- **Maintainability**: Code is more readable and logical
- **Future-proofing**: Semantic markup adapts to new technologies

## Practical Exercise: Company Annual Report Dashboard

### Project Description
Create a comprehensive company annual report webpage that demonstrates tables for financial data, semantic markup for content organization, and embedded content through iframes.

### Tasks
1. **Document Structure with Semantic Elements**
   - Use semantic HTML5 elements to create a logical page structure
   - Include header with navigation, main content areas, and footer
   - Organize content with appropriate sectioning elements

2. **Financial Data Tables**
   - Create tables for quarterly sales data, employee statistics, and budget breakdown
   - Use proper table headers with scope attributes
   - Include captions and summaries for accessibility
   - Implement responsive table design considerations

3. **Embedded Content with Iframes**
   - Embed a company location map
   - Include a chart or graph from an external source
   - Add a contact form or feedback widget
   - Ensure all iframes have appropriate security and accessibility attributes

4. **Content Organization**
   - Use article elements for distinct content sections
   - Implement aside elements for supplementary information
   - Add figure and figcaption for images and charts
   - Include interactive details/summary sections for additional information

5. **Accessibility and Best Practices**
   - Ensure all content is keyboard navigable
   - Provide alternative text and descriptions
   - Test with screen reader compatibility
   - Validate semantic markup structure

### Deliverables
- Semantic HTML document with proper element hierarchy
- Accessible data tables with financial information
- Responsibly embedded external content via iframes
- Proper use of HTML5 semantic elements throughout
- Validated, accessible markup following best practices

## Code Examples
Check the `code_examples/` folder for:
- Table structure and accessibility examples
- Iframe implementation and security practices
- Semantic HTML5 element demonstrations
- Complete page layout using semantic markup

## Additional Resources
- [HTML Tables - MDN](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables)
- [HTML5 Semantic Elements - MDN](https://developer.mozilla.org/en-US/docs/Glossary/Semantics#semantics_in_html)
- [iframe Security Best Practices](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe)
- [WebAIM: Creating Accessible Tables](https://webaim.org/techniques/tables/)
- [HTML5 Outlining Algorithm](https://www.w3.org/wiki/HTML/Usage/Headings/Missing)

## Self-Assessment Questions
1. When should you use a table versus other layout methods?
2. What is the difference between `<th>` and `<td>` elements?
3. How do the `scope` and `headers` attributes improve table accessibility?
4. What security considerations should you keep in mind when using iframes?
5. Explain the difference between `<section>`, `<article>`, and `<div>` elements
6. Why is semantic markup important for SEO and accessibility?
7. How do you make tables responsive without losing their tabular nature?

## Next Lesson Preview
In Lesson 5, we'll dive into CSS (Cascading Style Sheets) to learn how to style and visually enhance the semantic HTML structures we've created, transforming plain markup into beautiful, responsive designs.