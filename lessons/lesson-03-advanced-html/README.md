# Lesson 3: Advanced HTML

## Learning Objectives
By the end of this lesson, students will be able to:
- Create and configure different types of hyperlinks
- Build ordered, unordered, and nested lists
- Embed images with proper attributes and accessibility features
- Add audio and video content to web pages
- Understand file paths and linking between pages
- Apply best practices for multimedia content and navigation

## Key Concepts

### 1. Hyperlinks and Navigation
- **Anchor element**: `<a>` tag creates clickable links
- **href attribute**: Specifies the link destination
- **Link types**: External links, internal links, email links, phone links
- **Link states**: Default, visited, hover, active
- **Accessibility**: Link text should be descriptive and meaningful

### 2. Lists and Organization
- **Unordered lists**: `<ul>` for bullet point lists
- **Ordered lists**: `<ol>` for numbered lists
- **List items**: `<li>` for individual list entries
- **Nested lists**: Lists within lists for hierarchical structure
- **Description lists**: `<dl>`, `<dt>`, `<dd>` for term-definition pairs

### 3. Images and Graphics
- **img element**: `<img>` for embedding images
- **Essential attributes**:
  - `src`: Image source URL or path
  - `alt`: Alternative text for accessibility
  - `width` and `height`: Dimension control
  - `title`: Tooltip text on hover
- **File formats**: JPEG, PNG, GIF, SVG, WebP
- **Responsive considerations**: Image sizing and optimization

### 4. Audio Content
- **audio element**: `<audio>` for sound files
- **Important attributes**:
  - `src`: Audio file source
  - `controls`: Display playback controls
  - `autoplay`: Automatic playback (use carefully)
  - `loop`: Repeat playback
  - `muted`: Start muted
- **Multiple sources**: Support for different audio formats
- **Accessibility**: Providing transcripts and captions

### 5. Video Content
- **video element**: `<video>` for video files
- **Key attributes**:
  - `src`: Video file source
  - `controls`: Show video controls
  - `width` and `height`: Video dimensions
  - `poster`: Thumbnail image before play
  - `autoplay`, `loop`, `muted`: Playback options
- **Multiple formats**: Ensuring browser compatibility
- **Accessibility**: Captions and descriptions

### 6. File Paths and Links
- **Absolute paths**: Full URL or complete file path
- **Relative paths**: Paths relative to current document
- **Root-relative paths**: Paths from website root
- **Best practices**: Organizing files and folders logically

## Practical Exercise: Personal Portfolio Website

### Project Description
Create a multi-page personal portfolio website that demonstrates advanced HTML features including navigation, multimedia content, and proper file organization.

### Tasks
1. **Site Structure Setup**
   - Create a main index.html page
   - Create additional pages (about.html, portfolio.html, contact.html)
   - Organize images and media in appropriate folders
   - Set up logical navigation between pages

2. **Navigation Implementation**
   - Create a navigation menu with links to all pages
   - Include external links to social media or professional profiles
   - Add "back to top" links on longer pages
   - Implement proper link accessibility

3. **Content Organization with Lists**
   - Create bulleted lists for skills or services
   - Use numbered lists for processes or steps
   - Build nested lists for categorized information
   - Include a description list for technical terms or tools

4. **Multimedia Integration**
   - Add a profile photo with proper alt text
   - Include a portfolio gallery with multiple images
   - Embed an audio introduction or demo
   - Add a video presentation or project demo
   - Ensure all media has appropriate fallbacks

5. **Advanced Features**
   - Create downloadable links (resume, portfolio PDF)
   - Add mailto: and tel: links for contact information
   - Implement proper heading hierarchy across all pages
   - Test all links and media functionality

### Deliverables
- Multi-page website with consistent navigation
- Properly structured lists and multimedia content
- Working internal and external links
- Accessible images with descriptive alt text
- Functional audio and video elements
- Well-organized file structure

## Code Examples
Check the `code_examples/` folder for:
- Link variations and navigation patterns
- Different list types and structures
- Image implementation with various attributes
- Audio and video embedding techniques
- File organization examples

## Additional Resources
- [HTML Links - MDN](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks)
- [HTML Lists - MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)
- [HTML Images - MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)
- [HTML Audio and Video - MDN](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Video_and_audio_content)
- [Web Accessibility Guidelines - WCAG](https://www.w3.org/WAI/WCAG21/quickref/)

## Self-Assessment Questions
1. What is the difference between absolute and relative file paths?
2. Why is the alt attribute important for images?
3. When should you use ordered vs. unordered lists?
4. What considerations should you make before adding autoplay to audio/video?
5. How can you make links more accessible for screen reader users?
6. What are the advantages of using different image formats (JPEG, PNG, SVG)?

## Next Lesson Preview
In Lesson 4, we'll explore tables for data presentation, iframes for embedding content, and semantic HTML5 elements that give meaning and structure to our web pages.