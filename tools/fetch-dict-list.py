#!/usr/bin/env python3
"""fetch-dict-list.py — Generate a JSON list of dictionary download URLs.

This script fetches the release assets from the
``libreoffice-dictionaries-collection`` GitHub repository and generates a
``dictionaries.json`` file that can be consumed by ChordFlow and ChordPages
to let users download dictionaries on demand.

Usage:
  python3 tools/fetch-dict-list.py [--tag TAG]

  By default it fetches the latest release.  Pass ``--tag v1.0-dictionaries``
  to fetch a specific release.

Output:
  dictionaries.json  — a JSON array of objects, one per dictionary.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request

REPO = "wachin/libreoffice-dictionaries-collection"
API_URL = f"https://api.github.com/repos/{REPO}/releases"


def fetch_release(tag: str | None = None) -> dict:
    """Fetch release data from GitHub API."""
    url = f"{API_URL}/tags/{tag}" if tag else f"{API_URL}/latest"
    print(f"Fetching: {url}", file=sys.stderr)
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def build_dict_list(release: dict) -> list[dict]:
    """Build a sorted list of dictionaries from release assets.

    Each entry has the shape::

        {
            "code": "en_US",
            "name": "English (US)",
            "url": "https://github.com/.../dict-en.tar.gz",
            "size": 6930000
        }
    """
    lang_labels = {
        "af": "Afrikaans",
        "an": "Aragonese",
        "ar": "Arabic",
        "be": "Belarusian",
        "bg": "Bulgarian",
        "bn": "Bengali",
        "bo": "Classical Tibetan",
        "br": "Breton",
        "bs": "Bosnian",
        "ca": "Catalan",
        "ckb": "Central Kurdish",
        "cs": "Czech",
        "da": "Danish",
        "de": "German",
        "el": "Modern Greek",
        "en": "English",
        "eo": "Esperanto",
        "es": "Spanish",
        "et": "Estonian",
        "fa": "Persian",
        "fr": "French",
        "gd": "Scottish Gaelic",
        "gl": "Galician",
        "gu": "Gujarati",
        "he": "Hebrew",
        "hi": "Hindi",
        "hr": "Croatian",
        "hu": "Hungarian",
        "id": "Indonesian",
        "is": "Icelandic",
        "it": "Italian",
        "ko": "Korean",
        "lo": "Lao",
        "lt": "Lithuanian",
        "lv": "Latvian",
        "mn": "Mongolian",
        "ne": "Nepali",
        "nl": "Dutch",
        "no": "Norwegian",
        "oc": "Occitan",
        "pl": "Polish",
        "pt-BR": "Portuguese (Brazil)",
        "pt-PT": "Portuguese (Portugal)",
        "ro": "Romanian",
        "ru": "Russian",
        "si": "Sinhalese",
        "sk": "Slovak",
        "sl": "Slovenian",
        "sq": "Albanian",
        "sr": "Serbian",
        "sv": "Swedish",
        "te": "Telugu",
        "th": "Thai",
        "tr": "Turkish",
        "uk": "Ukrainian",
        "vi": "Vietnamese",
        "zu": "Zulu",
    }

    # Match asset names like "dict-en.tar.gz" → code "en"
    pattern = re.compile(r"^dict-([a-zA-Z-]+)\.tar\.gz$")
    entries: list[dict] = []

    for asset in release.get("assets", []):
        name = asset["name"]
        m = pattern.match(name)
        if not m:
            continue
        code = m.group(1)
        # Map dict-pt-BR → code "pt_BR" for the spell checker
        lang_code = code.replace("-", "_")
        label = lang_labels.get(code, code.replace("-", " ").title())
        entries.append(
            {
                "code": lang_code,
                "name": label,
                "url": asset["browser_download_url"],
                "size": asset["size"],
            }
        )

    entries.sort(key=lambda e: e["code"])
    return entries


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate dictionaries.json from GitHub release assets"
    )
    parser.add_argument(
        "--tag",
        help="Release tag (default: latest)",
    )
    args = parser.parse_args()

    release = fetch_release(args.tag)
    entries = build_dict_list(release)

    output = {"source": f"{REPO}/releases/tag/{args.tag or release['tag_name']}", "dictionaries": entries}
    with open("dictionaries.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Written {len(entries)} dictionaries to dictionaries.json", file=sys.stderr)


if __name__ == "__main__":
    main()