import os

CARD_DATA = [
    ("Title / Degree", "Electronic Engineer (Ingeniero Electrónico en Computación)"),
    ("Specialization", "Backend Development, AI Integration & Workflow Automations"),
    ("Future Goal", "Pursuing a Master's Degree in Artificial Intelligence"),
    ("Core Interests", "Backend Engineering, AI Systems, Automations & Tech"),
    ("Main Stack", "Python, PHP, JavaScript, SQL, C/C++, n8n, Docker, Git"),
    ("Featured Project", "Automated Expense System (Gemini 2.5 Flash + n8n + PHP)"),
    ("Location", "Venezuela"),
    ("LinkedIn", "linkedin.com/in/gerardo-rodrigues-flammia-1a6522302"),
    ("GitHub", "github.com/gerardorflammia"),
]

def generate_info_card():
    width = 490
    height = 420
    
    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">')
    svg_lines.append('<style>')
    svg_lines.append('  .bg { fill: #0d1117; rx: 8px; ry: 8px; stroke: #30363d; stroke-width: 1px; }')
    svg_lines.append('  .title-bar { fill: #161b22; }')
    svg_lines.append('  .title-dot-1 { fill: #ff5f56; }')
    svg_lines.append('  .title-dot-2 { fill: #ffbd2e; }')
    svg_lines.append('  .title-dot-3 { fill: #27c93f; }')
    svg_lines.append('  .title-text { fill: #8b949e; font-family: monospace; font-size: 11px; }')
    svg_lines.append('  .header-name { fill: #58a6ff; font-family: monospace; font-size: 15px; font-weight: bold; }')
    svg_lines.append('  .header-sep { fill: #30363d; font-family: monospace; font-size: 13px; }')
    svg_lines.append('  .key-text { fill: #79c0ff; font-family: monospace; font-size: 11px; font-weight: bold; }')
    svg_lines.append('  .val-text { fill: #c9d1d9; font-family: monospace; font-size: 11px; }')
    svg_lines.append('  .link-text { fill: #a5d6ff; font-family: monospace; font-size: 11px; text-decoration: underline; }')
    svg_lines.append('  .color-block { font-family: monospace; font-size: 13px; }')
    
    # CSS animations
    svg_lines.append('  @keyframes fadeIn {')
    svg_lines.append('    from { opacity: 0; transform: translateY(5px); }')
    svg_lines.append('    to { opacity: 1; transform: translateY(0); }')
    svg_lines.append('  }')
    svg_lines.append('  .animated-row { animation: fadeIn 0.4s ease-out forwards; opacity: 0; }')
    svg_lines.append('</style>')
    
    # Background card
    svg_lines.append(f'  <rect width="{width}" height="{height}" class="bg"/>')
    svg_lines.append(f'  <path d="M0 8 C0 3.58 3.58 0 8 0 L{width-8} 0 C{width-3.58} 0 {width} 3.58 {width} 8 L{width} 28 L0 28 Z" class="title-bar"/>')
    svg_lines.append('  <circle cx="15" cy="14" r="4" class="title-dot-1"/>')
    svg_lines.append('  <circle cx="27" cy="14" r="4" class="title-dot-2"/>')
    svg_lines.append('  <circle cx="39" cy="14" r="4" class="title-dot-3"/>')
    svg_lines.append('  <text x="54" y="18" class="title-text">gerardo@github ~ neofetch</text>')
    
    # User header line
    svg_lines.append('  <g class="animated-row" style="animation-delay: 0.1s;">')
    svg_lines.append('    <text x="20" y="55" class="header-name">gerardorflammia</text>')
    svg_lines.append('    <text x="165" y="55" class="header-name" fill="#d2a8ff">@</text>')
    svg_lines.append('    <text x="180" y="55" class="header-name" fill="#7ee787">backend-ai-dev</text>')
    svg_lines.append('    <text x="20" y="70" class="header-sep">--------------------------------------------------</text>')
    svg_lines.append('  </g>')
    
    start_y = 92
    y_step = 28
    
    for idx, (key, val) in enumerate(CARD_DATA):
        delay = 0.2 + idx * 0.08
        y_pos = start_y + idx * y_step
        
        svg_lines.append(f'  <g class="animated-row" style="animation-delay: {delay:.2f}s;">')
        svg_lines.append(f'    <text x="20" y="{y_pos}" class="key-text">{key}:</text>')
        
        is_link = "linkedin.com" in val or "github.com" in val
        val_class = "link-text" if is_link else "val-text"
        
        key_width_offset = 20 + max(115, len(key) * 8 + 10)
        svg_lines.append(f'    <text x="{key_width_offset}" y="{y_pos}" class="{val_class}">{val}</text>')
        svg_lines.append('  </g>')
        
    # Neofetch color blocks at bottom
    blocks_delay = 0.2 + len(CARD_DATA) * 0.08 + 0.1
    blocks_y = start_y + len(CARD_DATA) * y_step + 10
    svg_lines.append(f'  <g class="animated-row" style="animation-delay: {blocks_delay:.2f}s;">')
    svg_lines.append(f'    <text x="20" y="{blocks_y}" class="color-block">')
    svg_lines.append('      <tspan fill="#484f58">███</tspan>')
    svg_lines.append('      <tspan fill="#ff7b72">███</tspan>')
    svg_lines.append('      <tspan fill="#7ee787">███</tspan>')
    svg_lines.append('      <tspan fill="#ffa657">███</tspan>')
    svg_lines.append('      <tspan fill="#79c0ff">███</tspan>')
    svg_lines.append('      <tspan fill="#d2a8ff">███</tspan>')
    svg_lines.append('      <tspan fill="#f0883e">███</tspan>')
    svg_lines.append('      <tspan fill="#f0f6fc">███</tspan>')
    svg_lines.append('    </text>')
    svg_lines.append('  </g>')
    
    svg_lines.append('</svg>')
    
    output_path = os.path.join(os.path.dirname(__file__), "..", "info-card.svg")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_info_card()
