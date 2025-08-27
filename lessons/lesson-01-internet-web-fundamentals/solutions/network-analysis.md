# Network Analysis Solution Guide

## Exercise Solutions

### 1. Setting Up Local Server

**Python Server Solution:**
```bash
# Navigate to project directory
cd lesson-01-internet-web-fundamentals/code_examples

# Run the Python server
python3 simple-server.py
```

**Alternative Node.js Server:**
```bash
# Install http-server globally
npm install -g http-server

# Run server in current directory
http-server -p 8000
```

### 2. DNS Lookup Commands

**Windows:**
```cmd
# Basic DNS lookup
nslookup google.com

# Trace route to destination
tracert google.com

# Ping test
ping google.com
```

**macOS/Linux:**
```bash
# DNS lookup
nslookup google.com
# or
dig google.com

# Trace route
traceroute google.com

# Ping test
ping -c 4 google.com

# Show DNS cache (macOS)
dscacheutil -statistics

# Get IP information
curl ipinfo.io
```

### 3. Browser DevTools Network Analysis

#### Steps to Analyze Network Traffic:

1. **Open DevTools Network Tab**
   - Press F12 or Cmd+Option+I
   - Click on "Network" tab
   - Refresh the page (F5)

2. **Key Observations:**
   - **Name**: Resource being loaded
   - **Status**: HTTP status code (200, 404, etc.)
   - **Type**: Resource type (document, stylesheet, script, image)
   - **Size**: Transfer size vs actual size
   - **Time**: Loading duration
   - **Waterfall**: Visual timeline

3. **HTTP Headers Analysis**
   - Click on any request
   - View Headers tab:
     - Request Headers
     - Response Headers
     - General information

### 4. Sample Network Analysis Report

```markdown
# Network Analysis Report

## Website Analyzed: [Your Local Server]
**Date**: [Current Date]
**URL**: http://localhost:8000

## DNS Resolution
- **Domain**: localhost
- **IP Address**: 127.0.0.1 (loopback)
- **Resolution Time**: <1ms (local)

## HTTP Request/Response Cycle

### Initial Request
- **Method**: GET
- **URL**: http://localhost:8000/
- **Status**: 200 OK
- **Protocol**: HTTP/1.1

### Request Headers
- Host: localhost:8000
- User-Agent: [Your Browser Info]
- Accept: text/html,application/xhtml+xml
- Accept-Encoding: gzip, deflate
- Connection: keep-alive

### Response Headers
- Content-Type: text/html; charset=utf-8
- Content-Length: [Size in bytes]
- Server: SimpleHTTP/0.6 Python/3.x.x
- Date: [Current Date/Time]
- Cache-Control: no-cache, no-store, must-revalidate

## Page Load Performance
- **DOM Content Loaded**: ~[X]ms
- **Page Complete Load**: ~[X]ms
- **Total Resources**: [Number]
- **Total Size**: [Size]KB

## Resource Breakdown
1. HTML Document: 1 request, [X]KB
2. CSS Stylesheets: 0 external (inline styles used)
3. JavaScript: 0 external (inline script used)
4. Images: 0 requests
5. Other: 0 requests

## Observations
- Page loads quickly due to local server
- No external dependencies
- All content served from single HTML file
- No SSL/TLS encryption (HTTP not HTTPS)

## Recommendations
1. In production, use HTTPS for security
2. Consider external CSS/JS files for larger projects
3. Implement caching strategies
4. Optimize images when added
5. Add compression (gzip) for larger files
```

### 5. Console Commands Reference

**Useful Console Commands for Network Analysis:**

```javascript
// Get page load timing
console.log(performance.timing);

// Calculate page load time
const loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
console.log(`Page load time: ${loadTime}ms`);

// Get all network requests
performance.getEntriesByType("resource").forEach(resource => {
    console.log(`${resource.name}: ${resource.duration}ms`);
});

// Check connection type
console.log(navigator.connection);

// Get current page URL components
console.log({
    href: location.href,
    protocol: location.protocol,
    host: location.host,
    hostname: location.hostname,
    port: location.port,
    pathname: location.pathname
});

// Test fetch with timing
console.time('fetch-test');
fetch('https://jsonplaceholder.typicode.com/posts/1')
    .then(response => response.json())
    .then(data => {
        console.timeEnd('fetch-test');
        console.log(data);
    });
```

### 6. Common HTTP Status Codes

| Code | Meaning | Description |
|------|---------|-------------|
| 200 | OK | Request successful |
| 301 | Moved Permanently | Resource moved to new URL |
| 304 | Not Modified | Cached version is still valid |
| 400 | Bad Request | Invalid request syntax |
| 404 | Not Found | Resource doesn't exist |
| 500 | Internal Server Error | Server-side error |

## Tips for Success

1. **Always check Console for errors** - JavaScript errors appear here
2. **Use Network throttling** - Test slow connections
3. **Disable cache** - Check "Disable cache" in Network tab while DevTools is open
4. **Filter by type** - Use filters to focus on specific resource types
5. **Save HAR files** - Export network data for later analysis

## Conclusion

Understanding network analysis helps you:
- Debug loading issues
- Optimize performance
- Understand client-server communication
- Troubleshoot API calls
- Improve user experience

Keep practicing with different websites to become proficient with DevTools!