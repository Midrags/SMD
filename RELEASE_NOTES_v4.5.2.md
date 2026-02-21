# SMD v4.5.2

**Version:** 4.5.2  
**Release date:** February 2025

This release improves the **Check for updates** flow, makes **DLC check** reliable even when Steam is slow or times out, and includes a few smaller fixes.

---

## Update check (Check for updates)

- **Check for updates** now works for everyone: it always checks GitHub for the latest release and shows your version vs latest.
- If you're up to date: *"You're already on the latest version."*
- If a newer version exists: you can open the release page in your browser to download (or, for the Windows EXE with a matching update package, update from inside the app).
- The updater uses proper GitHub API headers and a fallback when the "latest" endpoint is unavailable.

## DLC check reliability

- **DLC check** no longer gets stuck when Steam is slow or times out.
- Steam API requests (app info, DLC details) now retry up to **3 times** with a short delay instead of looping forever. If it still fails, you get a clear message instead of hanging.
- If Steam fails after retries, SMD automatically falls back to the **Steam Store** (no login): it fetches the DLC list and names from the store website and still shows which DLCs are in your AppList/config and lets you add missing ones.
- So the DLC check works even when the Steam client connection is flaky.

## Other fixes

- **credentials.json** is now in `.gitignore` so it never gets committed or included in release zips.
- **UPLOAD_AND_PRIVACY.md** updated with release-zip instructions and what to exclude.

---

See [CHANGELOG.md](CHANGELOG.md) for the full history.
