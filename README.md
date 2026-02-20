# Steam Manifest Downloader (SMD)

Quick thing before we start remember to exclude SMD folder Windows Security or at least the folder in this path for Creaminstaller Resources to work! smd\dlc_unlockers\resources

SMD helps you set up games to work with Steam using Lua files and related data. It writes the right files into your Steam folder so games and DLC can run. It does not replace or crack Steam itself.

**Use at your own risk.** This project is for educational use. You are responsible for how you use it.

**Need help?** Check the [documentation](docs/README.md) and the [Troubleshooting](docs/TROUBLESHOOTING.md) guide.

## Quick start

**If you have the EXE**  
Run SMD.exe and follow the prompts. You'll need GreenLuma installed; see the Setup Guide for the download link.

**If you use Python**  
1. Install dependencies: `pip install -r requirements.txt`  
2. Run: `python Main.py`  
3. Optional (Windows desktop notifications): `pip install -r requirements-optional.txt`

**GreenLuma**  
SMD works with GreenLuma. You need to download and set up GreenLuma yourself:  
https://www.mediafire.com/file/a7jfz14htim55wk/GL.zip/file  

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

## Command line

```bash
python Main.py --version
python Main.py --help
python Main.py --file game.lua
python Main.py --batch file1.lua file2.lua
python Main.py --quiet
python Main.py --dry-run
python Main.py --auto-update
python Main.py --export-ids output.txt
```

## Credits

**SMD** – Steam Manifest Downloader.  

**Midrags** – For this build and distribution.  

**CreamInstaller** – The DLC Unlockers feature in SMD is inspired by and compatible with CreamInstaller. SMD does not ship CreamInstaller; it provides its own implementation that follows similar behavior.

Use SMD at your own responsibility.
