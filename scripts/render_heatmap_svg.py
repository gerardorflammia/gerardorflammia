import os
import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]
MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
DAY_NAMES = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

def render_heatmap():
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "contributions.json")
    if not os.path.exists(data_path):
        print(f"Data file not found at {data_path}. Please run fetch_contributions.py first.")
        return
        
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    days = data.get("days", [])
    total_contribs = data.get("total_contributions", 0)
    current_streak = data.get("current_streak", 0)
    longest_streak = data.get("longest_streak", 0)
    
    width = 860
    height = 200
    
    box_size = 11
    box_gap = 3.5
    start_x = 45
    start_y = 55
    
    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">')
    svg_lines.append('<style>')
    svg_lines.append('  .bg { fill: #0d1117; rx: 8px; ry: 8px; stroke: #30363d; stroke-width: 1px; }')
    svg_lines.append('  .title-bar { fill: #161b22; }')
    svg_lines.append('  .title-dot-1 { fill: #ff5f56; }')
    svg_lines.append('  .title-dot-2 { fill: #ffbd2e; }')
    svg_lines.append('  .title-dot-3 { fill: #27c93f; }')
    svg_lines.append('  .title-text { fill: #8b949e; font-family: monospace; font-size: 11px; }')
    svg_lines.append('  .label-text { fill: #7d8590; font-family: monospace; font-size: 10px; }')
    svg_lines.append('  .footer-text { fill: #8b949e; font-family: monospace; font-size: 11px; font-weight: bold; }')
    svg_lines.append('  .stat-highlight { fill: #39d353; font-family: monospace; font-size: 11px; font-weight: bold; }')
    
    # Keyframe animation for diagonal reveal
    svg_lines.append('  @keyframes slideIn {')
    svg_lines.append('    from { opacity: 0; transform: scale(0.4) translateY(-10px); }')
    svg_lines.append('    to { opacity: 1; transform: scale(1) translateY(0); }')
    svg_lines.append('  }')
    svg_lines.append('  .day-cell { animation: slideIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards; opacity: 0; transform-origin: center; rx: 2px; ry: 2px; }')
    svg_lines.append('</style>')
    
    # Card layout
    svg_lines.append(f'  <rect width="{width}" height="{height}" class="bg"/>')
    svg_lines.append(f'  <path d="M0 8 C0 3.58 3.58 0 8 0 L{width-8} 0 C{width-3.58} 0 {width} 3.58 {width} 8 L{width} 28 L0 28 Z" class="title-bar"/>')
    svg_lines.append('  <circle cx="15" cy="14" r="4" class="title-dot-1"/>')
    svg_lines.append('  <circle cx="27" cy="14" r="4" class="title-dot-2"/>')
    svg_lines.append('  <circle cx="39" cy="14" r="4" class="title-dot-3"/>')
    svg_lines.append('  <text x="54" y="18" class="title-text">gerardo@github ~ ./contributions.sh</text>')
    
    # Day of week labels (Mon, Wed, Fri)
    for day_idx, day_name in [(1, "Mon"), (3, "Wed"), (5, "Fri")]:
        y = start_y + day_idx * (box_size + box_gap) + 9
        svg_lines.append(f'  <text x="20" y="{y}" class="label-text">{day_name}</text>')
        
    # Render 53 weeks x 7 days grid
    # Organize days into 53 weeks (columns)
    weeks = []
    current_week = []
    
    for d in days:
        current_week.append(d)
        if len(current_week) == 7:
            weeks.append(current_week)
            current_week = []
    if current_week:
        weeks.append(current_week)
        
    weeks = weeks[-53:] # Ensure max 53 weeks
    
    # Month labels along the top
    last_month = -1
    for w_idx, week in enumerate(weeks):
        if week:
            date_parts = week[0]["date"].split("-")
            month_num = int(date_parts[1])
            if month_num != last_month and w_idx % 4 == 0:
                last_month = month_num
                month_name = MONTH_NAMES[month_num - 1]
                x = start_x + w_idx * (box_size + box_gap)
                svg_lines.append(f'  <text x="{x}" y="{start_y - 8}" class="label-text">{month_name}</text>')
                
    # Draw contribution day boxes
    for w_idx, week in enumerate(weeks):
        for d_idx, day_item in enumerate(week):
            x = start_x + w_idx * (box_size + box_gap)
            y = start_y + d_idx * (box_size + box_gap)
            
            level = day_item.get("level", 0)
            color = PALETTE[min(level, len(PALETTE)-1)]
            
            # Diagonal animation delay calculation (w_idx + d_idx)
            delay = (w_idx + d_idx) * 0.012
            
            tooltip = f'{day_item["count"]} contributions on {day_item["date"]}'
            svg_lines.append(f'  <rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" fill="{color}" class="day-cell" style="animation-delay: {delay:.3f}s;">')
            svg_lines.append(f'    <title>{tooltip}</title>')
            svg_lines.append('  </rect>')
            
    # Footer stats & Legend
    footer_y = start_y + 7 * (box_size + box_gap) + 24
    
    # Stats on the left
    stats_str = f'Total Contributions: <tspan class="stat-highlight">{total_contribs}</tspan> | Current Streak: <tspan class="stat-highlight">{current_streak} days</tspan> | Longest Streak: <tspan class="stat-highlight">{longest_streak} days</tspan>'
    svg_lines.append(f'  <text x="{start_x}" y="{footer_y}" class="footer-text">{stats_str}</text>')
    
    # Less -> More legend on the right
    legend_start_x = width - 140
    svg_lines.append(f'  <text x="{legend_start_x - 32}" y="{footer_y}" class="label-text">Less</text>')
    for idx, c in enumerate(PALETTE):
        lx = legend_start_x + idx * (11 + 3)
        ly = footer_y - 9
        svg_lines.append(f'  <rect x="{lx}" y="{ly}" width="11" height="11" fill="{c}" rx="2" ry="2"/>')
    svg_lines.append(f'  <text x="{legend_start_x + len(PALETTE)*(11+3) + 4}" y="{footer_y}" class="label-text">More</text>')
    
    svg_lines.append('</svg>')
    
    out_path = os.path.join(os.path.dirname(__file__), "..", "contrib-heatmap.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))
    print(f"Generated {out_path}")

if __name__ == "__main__":
    render_heatmap()
