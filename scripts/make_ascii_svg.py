import os

ASCII_NAME = [
    "  ██████╗ ███████╗██████╗  █████╗ ██████╗ ██████╗  ██████╗ ",
    " ██╔════╝ ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔═══██╗",
    " ██║  ███╗█████╗  ██████╔╝███████║██████╔╝██║  ██║██║   ██║",
    " ██║   ██║██╔══╝  ██╔══██╗██╔══██║██╔══██╗██║  ██║██║   ██║",
    " ╚██████╔╝███████╗██║  ██║██║  ██║██║  ██║██████╔╝╚██████╔╝",
    "  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ",
    "",
    " ███████╗██╗      █████╗ ███╗   ███╗███╗   ███╗██╗█████╗  ",
    " ██╔════╝██║     ██╔══██╗████╗ ████║████╗ ████║██║██╔══██╗",
    " █████╗  ██║     ███████║██╔████╔██║██╔████╔██║██║███████║",
    " ██╔══╝  ██║     ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██║██╔══██║",
    " ██║     ███████╗██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║██║  ██║",
    " ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═╝",
    "",
    "===========================================================",
    "      R&D ENGINEER | BACKEND & AI | AUTOMATIONS            ",
    "===========================================================",
]

def generate_svg():
    width = 860
    height = 360  # Increased height to eliminate any bottom clipping
    row_height = 175 // len(ASCII_NAME) if len(ASCII_NAME) > 0 else 18
    row_height = max(18, row_height)
    font_mono = 'monospace, ui-monospace, SFMono-Regular, Menlo, Consolas'
    
    svg_lines = []
    svg_lines.append('<?xml version="1.0" encoding="UTF-8"?>')
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">')
    
    # Background card
    svg_lines.append(f'  <rect width="{width}" height="{height}" fill="#0d1117" rx="8" ry="8" stroke="#30363d" stroke-width="1"/>')
    svg_lines.append(f'  <path d="M0 8 C0 3.58 3.58 0 8 0 L{width-8} 0 C{width-3.58} 0 {width} 3.58 {width} 8 L{width} 28 L0 28 Z" fill="#161b22"/>')
    svg_lines.append('  <circle cx="15" cy="14" r="4" fill="#ff5f56"/>')
    svg_lines.append('  <circle cx="27" cy="14" r="4" fill="#ffbd2e"/>')
    svg_lines.append('  <circle cx="39" cy="14" r="4" fill="#27c93f"/>')
    svg_lines.append(f'  <text x="54" y="18" fill="#8b949e" font-family="{font_mono}" font-size="11">gerardo@banner ~ ascii_art.sh</text>')
    
    center_x = width // 2  # 430px exact horizontal center
    
    # Render ASCII rows perfectly centered horizontally using text-anchor="middle"
    for i, line in enumerate(ASCII_NAME):
        y_pos = 58 + i * 17
        escaped_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        
        fill_color = "#58a6ff"
        font_size = "12"
        anim_tag = ""
        
        if i <= 5:
            fill_color = "#58a6ff"
            anim_tag = '<animate attributeName="fill" values="#58a6ff;#bc8cff;#39d353;#f0883e;#58a6ff" dur="6s" repeatCount="indefinite"/>'
        elif i >= 7 and i <= 12:
            fill_color = "#79c0ff"
            anim_tag = '<animate attributeName="fill" values="#79c0ff;#d2a8ff;#56d364;#ffa657;#79c0ff" dur="6s" repeatCount="indefinite"/>'
        elif i >= 15:
            fill_color = "#39d353"
            font_size = "12"
        elif "=" in line:
            fill_color = "#30363d"
            font_size = "12"
            
        svg_lines.append(f'  <text x="{center_x}" y="{y_pos}" fill="{fill_color}" font-family="{font_mono}" font-size="{font_size}" font-weight="bold" text-anchor="middle" xml:space="preserve">{anim_tag}{escaped_line}</text>')
        
    svg_lines.append('</svg>')
    
    out1 = os.path.join(os.path.dirname(__file__), "..", "ascii-art.svg")
    out2 = os.path.join(os.path.dirname(__file__), "..", "ascii-art-v2.svg")
    with open(out1, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))
    with open(out2, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))
    print(f"Generated centered {out1} and {out2}")

if __name__ == "__main__":
    generate_svg()
