# Changelog

## v4.5.1 (latest)

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
