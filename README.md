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

## 🔗 Use as Git Submodule

This repository can be used as a **Git submodule** in other projects that require dictionary functionality. This is especially useful for:

- Text editors
- Word processors
- Language learning applications
- Any software needing multilingual text processing

### 🐍 Integration Example: Python/PyQt6 Application

#### 1. Add as Submodule
In your project root:

```bash
git submodule add https://github.com/wachin/libreoffice-dictionaries-collection.git libs/dictionaries
git commit -m "Add dictionaries submodule"
```

#### 2. Install Dependencies (Ubuntu/Debian)

```bash
sudo apt-get install python3-pyqt6 python3-enchant python3-hunspell python3-pyphen libmythes-1.2-0 libmythes-dev
pip install git+https://github.com/corerd/pythes
```

#### 3. Project Structure

```
your-project/
├── .gitmodules
├── main.py
├── requirements.txt
└── libs/
    └── dictionaries/  # Submodule
        ├── dicts/
        │   ├── dict-es/
        │   ├── dict-en/
        │   └── ...
        └── README.md
```

#### 4. Code Implementation

```python
import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton

# Dictionary libraries
import enchant
import hunspell
import pyphen
from pythes import Thesaurus

class DictionaryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dict_path = os.path.join(os.path.dirname(__file__), 
                                     "libs", "dictionaries", "dicts")
        self.init_ui()
        self.init_dictionaries()
    
    def init_ui(self):
        self.setWindowTitle("Dictionary Processor")
        self.setGeometry(100, 100, 800, 600)
        
        # Layout
        layout = QVBoxLayout()
        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)
        
        # Buttons
        btn_spell = QPushButton("Check Spelling")
        btn_spell.clicked.connect(self.check_spelling)
        layout.addWidget(btn_spell)
        
        btn_hyphen = QPushButton("Hyphenate")
        btn_hyphen.clicked.connect(self.hyphenate_text)
        layout.addWidget(btn_hyphen)
        
        btn_synonyms = QPushButton("Get Synonyms")
        btn_synonyms.clicked.connect(self.get_synonyms)
        layout.addWidget(btn_synonyms)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def init_dictionaries(self):
        # Initialize Spanish dictionaries
        lang = "es"
        lang_path = os.path.join(self.dict_path, f"dict-{lang}")
        
        # Spell checking (Hunspell)
        self.hunspell = hunspell.HunSpell(
            os.path.join(lang_path, f"{lang}_ES.aff"),
            os.path.join(lang_path, f"{lang}_ES.dic")
        )
        
        # Hyphenation (Pyphen)
        self.pyphen = pyphen.Pyphen(lang=f"{lang}_ES")
        
        # Thesaurus (MyThes)
        self.thesaurus = Thesaurus(
            os.path.join(lang_path, f"th_{lang}_ES_v2.dat"),
            os.path.join(lang_path, f"th_{lang}_ES_v2.idx")
        )
    
    def check_spelling(self):
        text = self.text_edit.toPlainText()
        words = text.split()
        
        print("\n=== SPELL CHECK RESULTS ===")
        for word in words:
            word = word.strip(".,!?;:")
            if word:
                if self.hunspell.spell(word):
                    print(f"✓ {word}")
                else:
                    suggestions = self.hunspell.suggest(word)
                    print(f"✗ {word} -> {suggestions[:3]}")  # Show top 3 suggestions
    
    def hyphenate_text(self):
        text = self.text_edit.toPlainText()
        words = text.split()
        
        print("\n=== HYPHENATION RESULTS ===")
        for word in words:
            word = word.strip(".,!?;:")
            if word:
                hyphenated = self.pyphen.inserted(word)
                print(f"{word} -> {hyphenated}")
    
    def get_synonyms(self):
        word = self.text_edit.toPlainText().strip()
        if not word:
            return
            
        print(f"\n=== SYNONYMS FOR '{word}' ===")
        meanings = self.thesaurus.lookup(word)
        if meanings:
            for i, meaning in enumerate(meanings[:3], 1):  # Show top 3 meanings
                print(f"{i}. {meaning.description}:")
                print(f"   {', '.join(meaning.synonyms[:5])}")  # Show top 5 synonyms
        else:
            print("No synonyms found")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DictionaryApp()
    window.show()
    sys.exit(app.exec())
```

### 📚 Dictionary Usage Examples

#### Spell Checking (Hunspell)
```python
import hunspell

# Initialize dictionary
h = hunspell.HunSpell("libs/dictionaries/dicts/dict-es/es_ES.aff", 
                     "libs/dictionaries/dicts/dict-es/es_ES.dic")

# Check word
word = "computadora"
if h.spell(word):
    print(f"'{word}' is correct")
else:
    suggestions = h.suggest(word)
    print(f"Suggestions: {suggestions}")
```

#### Hyphenation (Pyphen)
```python
import pyphen

# Initialize dictionary
dic = pyphen.Pyphen(lang='es_ES')

# Hyphenate word
word = "extraordinario"
hyphenated = dic.inserted(word)  # "ex-tra-or-di-na-rio"
print(f"Hyphenation: {hyphenated}")
```

#### Thesaurus (MyThes via pythes)
```python
from pythes import Thesaurus

# Initialize thesaurus
thes = Thesaurus("libs/dictionaries/dicts/dict-es/th_es_ES_v2.dat",
                 "libs/dictionaries/dicts/dict-es/th_es_ES_v2.idx")

# Get synonyms
word = "rápido"
meanings = thes.lookup(word)
for meaning in meanings:
    print(f"{meaning.description}: {meaning.synonyms}")
```

### 🔄 Update Submodule
To update dictionaries to the latest version:
```bash
git submodule update --remote --merge
```

### 💡 Benefits of Using as Submodule
1. **Centralized Management**: Single source for all dictionaries
2. **Version Control**: Pin specific dictionary versions
3. **Space Efficiency**: Dictionaries stored once, referenced by multiple projects
4. **Easy Updates**: Update all dictionaries with one command
5. **Collaboration**: Contribute improvements upstream

### 🛠️ Supported Libraries
| Functionality  |    Library    |   Files Used    |
| -------------- | ------------- | --------------- |
| Spell Checking | hunspell      | `.aff` + `.dic` |
| Hyphenation    | pyphen        | `.dic` patterns |
| Thesaurus      | pythes/MyThes | `.dat` + `.idx` |
| Alternative    | enchant       | `.aff` + `.dic` |


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

