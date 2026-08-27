import os

CARD_DATA = [
    ("Title / Degree", "Electronic Engineer (Ingeniero Electronico en Computacion)"),
    ("Specialization", "Backend Development, AI Systems & Workflow Automations"),
    ("Future Goal", "Pursuing a Master's Degree in Artificial Intelligence"),
    ("Core Interests", "Backend Engineering, AI Architecture, Automations & Tech"),
    ("Main Stack", "Python, PHP, JavaScript, SQL, C/C++, n8n, Docker, Git, Linux"),
    ("Featured Project", "Automated Expense Claims (Gemini 2.5 Flash + n8n + PHP + MySQL)"),
    ("Location", "Venezuela"),
    ("LinkedIn", "linkedin.com/in/gerardo-rodrigues-flammia-1a6522302"),
    ("GitHub", "github.com/gerardorflammia"),
]

def generate_info_card():
    width = 860
    height = 400
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
    svg_lines.append(f'  <text x="54" y="18" fill="#8b949e" font-family="{font_mono}" font-size="11">gerardo@github ~ neofetch</text>')
    
    # User header line
    svg_lines.append(f'  <text x="30" y="58" fill="#58a6ff" font-family="{font_mono}" font-size="16" font-weight="bold">gerardorflammia</text>')
    svg_lines.append(f'  <text x="180" y="58" fill="#d2a8ff" font-family="{font_mono}" font-size="16" font-weight="bold">@</text>')
    svg_lines.append(f'  <text x="200" y="58" fill="#7ee787" font-family="{font_mono}" font-size="16" font-weight="bold">backend-ai-dev</text>')
    svg_lines.append(f'  <text x="30" y="74" fill="#30363d" font-family="{font_mono}" font-size="13">--------------------------------------------------------------------------------</text>')
    
    start_y = 96
    y_step = 28
    
    for idx, (key, val) in enumerate(CARD_DATA):
        y_pos = start_y + idx * y_step
        svg_lines.append(f'  <text x="30" y="{y_pos}" fill="#79c0ff" font-family="{font_mono}" font-size="12" font-weight="bold">{key}:</text>')
        
        is_link = "linkedin.com" in val or "github.com" in val
        val_color = "#a5d6ff" if is_link else "#c9d1d9"
        key_width_offset = 200
        svg_lines.append(f'  <text x="{key_width_offset}" y="{y_pos}" fill="{val_color}" font-family="{font_mono}" font-size="12">{val}</text>')
        
    # Neofetch color blocks at bottom
    blocks_y = start_y + len(CARD_DATA) * y_step + 10
    colors = ["#484f58", "#ff7b72", "#7ee787", "#ffa657", "#79c0ff", "#d2a8ff", "#f0883e", "#f0f6fc"]
    svg_lines.append(f'  <text x="30" y="{blocks_y}" font-family="{font_mono}" font-size="14">')
    for c in colors:
        svg_lines.append(f'    <tspan fill="{c}">█████</tspan>')
    svg_lines.append('  </text>')
    
    svg_lines.append('</svg>')
    
    output_path = os.path.join(os.path.dirname(__file__), "..", "info-card.svg")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))
    print(f"Generated large 860px {output_path}")

if __name__ == "__main__":
    generate_info_card()
