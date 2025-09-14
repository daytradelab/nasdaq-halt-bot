import requests
import time
import feedparser

DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1416894589272461313/TGuMhJgfxDzewtG0t7_Csg-3M9kHGocukYbMKhTXv_AAr5jcuRXgUW9mnz8cG7HL7G_P'
RSS_FEED_URL = 'https://www.nasdaqtrader.com/rss.aspx?feed=tradehalts'

seen_entries = set()

def post_to_discord(title, link):
    data = {
        "content": f"🛑 **New Stock Halt:** {title}\n🔗 [Details]({link})"
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code != 204:
        print(f"Failed to send message: {response.status_code} - {response.text}")

def check_feed():
    feed = feedparser.parse(RSS_FEED_URL)
    for entry in feed.entries:
        if entry.id not in seen_entries:
            seen_entries.add(entry.id)
            post_to_discord(entry.title, entry.link)

if __name__ == "__main__":
    while True:
        check_feed()
        time.sleep(60)
