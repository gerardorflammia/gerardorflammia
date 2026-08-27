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
    
    font_mono = 'monospace, ui-monospace, SFMono-Regular, Menlo, Consolas'
    
    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">')
    
    # Background card with inline attributes (bypasses GitHub style stripper)
    svg_lines.append(f'  <rect width="{width}" height="{height}" fill="#0d1117" rx="8" ry="8" stroke="#30363d" stroke-width="1"/>')
    svg_lines.append(f'  <path d="M0 8 C0 3.58 3.58 0 8 0 L{width-8} 0 C{width-3.58} 0 {width} 3.58 {width} 8 L{width} 28 L0 28 Z" fill="#161b22"/>')
    svg_lines.append('  <circle cx="15" cy="14" r="4" fill="#ff5f56"/>')
    svg_lines.append('  <circle cx="27" cy="14" r="4" fill="#ffbd2e"/>')
    svg_lines.append('  <circle cx="39" cy="14" r="4" fill="#27c93f"/>')
    svg_lines.append(f'  <text x="54" y="18" fill="#8b949e" font-family="{font_mono}" font-size="11">gerardo@banner ~ ascii_art.sh</text>')
    
    # Render ASCII rows directly with inline presentation attributes
    for i, line in enumerate(ASCII_NAME):
        y_pos = 110 + i * row_height
        escaped_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        
        fill_color = "#58a6ff"
        font_size = "7.5"
        
        if i >= 7 and i <= 12:
            fill_color = "#79c0ff"
        elif i >= 15:
            fill_color = "#39d353"
            font_size = "9"
        elif "=" in line:
            fill_color = "#30363d"
            font_size = "9.5"
            
        svg_lines.append(f'  <text x="12" y="{y_pos}" fill="{fill_color}" font-family="{font_mono}" font-size="{font_size}" font-weight="bold" xml:space="preserve">{escaped_line}</text>')
        
    svg_lines.append('</svg>')
    
    output_path = os.path.join(os.path.dirname(__file__), "..", "ascii-art-v2.svg")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_svg()
