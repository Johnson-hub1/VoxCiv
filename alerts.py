# alerts.py

from collections import Counter
from data_storage import fetch_reports
from text_analysis import extract_keywords_and_topics

# Alert rule configuration
ALERT_KEYWORDS = {
    "health": ["clinic", "medicine", "sick", "hospital"],
    "education": ["school", "teacher", "learning", "classroom"],
    "infrastructure": ["road", "bridge", "electricity", "pump", "water"],
    "security": ["theft", "attack", "violence", "fight"]
}

ALERT_THRESHOLD = 3  # Trigger alert if 3+ related reports

def generate_alerts():
    """Scan reports and generate alerts based on keyword frequency"""
    reports = fetch_reports()
    keyword_pool = []

    for report in reports:
        keywords = extract_keywords_and_topics(report["message"])
        keyword_pool.extend(keywords)

    keyword_freq = Counter(keyword_pool)
    alerts = []

    for category, keywords in ALERT_KEYWORDS.items():
        category_count = sum(keyword_freq[k] for k in keywords if k in keyword_freq)

        if category_count >= ALERT_THRESHOLD:
            alerts.append({
                "category": category,
                "keywords_triggered": [k for k in keywords if k in keyword_freq],
                "total_mentions": category_count
            })

    return alerts

if __name__ == "__main__":
    print("🚨 Running VoxCiv Alert Engine...\n")
    alerts = generate_alerts()

    if alerts:
        for alert in alerts:
            print(f"[ALERT] 🚨 {alert['category'].upper()} CRISIS DETECTED!")
            print(f" - Keywords: {', '.join(alert['keywords_triggered'])}")
            print(f" - Total Mentions: {alert['total_mentions']}")
            print()
    else:
        print("✅ No major issues detected at the moment.")
