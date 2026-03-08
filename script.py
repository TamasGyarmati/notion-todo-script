import os
from notion_client import Client

notion = Client(auth=os.environ["NOTION_TOKEN"])

page_id = os.environ["NOTION_PAGE_ID"]

child_pages = notion.blocks.children.list(block_id=page_id)

for child in child_pages["results"]:
    if child["type"] == "child_page":
        day_title = child["child_page"]["title"]
        day_id = child["id"]
        print(f"Resetting {day_title} ...")

        if day_title == "Tanulnivalók":
            print(f"Skipping {day_title}")
            continue

        blocks = notion.blocks.children.list(block_id=day_id)
        for block in blocks["results"]:
            if block["type"] == "to_do":
                notion.blocks.delete(block_id=block["id"])

        updated_blocks = notion.blocks.children.list(block_id=day_id)["results"]

        for block in updated_blocks:
            if block["type"] == "paragraph":
                rich_text = block["paragraph"]["rich_text"]
                if rich_text:
                    text_content = block["paragraph"]["rich_text"][0]["plain_text"].strip().lower()
                    if text_content == "to-do":
                        print(f" - Új üres mező beszúrása a(z) '{text_content}' alá")
                        notion.blocks.children.append(
                            block_id=day_id,
                            after=block["id"],
                            children=[
                                {
                                    "object": "block",
                                    "type": "to_do",
                                    "to_do": {
                                        "rich_text": [],
                                        "checked": False
                                    }
                                }
                            ]
                        )
                    elif text_content == "egyéb":
                        print(f" - Új üres mező beszúrása a(z) '{text_content}' alá")
                        notion.blocks.children.append(
                            block_id=day_id,
                            after=block["id"],
                            children=[
                                {
                                    "object": "block",
                                    "type": "to_do",
                                    "to_do": {
                                        "rich_text": [{"type": "text", "text": {"content": "Weight - in"}}],
                                        "checked": False
                                    }
                                },
                                {
                                    "object": "block",
                                    "type": "to_do",
                                    "to_do": {
                                        "rich_text": [{"type": "text", "text": {"content": "1800 kcal"}}],
                                        "checked": False
                                    }
                                }
                            ]
                        )