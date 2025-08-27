# 🚀 GitHub Codespaces Setup Guide

## Quick Start with GitHub Codespaces

GitHub Codespaces provides a complete, cloud-based development environment that runs in your browser. No local installation required!

### 1. Launch Codespace

1. **From GitHub:**
   - Go to the repository on GitHub
   - Click the green **"Code"** button
   - Select **"Codespaces"** tab
   - Click **"Create codespace on main"**

2. **Wait for Setup:**
   - Codespace will automatically configure your environment
   - Extensions will be installed
   - Development servers will be ready

### 2. Running the Evolution Example

Once your Codespace is ready, you have multiple ways to run the web app:

#### Option A: Using Live Server (Recommended)
```bash
# The Live Server extension is pre-installed
# Simply right-click on evolution-example.html
# Select "Open with Live Server"
```

#### Option B: Using Python HTTP Server
```bash
# Navigate to the repository root
cd /workspaces/web-programming-1

# Run Python server
python3 -m http.server 8000

# Open the preview panel or visit:
# http://localhost:8000/evolution-example.html
```

#### Option C: Using Node.js HTTP Server
```bash
# http-server is pre-installed via postCreateCommand
http-server -p 8080

# Visit: http://localhost:8080/evolution-example.html
```

#### Option D: Using Live Server CLI
```bash
# live-server is pre-installed
live-server --port=5500

# Browser will open automatically
```

### 3. Accessing the Application

When running any server, Codespaces will:
1. Detect the running port
2. Show a notification to open in browser
3. Provide a forwarded URL like: `https://[codespace-name]-[port].app.github.dev`

### 4. Understanding the Evolution Example

The `evolution-example.html` file demonstrates three stages:

1. **Stage 1 - Plain HTML**
   - Basic form with browser default styling
   - No custom appearance
   - Form submission would reload the page

2. **Stage 2 - HTML + CSS**
   - Same form with beautiful styling
   - Gradients, shadows, hover effects
   - Responsive design with flexbox

3. **Stage 3 - HTML + CSS + JavaScript**
   - Fully interactive form
   - No page reload on submission
   - Dynamic feedback messages
   - Input validation

### 5. Exploring with DevTools

While in Codespaces:

1. **Open DevTools:**
   - Right-click → Inspect
   - Or press `F12` / `Cmd+Option+I`

2. **Try These Experiments:**
   - **Elements Tab:** Modify styles in real-time
   - **Console Tab:** See JavaScript messages and run commands
   - **Network Tab:** Watch resource loading
   - **Sources Tab:** Set breakpoints in JavaScript

### 6. Codespaces Features

Your environment includes:

#### Pre-installed Extensions
- **Live Server** - Launch development server with live reload
- **Prettier** - Code formatter
- **ESLint** - JavaScript linter
- **Auto Rename Tag** - Automatically rename paired HTML tags
- **Auto Close Tag** - Automatically close HTML tags
- **HTML CSS Support** - CSS IntelliSense for HTML

#### Available Ports
- `5500` - Live Server default
- `8000` - Python HTTP server
- `3000` - Node.js apps
- `8080` - Alternative HTTP server

#### Terminal Commands Available
```bash
# Python (3.11)
python3 --version

# Node.js (20.x)
node --version
npm --version

# Pre-installed global packages
http-server --version
live-server --version
```

### 7. Working with Lessons

Each lesson has its own folder:

```bash
# Navigate to a specific lesson
cd lessons/lesson-01-internet-web-fundamentals

# Open the lesson's code examples
cd code_examples

# Run a local server from this directory
python3 -m http.server 8000
```

### 8. Tips for Success

1. **Auto-save is enabled** - Your changes are saved automatically
2. **Use multiple terminals** - Run different servers simultaneously
3. **Preview panel** - Use the built-in browser for quick testing
4. **Port forwarding** - All ports are automatically forwarded
5. **Collaboration** - Share your Codespace URL with others

### 9. Troubleshooting

#### Server won't start?
```bash
# Kill any existing processes on the port
lsof -ti:8000 | xargs kill -9

# Or use a different port
python3 -m http.server 8001
```

#### Extensions not working?
1. Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
2. Run: "Developer: Reload Window"

#### Can't see the preview?
1. Check the Ports panel in the terminal area
2. Click the globe icon to open in browser
3. Or manually visit the forwarded URL

### 10. Saving Your Work

Your work in Codespaces is automatically saved to the cloud. To save permanently:

1. **Commit changes:**
   ```bash
   git add .
   git commit -m "Add my changes"
   git push
   ```

2. **Or use Source Control panel:**
   - Click Source Control icon in sidebar
   - Stage changes
   - Commit with message
   - Push to repository

## Next Steps

1. Open `evolution-example.html` in Live Server
2. Explore the three stages of web development
3. Try modifying the code in each stage
4. Check the browser console for helpful messages
5. Start with Lesson 1 in the `lessons/` directory

Happy coding! 🎉