# Steam Manifest Downloader (SMD)

Quick thing before we start remember to exclude SMD folder Windows Security or at least the folder in this path for Creaminstaller Resources to work! smd\dlc_unlockers\resources

SMD helps you set up games to work with Steam using Lua files and related data. It writes the right files into your Steam folder so games and DLC can run. It does not replace or crack Steam itself.

**Need help?** Check the [documentation](docs/README.md), the [Troubleshooting](docs/TROUBLESHOOTING.md) guide or just Reach out to jericjan on the discord server and we'll sort it out: https://discord.gg/bK667akcjn

## Quick start

Before doing anything after you install it first thing to do just to make sure everything works run `pip install -r requirements.txt`

**If you have the EXE**  
Run SMD.exe and follow the prompts. You'll need GreenLuma installed; see the Setup Guide for the download link.

**If you use Python**  
1. Install dependencies: `pip install -r requirements.txt`  
2. Run: `python Main.py`  or use `simple_build.bat` to get exe instead of using python everytime.
3. Optional (Windows desktop notifications): `pip install -r requirements-optional.txt`

**GreenLuma**  
SMD works with GreenLuma. You need to download and set up GreenLuma yourself:  
(https://www.up-4ever.net/h3vt78x7jdap)

Extract the ZIP and use the AppList folder from GreenLuma when SMD asks for it. Full steps are in the [Setup Guide](docs/SETUP_GUIDE.md).

## What SMD can do

- Download and use Lua files for games, download manifests, and set up GreenLuma.  
- Write Lua and manifest data into Steam's config so games work with or without an extra injector.  
- On Windows, optionally patch Steam (using two DLLs in the steam_patch folder) so Steam reads that data without replacing Steam.exe.  
- Other features: multiplayer fixes (online-fix.me), DLC status check, cracking (gbe_fork), SteamStub DRM removal (Steamless), AppList management, and DLC Unlockers (CreamInstaller-style: SmokeAPI, CreamAPI, Koaloader, Uplay).  
- Parallel downloads, backups, recent files, and settings export/import.

## Documentation

[Documentation index](docs/README.md) – Start here.

[Setup Guide](docs/SETUP_GUIDE.md) – What to install (including GreenLuma and the optional Steam patch).

[User Guide](docs/USER_GUIDE.md) – What each menu option does and how to add games.

[Quick Reference](docs/QUICK_REFERENCE.md) – Commands and shortcuts.

[Feature Guide](docs/FEATURE_USAGE_GUIDE.md) – Parallel downloads, backups, library scanner, and more.

[Multiplayer Fix](docs/MULTIPLAYER_FIX.md) – Using the online-fix.me multiplayer fix.

[DLC Unlockers](docs/dlc_unlockers/README.md) – Using DLC unlockers (CreamInstaller-style).

[Troubleshooting](docs/TROUBLESHOOTING.md) – Common problems and what to try.

## Credits

Original author: **jericjan** – SMD/Steam Manifest Downloader was originally made by jericjan and just modified by me adding more features etc.  

Credit to RedPaper for the Broken Moon MIDI cover, originally arranged by U2 Akiyama and used in Touhou 7.5: Immaterial and Missing Power. Touhou 7.5 and its related assets are owned by Team Shanghai Alice and Twilight Frontier. SMD is not affiliated with, endorsed by, or sponsored by either party. All trademarks belong to their respective owners.

**CreamInstaller** – The DLC Unlockers feature in SMD is inspired by and compatible with CreamInstaller. SMD does not ship CreamInstaller; it provides its own implementation that follows similar behavior.

modified version by me of jericjan/SMD

Use SMD at your own responsibility.
