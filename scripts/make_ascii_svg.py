import os

ASCII_NAME = [
    " ██████╗ ███████╗██████╗  █████╗ ██████╗ ██████╗  ██████╗ ",
    "██╔════╝ ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔═══██╗",
    "██║  ███╗█████╗  ██████╔╝███████║██████╔╝██║  ██║██║   ██║",
    "██║   ██║██╔══╝  ██╔══██╗██╔══██║██╔══██╗██║  ██║██║   ██║",
    "╚██████╔╝███████╗██║  ██║██║  ██║██║  ██║██████╔╝╚██████╔╝",
    " ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ",
    "",
    "███████╗██╗      █████╗ ███╗   ███╗███╗   ███╗██╗█████╗  ",
    "██╔════╝██║     ██╔══██╗████╗ ████║████╗ ████║██║██╔══██╗",
    "█████╗  ██║     ███████║██╔████╔██║██╔████╔██║██║███████║",
    "██╔══╝  ██║     ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██║██╔══██║",
    "██║     ███████╗██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║██║  ██║",
    "╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═╝",
    "",
    "=========================================================",
    "      R&D ENGINEER | BACKEND & AI | AUTOMATIONS          ",
    "=========================================================",
]

def generate_svg():
    width = 370
    height = 420
    row_height = 16
    total_rows = len(ASCII_NAME)
    
    duration_per_row = 0.06
    
    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">')
    svg_lines.append('<style>')
    svg_lines.append('  .bg { fill: #0d1117; rx: 8px; ry: 8px; stroke: #30363d; stroke-width: 1px; }')
    svg_lines.append('  .title-bar { fill: #161b22; }')
    svg_lines.append('  .title-dot-1 { fill: #ff5f56; }')
    svg_lines.append('  .title-dot-2 { fill: #ffbd2e; }')
    svg_lines.append('  .title-dot-3 { fill: #27c93f; }')
    svg_lines.append('  .title-text { fill: #8b949e; font-family: monospace; font-size: 11px; }')
    svg_lines.append('  .ascii-text { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; font-size: 7.5px; font-weight: bold; white-space: pre; }')
    
    # Animated gradient colors
    svg_lines.append('  @keyframes colorGlow {')
    svg_lines.append('    0% { fill: #58a6ff; }')
    svg_lines.append('    25% { fill: #bc8cff; }')
    svg_lines.append('    50% { fill: #39d353; }')
    svg_lines.append('    75% { fill: #f0883e; }')
    svg_lines.append('    100% { fill: #58a6ff; }')
    svg_lines.append('  }')
    
    svg_lines.append('  @keyframes colorGlowAlt {')
    svg_lines.append('    0% { fill: #79c0ff; }')
    svg_lines.append('    33% { fill: #d2a8ff; }')
    svg_lines.append('    66% { fill: #56d364; }')
    svg_lines.append('    100% { fill: #79c0ff; }')
    svg_lines.append('  }')

    svg_lines.append('  .c-name { animation: colorGlow 6s ease-in-out infinite; }')
    svg_lines.append('  .c-flammia { animation: colorGlowAlt 6s ease-in-out infinite; }')
    svg_lines.append('  .c-subtitle { fill: #39d353; font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 9px; font-weight: bold; }')
    svg_lines.append('  .c-sep { fill: #30363d; font-family: monospace; font-size: 9.5px; }')
    svg_lines.append('</style>')
    
    # Background card
    svg_lines.append(f'  <rect width="{width}" height="{height}" class="bg"/>')
    svg_lines.append(f'  <path d="M0 8 C0 3.58 3.58 0 8 0 L{width-8} 0 C{width-3.58} 0 {width} 3.58 {width} 8 L{width} 28 L0 28 Z" class="title-bar"/>')
    svg_lines.append('  <circle cx="15" cy="14" r="4" class="title-dot-1"/>')
    svg_lines.append('  <circle cx="27" cy="14" r="4" class="title-dot-2"/>')
    svg_lines.append('  <circle cx="39" cy="14" r="4" class="title-dot-3"/>')
    svg_lines.append('  <text x="54" y="18" class="title-text">gerardo@banner ~ ascii_name.sh</text>')
    
    # Defs for clip paths
    svg_lines.append('  <defs>')
    for i in range(total_rows):
        begin_time = i * duration_per_row
        svg_lines.append(f'    <clipPath id="clip-row-{i}">')
        svg_lines.append(f'      <rect x="8" y="{45 + i * row_height}" width="0" height="{row_height}">')
        svg_lines.append(f'        <animate attributeName="width" from="0" to="{width-16}" begin="{begin_time:.2f}s" dur="0.12s" fill="freeze"/>')
        svg_lines.append('      </rect>')
        svg_lines.append('    </clipPath>')
    svg_lines.append('  </defs>')
    
    # Render ASCII rows
    for i, line in enumerate(ASCII_NAME):
        y_pos = 110 + i * row_height
        escaped_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        
        css_class = "ascii-text c-name"
        if i >= 7 and i <= 12:
            css_class = "ascii-text c-flammia"
        elif i >= 15:
            css_class = "c-subtitle"
        elif "=" in line:
            css_class = "c-sep"
            
        svg_lines.append(f'  <g clip-path="url(#clip-row-{i})">')
        svg_lines.append(f'    <text x="12" y="{y_pos}" class="{css_class}">{escaped_line}</text>')
        svg_lines.append('  </g>')
        
    svg_lines.append('</svg>')
    
    output_path = os.path.join(os.path.dirname(__file__), "..", "ascii-art.svg")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_svg()
