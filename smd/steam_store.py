"""
Fetch game names from Steam store pages (HTTP). Used when local ACF is missing
(e.g. remove-game list for uninstalled games).
"""

import re
import logging
from typing import Optional

import httpx

logger = logging.getLogger(__name__)

# Store page title: "Game Name on Steam" or "Save 60% on Game Name on Steam"
_STEAM_TITLE_RE = re.compile(
    r"<title>\s*(.+)\s+(?:on|en)\s+Steam\s*</title>",
    re.IGNORECASE | re.DOTALL,
)
_STORE_TIMEOUT = 8.0
_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


def get_app_name_from_store(app_id: int) -> Optional[str]:
    """
    Fetch app name from Steam store page (no Steam client login).
    Returns None on failure or if title cannot be parsed.
    """
    url = f"https://store.steampowered.com/app/{app_id}/"
    try:
        resp = httpx.get(
            url,
            timeout=_STORE_TIMEOUT,
            headers={"User-Agent": _USER_AGENT},
            follow_redirects=True,
        )
        if resp.status_code != 200:
            return None
        html = resp.text
    except (httpx.TimeoutException, httpx.RequestError) as e:
        logger.debug("Store fetch failed for %s: %s", app_id, e)
        return None

    m = _STEAM_TITLE_RE.search(html)
    if not m:
        return None
    name = m.group(1).strip()
    # Trim " en " suffix if present (e.g. Spanish page)
    if " en " in name:
        name = name.split(" en ")[-1].strip()
    # Optional: strip "Save N% on " prefix for cleaner display
    if name.lower().startswith("save ") and " on " in name:
        parts = name.split(" on ", 1)
        if len(parts) == 2 and parts[0].strip().endswith("%"):
            name = parts[1].strip()
    return name if name else None
