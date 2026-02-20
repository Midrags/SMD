# Before You Upload or Share

This folder is a **consumer-ready** copy of SMD with no personal data in the code.

## Never commit or upload these

- **settings.bin** – Stores your settings and (if you use them) encrypted passwords.
- **settings_export.json** – Export of settings; can contain paths and usernames.
- **debug.log**, **crash.log** – Logs that may contain paths.
- **recent_files.json**, **api_cache.json**, **analytics.json** – Local caches.
- **GreenLuma/**, **dlc_unlocker_cache/**, **backups/**, **saved_lua/** – Your own data.
- **build/**, **dist/** – Build outputs.

The **.gitignore** in this folder is already set so that these are ignored if you use Git.

## If you use Git

1. Copy this **MainTool_Consumers** folder (or its contents) to your repo.
2. Ensure **.gitignore** is present so the files above are never committed.
3. Run `git status` and confirm that `settings.bin`, `settings_export.json`, and the other listed files do **not** appear.

## Running SMD

- Install dependencies: `pip install -r requirements.txt`
- Optional (Windows notifications): `pip install win10toast`
- Run: `python Main.py`

Settings are saved in **settings.bin** in the same folder as Main.py. Each user gets their own file when they run the tool.
