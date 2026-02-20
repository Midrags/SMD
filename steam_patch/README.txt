Steam patch (optional)
======================

SMD can patch Steam so it reads the game data SMD prepares, without replacing
Steam.exe. It uses two files that Steam loads from its own folder:

  xinput1_4.dll
  hid.dll

These two files are included in this folder (steam_patch). In SMD choose
"Patch / Unpatch Steam (DLL)" from the main menu and pick "Patch Steam".
After that, restart Steam.

Unpatching
----------

To remove the patch, open SMD, choose "Patch / Unpatch Steam (DLL)" and pick
"Unpatch Steam". Then restart Steam. Your Steam folder will be back to normal.
