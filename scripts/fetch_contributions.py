import os
import json
import datetime
import requests
from bs4 import BeautifulSoup

USERNAME = "gerardorflammia"
URL = f"https://github.com/users/{USERNAME}/contributions"

LEVEL_MAP = {
    "NONE": 0,
    "FIRST_QUARTILE": 1,
    "SECOND_QUARTILE": 2,
    "THIRD_QUARTILE": 3,
    "FOURTH_QUARTILE": 4
}

def fetch_via_graphql(token):
    headers = {
        "Authorization": f"bearer {token}",
        "User-Agent": "Python-Contribution-Fetcher"
    }
    query = """
    query($login: String!) {
      user(login: $login) {
        contributionsCollection {
          contributionCalendar {
            totalContributions
            weeks {
              contributionDays {
                date
                contributionCount
                contributionLevel
              }
            }
          }
        }
      }
    }
    """
    print(f"Fetching contribution calendar via GitHub GraphQL API for {USERNAME}...")
    res = requests.post("https://api.github.com/graphql", json={"query": query, "variables": {"login": USERNAME}}, headers=headers)
    if res.status_code == 200:
        data = res.json()
        if "data" in data and data["data"].get("user"):
            calendar = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
            days_data = []
            for week in calendar["weeks"]:
                for day in week["contributionDays"]:
                    level_str = day.get("contributionLevel", "NONE")
                    days_data.append({
                        "date": day["date"],
                        "count": day["contributionCount"],
                        "level": LEVEL_MAP.get(level_str, 0)
                    })
            return days_data, calendar.get("totalContributions", sum(d["count"] for d in days_data))
    print(f"GraphQL request failed (status {res.status_code}). Falling back to HTML scraping.")
    return None, 0

def fetch_via_html():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
    
    print(f"Fetching public contributions for {USERNAME} from {URL}...")
    response = requests.get(URL, headers=headers)
    if response.status_code != 200:
        print(f"Warning: Failed to fetch contributions page (status {response.status_code}). Using fallback data.")
        return generate_fallback_days(), 0
        
    soup = BeautifulSoup(response.text, "html.parser")
    days_data = []
    
    tooltips = {}
    for tool_tip in soup.find_all("tool-tip"):
        for_id = tool_tip.get("for")
        if for_id:
            tooltips[for_id] = tool_tip.text.strip()
            
    day_cells = soup.find_all("td", class_="ContributionCalendar-day")
    if not day_cells:
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
            level = int(level_str) if level_str.isdigit() else 0
            count = level * 2 if level > 0 else 0

        days_data.append({
            "date": date_str,
            "count": count,
            "level": int(level_str) if level_str.isdigit() else 0
        })
        
    if not days_data:
        days_data = generate_fallback_days()
        
    return days_data, sum(d["count"] for d in days_data)

def generate_fallback_days():
    today = datetime.date.today()
    days = []
    for i in range(371, -1, -1):
        d = today - datetime.timedelta(days=i)
        days.append({
            "date": d.isoformat(),
            "count": 0,
            "level": 0
        })
    return days

def fetch_and_parse_contributions():
    token = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN")
    days_data = None
    total_contributions = 0
    
    if token:
        days_data, total_contributions = fetch_via_graphql(token)
        
    if not days_data:
        days_data, total_contributions = fetch_via_html()

    days_data.sort(key=lambda x: x["date"])
    
    if total_contributions == 0:
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

if __name__ == "__main__":
    fetch_and_parse_contributions()
