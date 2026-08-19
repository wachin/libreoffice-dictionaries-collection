# LibreOffice Dictionaries Collection

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Dictionary Count](https://img.shields.io/badge/Dictionaries-57-green.svg)](https://github.com/wachin/libreoffice-dictionaries-collection)

> Complete multilingual dictionary collection extracted from LibreOffice Portable 25.2.3
>
> **All dictionaries converted to UTF-8** for universal compatibility.

**En español**
[README_ES.md](README_ES.md)

##  Description

This repository contains **57 dictionaries** from LibreOffice in 42 languages, including:

- **Spell checking** (`.aff` + `.dic` files)
- **Synonyms** (`.dat` + `.idx` files)
- **Hyphenation** (`hyph_*.dic` files)

Extracted from [LibreOffice Portable 25.2.3](https://portableapps.com/apps/office/libreoffice_portable) for use in:

- OpenOffice/LibreOffice
- Browsers (Firefox, Thunderbird)
- Text editors
- Open-source software projects

## 🌍 Available Languages

The **path** to where they were located:

> 📂 PortableApps → LibreOfficePortable → App → libreoffice → share → extensions

### Language Code & Language

| **Folder** | **Language** |
| ---------- | ------------ |
| dict-af | Afrikaans |
| dict-an | Aragonese |
| dict-ar | Arabic |
| dict-be | Belarusian |
| dict-bg | Bulgarian |
| dict-bn | Bengali |
| dict-bo | Tibetan |
| dict-br | Breton |
| dict-bs | Bosnian |
| dict-ca | Catalan |
| dict-ckb | Central Kurdish |
| dict-cs | Czech |
| dict-da | Danish |
| dict-de | German |
| dict-el | Greek |
| dict-en | English |
| dict-eo | Esperanto |
| dict-es | Spanish |
| dict-et | Estonian |
| dict-fa | Persian |
| dict-fr | French |
| dict-gd | Scottish Gaelic |
| dict-gl | Galician |
| dict-gu | Gujarati |
| dict-he | Hebrew |
| dict-hi | Hindi |
| dict-hr | Croatian |
| dict-hu | Hungarian |
| dict-id | Indonesian |
| dict-is | Icelandic |
| dict-it | Italian |
| dict-ko | Korean |
| dict-lo | Lao |
| dict-lt | Lithuanian |
| dict-lv | Latvian |
| dict-mn | Mongolian |
| dict-ne | Nepali |
| dict-nl | Dutch |
| dict-no | Norwegian |
| dict-oc | Occitan |
| dict-pl | Polish |
| dict-pt-BR | Portuguese (Brazil) |
| dict-pt-PT | Portuguese (Portugal) |
| dict-ro | Romanian |
| dict-ru | Russian |
| dict-si | Sinhala |
| dict-sk | Slovak |
| dict-sl | Slovene |
| dict-sq | Albanian |
| dict-sr | Serbian |
| dict-sv | Swedish |
| dict-te | Telugu |
| dict-th | Thai |
| dict-tr | Turkish |
| dict-uk | Ukrainian |
| dict-vi | Vietnamese |
| dict-zu | Zulu |

You can check the language names [here](https://wiki.documentfoundation.org/Development/Dictionaries)

---

## 🔤 Character Encoding

### Original encodings (as extracted from LibreOffice Portable)

When extracted from LibreOffice Portable 25.2.3, each dictionary used the
character encoding declared in its `.aff` file (`SET <encoding>` line).
The original encodings were:

| **Folder** | **Language** | **Original Encoding** |
| ---------- | ------------ | --------------------- |
| dict-af | Afrikaans | UTF-8 |
| dict-an | Aragonese | ISO-8859-1 |
| dict-ar | Arabic | *(not declared)* |
| dict-be | Belarusian | UTF-8 |
| dict-bg | Bulgarian | UTF-8 |
| dict-bn | Bengali | UTF-8 |
| dict-bo | Tibetan | UTF-8 |
| dict-br | Breton | UTF-8 |
| dict-bs | Bosnian | ISO-8859-2 |
| dict-ca | Catalan | UTF-8 |
| dict-ckb | Central Kurdish | UTF-8 |
| dict-cs | Czech | UTF-8 |
| dict-da | Danish | UTF-8 |
| dict-de | German | ISO-8859-1 |
| dict-el | Greek | ISO-8859-7 |
| dict-en | English | UTF-8 |
| dict-eo | Esperanto | UTF-8 |
| dict-es | Spanish | UTF-8 |
| dict-et | Estonian | ISO-8859-15 |
| dict-fa | Persian | UTF-8 |
| dict-fr | French | UTF-8 |
| dict-gd | Scottish Gaelic | UTF-8 |
| dict-gl | Galician | UTF-8 |
| dict-gu | Gujarati | UTF-8 |
| dict-he | Hebrew | UTF-8 |
| dict-hi | Hindi | UTF-8 |
| dict-hr | Croatian | UTF-8 |
| dict-hu | Hungarian | UTF-8 |
| dict-id | Indonesian | ISO-8859-1 |
| dict-is | Icelandic | UTF-8 |
| dict-it | Italian | UTF-8 |
| dict-ko | Korean | UTF-8 |
| dict-lo | Lao | UTF-8 |
| dict-lt | Lithuanian | ISO-8859-13 |
| dict-lv | Latvian | UTF-8 |
| dict-mn | Mongolian | UTF-8 |
| dict-ne | Nepali | UTF-8 |
| dict-nl | Dutch | UTF-8 |
| dict-no | Norwegian | ISO-8859-1 |
| dict-oc | Occitan | UTF-8 |
| dict-pl | Polish | ISO-8859-2 |
| dict-pt-BR | Portuguese (Brazil) | *(not declared)* |
| dict-pt-PT | Portuguese (Portugal) | UTF-8 |
| dict-ro | Romanian | UTF-8 |
| dict-ru | Russian | UTF-8 |
| dict-si | Sinhala | UTF-8 |
| dict-sk | Slovak | UTF-8 |
| dict-sl | Slovene | ISO-8859-2 |
| dict-sq | Albanian | UTF-8 |
| dict-sr | Serbian | UTF-8 |
| dict-sv | Swedish | UTF-8 |
| dict-te | Telugu | UTF-8 |
| dict-th | Thai | UTF-8 |
| dict-tr | Turkish | UTF-8 |
| dict-uk | Ukrainian | UTF-8 |
| dict-vi | Vietnamese | UTF-8 |
| dict-zu | Zulu | UTF-8 |

**11 dictionaries** used non-UTF8 encodings (ISO-8859-1, ISO-8859-2,
ISO-8859-7, ISO-8859-13, ISO-8859-15), and 2 had no encoding declared.


---

## 🚀 Usage in Applications

### For OpenOffice/LibreOffice:

1. Download the required language folder
2. Copy the `.aff` and `.dic` files to:

```
/usr/share/hunspell/  (Linux)
C:\Program Files\LibreOffice\share\extensions\dict\  (Windows)
```

3. Restart the application

### For Firefox/Thunderbird:

1. Copy the `.aff` and `.dic` files to the user profile:

```
[Profile]/dictionaries/
```

2. Restart the application

### For Developers (Hunspell):

```python
import hunspell
h = hunspell.Hunspell("es_ES.aff", "es_ES.dic")
h.spell("hola")  # True
```

---

## ⚖️ Licenses

Each dictionary has its own license. Check these files:

- `LICENSE*.txt`
- `COPYING*`
- `README_*.txt`

Most use:

- **GPL**, **LGPL**, **MPL** (Mozilla Public License)
- Open-source licenses (BSD, MIT, etc.)

---

## 🔧 File Structure

```
dict-xx/
├── xx_YY.aff       # Affix rules
├── xx_YY.dic       # Main dictionary
── hyph_xx_YY.dic  # Hyphenation patterns
├── th_xx_YY.dat    # Thesaurus data
├── th_xx_YY.idx    # Thesaurus index
├── description.xml # Metadata
├── dictionaries.xcu# Configuration
└── README_*.txt    # Language information
```

---

## 🔗 Use as Git Submodule

This repository can be used as a **Git submodule** in other projects that
require dictionary functionality.

### Adding as Submodule

```bash
git submodule add https://github.com/wachin/libreoffice-dictionaries-collection.git libs/dictionaries
git commit -m "Add dictionaries submodule"
```

### Updating the Submodule

```bash
git submodule update --remote --merge
```

### Packaging Tools

This repository includes helper scripts:

- **`tools/package-dicts.sh`** — Compresses each `dict-XX/` folder into
  `.tar.gz` archives for releases.
- **`tools/fetch-dict-list.py`** — Generates `dictionaries.json` from a
  GitHub Release.
- **`tools/convert-to-utf8.bat`** — Converts all non-UTF8 dictionaries to
  UTF-8 using `iconv.exe` from MSYS2.

---

## 🤝 Contributions

Contributions are welcome! If you find:

- Missing dictionaries
- File errors
- License issues

Open an *issue* or submit a *pull request*.

---

##  Credits

- **Original source**: [LibreOffice Portable](https://portableapps.com/)
- **Developers**: LibreOffice team and dictionary contributors
- **Licenses**: See specific files for each language

---

**Last updated**: Extracted from LibreOffice 25.2.3 (2025) · All dictionaries converted to UTF-8
