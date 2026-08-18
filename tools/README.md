# Tools

Utility scripts for packaging and distributing Hunspell & Mythes dictionaries.

## package-dicts.sh

Compress each dictionary folder from the `third-party/` submodule into
individual `.tar.gz` archives and place them in the `build/` directory.

### Usage

From the repository root:

```bash
bash tools/package-dicts.sh
```

### Output

All archives are written to `build/`:

```
build/dict-en.tar.gz
build/dict-es.tar.gz
build/dict-de.tar.gz
...
```

Each archive contains a single `dict-XX/` folder with the Hunspell (`.aff`,
`.dic`) and Mythes (`.dat`, `.idx`) files for that language.

---

## fetch-dict-list.py

Fetch the list of dictionary assets from a GitHub Release and generate a
`dictionaries.json` file that can be consumed by ChordFlow, ChordPages, or
any other application.

### Usage

From the repository root:

```bash
python3 tools/fetch-dict-list.py --tag v1.0-dictionaries-thesaurus
```

### Output

`dictionaries.json` is written to the current directory with the following
structure:

```json
{
  "source": "wachin/libreoffice-dictionaries-collection/releases/tag/v1.0-dictionaries-thesaurus",
  "dictionaries": [
    {
      "code": "en",
      "name": "English",
      "url": "https://github.com/.../dict-en.tar.gz",
      "size": 6841341
    },
    ...
  ]
}
```

### Options

- `--tag TAG` — Fetch a specific release tag (default: latest release).

---

## Release workflow

To publish a new dictionary release:

1. Make sure the `third-party/` submodule is up to date:
   ```bash
   git submodule update --init --recursive
   ```

2. Package the dictionaries:
   ```bash
   bash tools/package-dicts.sh
   ```

3. Upload all `build/dict-*.tar.gz` files to a new GitHub Release on the
   [libreoffice-dictionaries-collection](https://github.com/wachin/libreoffice-dictionaries-collection)
   repository.

4. After publishing the release, generate the dictionary list:
   ```bash
   python3 tools/fetch-dict-list.py --tag <TAG_NAME>
   ```

5. Commit the resulting `dictionaries.json` to the
   [guitarchordstudio](https://github.com/wachin/guitarchordstudio) repository
   so the applications can use it.