import random
import requests

rows = []
handles = ["washingtonpost.com", "nytimes.com", "espn.com", "theguardian.com", "cnn.com", "wsj.com"]

for handle in handles:

    url = "https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed"
    feed = requests.get(url, params={"actor": handle, "limit": 4}).json()

    for item in feed["feed"]:
        post = item["post"]
        path = post["uri"][5:]
        theme = random.choice(["light", "dark"])

        rows.append({
            "source": handle,
            "text": post["record"]["text"],
            "embed_html": (
                f'<iframe src="https://embed.bsky.app/embed/{path}'
                f'?colorMode={theme}" width="100%" height="600" '
                f'style="border:0"></iframe>'
            ),
        })

newstweets = pd.DataFrame(rows)
