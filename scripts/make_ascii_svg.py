import os

ASCII_ART = [
    "                 ___________________________________",
    "               /                                     \\",
    "              |   ______  _   _  ______  _____  _____ |",
    "              |  |  ____|| \\ | ||  ____||  ___||  ___||",
    "              |  | |__   |  \\| || |__   | |__  | |__  |",
    "              |  |  __|  | . ` ||  __|  |  __| |  __| |",
    "              |  | |____ | |\\  || |____ | |____| |____|",
    "              |  |______||_| \\_||______||______||_____|",
    "               \\_____________________________________/",
    "",
    "                   .-----------------------.",
    "                 /   ____________________   \\",
    "                /   /                    \\   \\",
    "             .-'   /     ,----------.     \\   '-.",
    "           .'     /     /  .------.  \\\\     '.",
    "          /      /     /  /  __  __ \\ \\     \\      \\",
    "         |      |     |  |  /  \\/  \\ | |     |      |",
    "  \\  /   |      |     |  |  \\__/\\__/ | |     |      |   \\  /",
    "   \\/     \\     |     |   \\    /\\   /  |     |     /     \\/",
    "   /\\      \\     \\     \\   '--'  '--' /     /     /      /\\",
    "  /  \\      '-.   \\     '------------'     /   .-'      /  \\",
    "               '-. \\                      / .-'",
    "                  '----------------------'",
    "",
    "             🏴‍☠️ STRAW HAT PIRATES // ONE PIECE 🏴‍☠️",
    "            \"I'm gonna be the King of the Pirates!\"",
    "                          - Luffy -",
]

def generate_svg():
    row_height = 14
    total_rows = len(ASCII_ART)
    width = 370
    height = max(420, total_rows * row_height + 40)
    
    # Calculate staggered animation timings
    duration_per_row = 0.08
    total_anim_time = total_rows * duration_per_row + 0.5
    
    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">')
    svg_lines.append('<style>')
    svg_lines.append('  .bg { fill: #0d1117; rx: 8px; ry: 8px; stroke: #30363d; stroke-width: 1px; }')
    svg_lines.append('  .title-bar { fill: #161b22; }')
    svg_lines.append('  .title-dot-1 { fill: #ff5f56; }')
    svg_lines.append('  .title-dot-2 { fill: #ffbd2e; }')
    svg_lines.append('  .title-dot-3 { fill: #27c93f; }')
    svg_lines.append('  .title-text { fill: #8b949e; font-family: monospace; font-size: 11px; }')
    svg_lines.append('  .ascii-text { font-family: "Courier New", Courier, monospace; font-size: 9px; fill: #e6edf3; font-weight: bold; white-space: pre; }')
    svg_lines.append('  .accent-text { fill: #58a6ff; font-family: "Courier New", Courier, monospace; font-size: 10px; font-weight: bold; }')
    svg_lines.append('  .highlight-text { fill: #f0883e; font-family: "Courier New", Courier, monospace; font-size: 10px; font-weight: bold; }')
    svg_lines.append('</style>')
    
    # Background card
    svg_lines.append(f'  <rect width="{width}" height="{height}" class="bg"/>')
    svg_lines.append(f'  <path d="M0 8 C0 3.58 3.58 0 8 0 L{width-8} 0 C{width-3.58} 0 {width} 3.58 {width} 8 L{width} 28 L0 28 Z" class="title-bar"/>')
    svg_lines.append('  <circle cx="15" cy="14" r="4" class="title-dot-1"/>')
    svg_lines.append('  <circle cx="27" cy="14" r="4" class="title-dot-2"/>')
    svg_lines.append('  <circle cx="39" cy="14" r="4" class="title-dot-3"/>')
    svg_lines.append('  <text x="54" y="18" class="title-text">gerardo@onepiece ~ ascii_art.sh</text>')
    
    # Defs for clip paths
    svg_lines.append('  <defs>')
    for i in range(total_rows):
        begin_time = i * duration_per_row
        svg_lines.append(f'    <clipPath id="clip-row-{i}">')
        svg_lines.append(f'      <rect x="10" y="{35 + i * row_height}" width="0" height="{row_height}">')
        svg_lines.append(f'        <animate attributeName="width" from="0" to="{width-20}" begin="{begin_time:.2f}s" dur="0.1s" fill="freeze"/>')
        svg_lines.append('      </rect>')
        svg_lines.append('    </clipPath>')
    svg_lines.append('  </defs>')
    
    # Render ASCII rows
    for i, line in enumerate(ASCII_ART):
        y_pos = 46 + i * row_height
        escaped_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        
        css_class = "ascii-text"
        if "ONE PIECE" in line or "STRAW HAT" in line:
            css_class = "highlight-text"
        elif "Luffy" in line or "King of the Pirates" in line:
            css_class = "accent-text"
            
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
