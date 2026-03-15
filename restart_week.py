import os
from notion_client import Client
from datetime import datetime

notion = Client(auth=os.environ["NOTION_TOKEN"])
page_id = os.environ["NOTION_PAGE_ID"]

KCAL_LIMIT = 1800
today = datetime.now().weekday()

if today == 6:
    target_days = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat"]
    print("Sunday mode: Resetting Monday - Saturday")
elif today == 0:
    target_days = ["Vasárnap"]
    print("Monday mode: Resetting Sunday")
else:
    print("Nothing to update. Script exitting...")
    exit()

child_pages = notion.blocks.children.list(block_id=page_id)

for child in child_pages["results"]:
    if child["type"] == "child_page":
        day_title = child["child_page"]["title"]
        day_id = child["id"]
        
        if day_title in target_days:
            print(f"Resetting {day_title} ...")

            notion.pages.update(page_id=day_id, icon={"type": "emoji", "emoji": "☑️"})

            blocks = notion.blocks.children.list(block_id=day_id)
            for block in blocks["results"]:
                if block["type"] == "to_do" or block["type"] == "toggle":
                    notion.blocks.delete(block_id=block["id"])

            updated_blocks = notion.blocks.children.list(block_id=day_id)["results"]

            for block in updated_blocks:
                if block["type"] == "paragraph" and block["paragraph"]["rich_text"]:
                        text_content = block["paragraph"]["rich_text"][0]["plain_text"].strip().lower()
                        if text_content == "to-do":
                            print(f" - New empty field inserted below '{text_content}'")
                            notion.blocks.children.append(block_id=day_id, after=block["id"], children=[
                                {"object": "block", "type": "to_do", "to_do": {"rich_text": [],"checked": False}}
                            ])
                        elif text_content == "egyéb":
                            print(f" - New empty field inserted below '{text_content}'")
                            notion.blocks.children.append(block_id=day_id, after=block["id"], children=[
                                {"object": "block", "type": "to_do", "to_do": {"rich_text": [{"type": "text", "text": {"content": "Weight - in"}}], "checked": False}},
                                {"object": "block", "type": "to_do", "to_do": {"rich_text": [{"type": "text", "text": {"content": f"{KCAL_LIMIT} kcal"}}], "checked": False}}
                            ])