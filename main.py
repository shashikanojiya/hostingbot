from pyrogram import Client, filters
import os, json
from runner import start_bot

BOT_TOKEN = "8589908424:AAHAcii-gs4gBZ3NXximi-qGJVwcbqspfHI"
API_ID = 23808998
API_HASH = "68881532c4bad1f35a2658663d3894c0"

app = Client(
    "hostingbot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

DATA_FILE = "users.json"
BOT_FOLDER = "user_bots"

os.makedirs(BOT_FOLDER, exist_ok=True)

def load():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE) as f:
        return json.load(f)

def save(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# START COMMAND
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "🤖 Welcome to FREE HOSTING BOT\n\n"
        "📤 Apni Python bot file (.py) bhejo\n"
        "⚠️ Ek user sirf 5 bots chala sakta hai"
    )

# FILE RECEIVE
@app.on_message(filters.document)
async def upload(client, message):

    if not message.document.file_name.endswith(".py"):
        return await message.reply("❌ Sirf Python (.py) file bhejo!")

    user_id = str(message.from_user.id)
    data = load()

    if user_id not in data:
        data[user_id] = []

    # LIMIT 5
    if len(data[user_id]) >= 5:
        return await message.reply("🚫 Tum already 5 bots chala rahe ho!")

    file_path = await message.download(f"{BOT_FOLDER}/{user_id}_{message.document.file_name}")

    ok = start_bot(file_path)

    if ok:
        data[user_id].append(file_path)
        save(data)
        await message.reply("✅ Tumhara bot start ho gaya (24/7 online)")
    else:
        await message.reply("❌ Bot start nahi ho paya!")

app.run()