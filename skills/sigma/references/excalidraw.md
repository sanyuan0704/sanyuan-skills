# Excalidraw Diagram Guide

Create elegant Excalidraw diagrams as HTML files with browser preview.

## Workflow

1. Plan node positions to avoid line intersections
2. Use consistent flow direction (left-to-right OR top-to-bottom)
3. Design element layout — positions, sizes, colors for visual harmony
4. Generate HTML file with elements
5. Open in browser: `open <path>.html`

## HTML Template

Write an HTML file replacing the `elementsData` array with designed elements:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Excalidraw Preview</title>
    <link
      rel="stylesheet"
      href="https://esm.sh/@excalidraw/excalidraw@0.18.0/dist/dev/index.css"
    />
    <script>
      window.EXCALIDRAW_ASSET_PATH =
        "https://esm.sh/@excalidraw/excalidraw@0.18.0/dist/prod/";
    </script>
    <script type="importmap">
      {
        "imports": {
          "react": "https://esm.sh/react@19.0.0",
          "react/jsx-runtime": "https://esm.sh/react@19.0.0/jsx-runtime",
          "react-dom": "https://esm.sh/react-dom@19.0.0",
          "react-dom/client": "https://esm.sh/react-dom@19.0.0/client"
        }
      }
    </script>
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body, #app { height: 100%; width: 100%; }
    </style>
  </head>
  <body>
    <div id="app"></div>
    <script type="module">
      import React from "https://esm.sh/react@19.0.0";
      import { createRoot } from "https://esm.sh/react-dom@19.0.0/client";
      import * as ExcalidrawLib from "https://esm.sh/@excalidraw/excalidraw@0.18.0/dist/dev/index.js?external=react,react-dom";

      const { Excalidraw, convertToExcalidrawElements } = ExcalidrawLib;

      const elementsData = [
        // INSERT DESIGNED ELEMENTS HERE
      ];

      const elements = convertToExcalidrawElements(elementsData);

      function App() {
        return React.createElement(
          "div",
          { style: { height: "100%", width: "100%" } },
          React.createElement(Excalidraw, {
            initialData: {
              elements: elements,
              appState: { viewBackgroundColor: "#ffffff" },
              scrollToContent: true,
            },
            langCode: "en",
          }),
        );
      }

      const root = createRoot(document.getElementById("app"));
      root.render(React.createElement(App));
    </script>
  </body>
</html>
```

## Element Types

All elements share base properties:

```javascript
{
  type: "rectangle" | "ellipse" | "diamond" | "line" | "arrow" | "text" | "freedraw",
  x: number,           // X position
  y: number,           // Y position
  width: number,       // Element width
  height: number,      // Element height
  strokeColor: string, // Border color (hex)
  backgroundColor: string, // Fill color (hex or "transparent")
  fillStyle: "solid" | "hachure" | "cross-hatch",
  strokeWidth: 1 | 2 | 4,
  roughness: 0 | 1 | 2,   // 0=architect, 1=artist, 2=cartoonist
  opacity: number,         // 0-100
  roundness: { type: 1 | 2 | 3 } | null,
}
```

### Rectangle
```javascript
{ type: "rectangle", x: 100, y: 100, width: 200, height: 100, backgroundColor: "#a5d8ff", strokeColor: "#1971c2" }
```

### Ellipse
```javascript
{ type: "ellipse", x: 100, y: 100, width: 150, height: 150, backgroundColor: "#b2f2bb", strokeColor: "#2f9e44" }
```

### Diamond
```javascript
{ type: "diamond", x: 100, y: 100, width: 120, height: 120, backgroundColor: "#ffec99", strokeColor: "#f08c00" }
```

### Text
```javascript
{ type: "text", x: 100, y: 100, text: "Hello World", fontSize: 20, width: 160, fontFamily: 1, textAlign: "center" }
```
- **`width`: REQUIRED** — `width = text.length * fontSize * 0.6`
- `fontSize`: 16 (small), 20 (medium), 28 (large), 36 (extra large)
- `fontFamily`: 1 (hand-drawn), 2 (normal), 3 (code)
- `textAlign`: "left" | "center" | "right"

### Arrow
```javascript
{ type: "arrow", x: 100, y: 100, width: 200, height: 0, strokeColor: "#e03131" }
```
- Positive width = right, negative = left
- Positive height = down, negative = up

### Line
```javascript
{ type: "line", x: 100, y: 100, width: 200, height: 100, strokeColor: "#1971c2" }
```

## Color Palette

| Color | Light | Stroke |
|-------|-------|--------|
| Blue | `#a5d8ff` | `#1971c2` |
| Green | `#b2f2bb` | `#2f9e44` |
| Yellow | `#ffec99` | `#f08c00` |
| Red | `#ffc9c9` | `#e03131` |
| Purple | `#d0bfff` | `#7048e8` |
| Gray | `#e9ecef` | `#495057` |
| Orange | `#ffd8a8` | `#e8590c` |
| Pink | `#fcc2d7` | `#d6336c` |
| Cyan | `#99e9f2` | `#0c8599` |

## Layout Guidelines

- Minimum padding between elements: 40px
- Group spacing: 80-100px
- Text padding inside shapes: 20px
- Use larger shapes for main concepts, bolder colors for emphasis

## Common Patterns

### Flowchart Node
```javascript
[
  { type: "rectangle", x: 0, y: 0, width: 160, height: 60, backgroundColor: "#a5d8ff", strokeColor: "#1971c2", roundness: { type: 3 } },
  { type: "text", x: 80, y: 30, text: "Step 1", fontSize: 20, textAlign: "center" }
]
```

### Connection Arrow
```javascript
{ type: "arrow", x: 160, y: 30, width: 60, height: 0, strokeColor: "#495057" }
```

### Decision Diamond
```javascript
{ type: "diamond", x: 0, y: 0, width: 100, height: 80, backgroundColor: "#ffec99", strokeColor: "#f08c00" }
```

### Container/Group Box
```javascript
{ type: "rectangle", x: 0, y: 0, width: 300, height: 200, backgroundColor: "transparent", strokeColor: "#dee2e6", strokeStyle: "dashed" }
```
