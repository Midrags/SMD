# SMD v4.5.3

**Version:** 4.5.3  
**Release date:** February 2025

This release fixes the **Multiplayer fix (online-fix.me)** flow so it finds the correct game and no longer shows "Game: Unknown" or picks the wrong fix page.

---

## Multiplayer fix (online-fix.me) – correct game and better matching

- **"Game: Unknown" fixed:** The game name is now read from the ACF in the **same Steam library** where the game is installed (e.g. if the game is on `D:\SteamLibrary\...`, we read that library’s manifest, not the first one). If the name is still missing, we fetch the official name from the **Steam Store API** so we never search with "Unknown".

- **Wrong game match fixed:** Search now uses a stricter minimum match (50%) and prefers results whose link text contains the game name (e.g. "R.E.P.O. по сети" for R.E.P.O.). We also search with "game name online-fix" to narrow results. This avoids picking the wrong game (e.g. "Species Unknown" when you selected R.E.P.O.).

---

See [CHANGELOG.md](CHANGELOG.md) for the full history.
