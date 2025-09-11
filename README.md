# LibreOffice Dictionaries Collection

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Dictionary Count](https://img.shields.io/badge/Dictionaries-138-green.svg)](https://github.com/usuario/libreoffice-dictionaries-collection)

> Complete multilingual dictionary collection extracted from LibreOffice Portable 25.2.3

**En español**
[README_ES.md](README_ES.md)

## 📚 Description
This repository contains **138 dictionaries** from LibreOffice in 42 languages, including:
- **Spell checking** (`.aff` + `.dic` files)
- **Synonyms** (`.dat` + `.idx` files)
- **Hyphenation** (`hyph_*.dic` files)

Extracted from [LibreOffice Portable 25.2.3](https://portableapps.com/apps/office/libreoffice_portable) for use in:
- OpenOffice/LibreOffice
- Browsers (Firefox, Thunderbird)
- Text editors
- Open-source software projects

## 🌍 Available Languages

| Code  | Language               |
|-------|------------------------|
| af    | Afrikaans             |
| an    | Aragonese             |
| ar    | Arabic                |
| be    | Belarusian            |
| bg    | Bulgarian             |
| bn    | Bengali               |
| bo    | Tibetan               |
| br    | Breton                |
| bs    | Bosnian               |
| ca    | Catalan               |
| ckb   | Central Kurdish       |
| cs    | Czech                 |
| da    | Danish                |
| de    | German                |
| el    | Greek                 |
| en    | English               |
| eo    | Esperanto             |
| es    | Spanish               |
| et    | Estonian              |
| fa    | Persian               |
| fr    | French                |
| gd    | Scottish Gaelic       |
| gl    | Galician              |
| gu    | Gujarati              |
| he    | Hebrew                |
| hi    | Hindi                 |
| hr    | Croatian              |
| hu    | Hungarian             |
| id    | Indonesian            |
| is    | Icelandic             |
| it    | Italian               |
| ko    | Korean                |
| lo    | Lao                   |
| lt    | Lithuanian            |
| lv    | Latvian               |
| mn    | Mongolian             |
| ne    | Nepali                |
| nl    | Dutch                 |
| no    | Norwegian             |
| oc    | Occitan               |
| pl    | Polish                |
| pt-BR | Portuguese (Brazil)   |
| pt-PT | Portuguese (Portugal) |
| ro    | Romanian              |
| ru    | Russian               |
| si    | Sinhala               |
| sk    | Slovak                |
| sl    | Slovenian             |
| sq    | Albanian              |
| sr    | Serbian               |
| sv    | Swedish               |
| te    | Telugu                |
| th    | Thai                  |
| tr    | Turkish               |
| uk    | Ukrainian             |
| vi    | Vietnamese            |
| zu    | Zulu                  |

This table includes the 42 languages ​​available in the collection, maintaining the original LibreOffice codecs and their Spanish names for clarity. Codes with hyphens (such as pt-BR and pt-PT) represent regionally specific variants of the language.

The **path** to where they were located is this:

→ PortableApps → LibreOfficePortable → App → libreoffice → share → extensions


## 🚀 Usage in applications
### For OpenOffice/LibreOffice:
1. Download the required language folder
2. Copy the `.aff` and `.dic` files to:
   ```
   /usr/share/hunspell/  (Linux)
   C:\Program Files\LibreOffice\share\dict\  (Windows)
   ```
3. Restart the application

### For Firefox/Thunderbird:
1. Copy the `.aff` and `.dic` files to the user profile:
   ```
   [Profile]/dictionaries/
   ```
2. Restart the application

### For developers (Hunspell):
```python
import hunspell
hunspell_object = hunspell.Hunspell("es_ES.dic", "es_ES.aff")
```

## ⚖️ Licenses
Each dictionary has its own license. Check these files:
- `LICENSE*.txt`
- `COPYING*`
- `README_*.txt`

Most use:
- **GPL**, **LGPL**, **MPL** (Mozilla Public License)
- Open-source licenses (BSD, MIT, etc.)

## 🔧 File structure
```
dict-xx/
├── xx_YY.aff       # Affix rules
├── xx_YY.dic       # Main dictionary
├── hyph_xx_YY.dic  # Hyphenation patterns
├── th_xx_YY.dat    # Thesaurus data
├── th_xx_YY.idx    # Thesaurus index
├── description.xml # Metadata
├── dictionaries.xcu# Configuration
└── README_*.txt    # Language information
```

## 🤝 Contributions
Contributions are welcome! If you find:
- Missing dictionaries
- File errors
- License issues

Open an *issue* or submit a *pull request*.

## 📄 Credits
- **Original source**: [LibreOffice Portable](https://portableapps.com/)
- **Developers**: LibreOffice team and dictionary contributors
- **Licenses**: See specific files for each language

---

**Last updated**: Extracted from LibreOffice 25.2.3 (2025)

