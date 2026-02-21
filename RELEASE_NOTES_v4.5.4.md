# SMD v4.5.4

**Version:** 4.5.4  
**Release date:** February 2025

This release makes **Check for updates** fully automatic: download, extract, and replace files in place. When running from the EXE, you are prompted to rebuild the EXE after the update.

---

## Check for updates – automatic install

- **Automatic update:** When a newer version is available, you can choose "Download and update automatically?". SMD downloads the release zip, extracts it, and replaces the files in your install folder.
- **Running from Python:** The app restarts with the new version after the update.
- **Running from the EXE:** SMD does not relaunch the EXE after updating. It shows: *"Update complete. Rebuild the EXE to use the new version."* so you can rebuild the executable with the updated code.
- Updates use the same folder as your current install—no manual copying or extracting needed.

---

See [CHANGELOG.md](CHANGELOG.md) for the full history.
