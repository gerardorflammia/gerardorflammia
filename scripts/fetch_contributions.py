import os
import json
import datetime
import requests
from bs4 import BeautifulSoup

USERNAME = "gerardorflammia"
URL = f"https://github.com/users/{USERNAME}/contributions"

def fetch_and_parse_contributions():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
    
    print(f"Fetching contributions for {USERNAME} from {URL}...")
    response = requests.get(URL, headers=headers)
    if response.status_code != 200:
        print(f"Warning: Failed to fetch contributions page (status {response.status_code}). Using fallback data.")
        days_data = generate_fallback_days()
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        days_data = []
        
        # GitHub contribution cells are td elements with class ContributionCalendar-day or tooltips
        tooltips = {}
        for tool_tip in soup.find_all("tool-tip"):
            for_id = tool_tip.get("for")
            if for_id:
                tooltips[for_id] = tool_tip.text.strip()
                
        day_cells = soup.find_all("td", class_="ContributionCalendar-day")
        if not day_cells:
            # Fallback for SVG / table layout variations
            day_cells = soup.find_all("rect", class_="ContributionCalendar-day")
            
        for cell in day_cells:
            date_str = cell.get("data-date")
            level_str = cell.get("data-level", "0")
            cell_id = cell.get("id")
            
            if not date_str:
                continue
                
            count = 0
            tooltip_text = tooltips.get(cell_id, "")
            if tooltip_text and "contribution" in tooltip_text:
                try:
                    parts = tooltip_text.split(" ")
                    if parts[0].isdigit():
                        count = int(parts[0])
                    elif parts[0] == "No":
                        count = 0
                except Exception:
                    count = int(level_str) if level_str.isdigit() else 0
            else:
                # Approximate count from level if tooltip parse fails
                level = int(level_str) if level_str.isdigit() else 0
                count = level * 2 if level > 0 else 0

            days_data.append({
                "date": date_str,
                "count": count,
                "level": int(level_str) if level_str.isdigit() else 0
            })
            
        if not days_data:
            print("No day cells found in response HTML. Generating fallback data.")
            days_data = generate_fallback_days()

    # Sort days by date
    days_data.sort(key=lambda x: x["date"])
    
    # Calculate stats
    total_contributions = sum(d["count"] for d in days_data)
    current_streak = 0
    longest_streak = 0
    temp_streak = 0
    best_day = {"date": "", "count": 0}
    
    for d in days_data:
        cnt = d["count"]
        if cnt > best_day["count"]:
            best_day = {"date": d["date"], "count": cnt}
            
        if cnt > 0:
            temp_streak += 1
            if temp_streak > longest_streak:
                longest_streak = temp_streak
        else:
            temp_streak = 0
            
    # Calculate current streak up to today/yesterday
    for d in reversed(days_data):
        if d["count"] > 0:
            current_streak += 1
        else:
            break
            
    result = {
        "username": USERNAME,
        "updated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_contributions": total_contributions,
        "current_streak": current_streak,
        "longest_streak": longest_streak,
        "best_day": best_day,
        "days": days_data
    }
    
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    os.makedirs(data_dir, exist_ok=True)
    out_file = os.path.join(data_dir, "contributions.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
        
    print(f"Saved {len(days_data)} days of contribution data to {out_file} (Total: {total_contributions})")

def generate_fallback_days():
    # 53 weeks * 7 days = 371 days ending today
    today = datetime.date.today()
    days = []
    for i in range(371, -1, -1):
        d = today - datetime.timedelta(days=i)
        days.append({
            "date": d.isoformat(),
            "count": (i % 5 if i % 3 == 0 else 0),
            "level": (1 if i % 3 == 0 else 0)
        })
    return days

if __name__ == "__main__":
    fetch_and_parse_contributions()
