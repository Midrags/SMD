# Changelog

## v4.5.2 (latest)

### Update check (Check for updates)

- **Check for updates** now works for everyone: it always checks GitHub for the latest release and shows your version vs latest.
- If you're up to date: *"You're already on the latest version."*
- If a newer version exists: you can open the release page in your browser to download (or, for the Windows EXE with a matching update package, update from inside the app).
- The updater uses proper GitHub API headers and a fallback when the "latest" endpoint is unavailable.

### DLC check reliability

- **DLC check** no longer gets stuck when Steam is slow or times out.
- Steam API requests (app info, DLC details) now retry up to 3 times with a short delay instead of looping forever.
- If Steam still fails after retries, SMD automatically falls back to the **Steam Store** (no login): it fetches the DLC list and names from the store website and still shows which DLCs are in your AppList/config and lets you add missing ones.
- So the DLC check works even when the Steam client connection is flaky.

### Other fixes

- **credentials.json** is now in `.gitignore` so it never gets committed or included in release zips.
- **UPLOAD_AND_PRIVACY.md** updated with release-zip instructions and what to exclude.

---

## v4.5.1

### Fix for crash on startup (`_listeners` error)

**What was the problem?**

Some people got a crash when starting SMD. The error said something like:  
`'SteamClient' object has no attribute '_listeners'. Did you mean: 'listeners'?`

That happened because the wrong Python package named "eventemitter" was installed. SMD needs a specific one called **gevent-eventemitter**. There is another package with a similar name that does not work with SMD and caused the crash.

**What we changed**

- We now tell the installer to use the correct **gevent-eventemitter** package so new installs should not hit this crash.
- If you already had the crash, do this once:
  1. Open a command line in the SMD folder.
  2. Run: `pip uninstall eventemitter`
  3. Run: `pip install "steam[client]"`
  4. Run: `pip install -r requirements.txt`
  5. Start SMD again.

After that, SMD should start normally.
