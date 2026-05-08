#!/usr/bin/env python3
from pathlib import Path

LANGUAGES = {
    "dict-af": "Afrikaans",
    "dict-an": "Aragonese",
    "dict-ar": "Arabic",
    "dict-be": "Belarusian",
    "dict-bg": "Bulgarian",
    "dict-bn": "Bengali",
    "dict-bo": "Tibetan",
    "dict-br": "Breton",
    "dict-bs": "Bosnian",
    "dict-ca": "Catalan",
    "dict-ckb": "Central Kurdish",
    "dict-cs": "Czech",
    "dict-da": "Danish",
    "dict-de": "German",
    "dict-el": "Greek",
    "dict-en": "English",
    "dict-eo": "Esperanto",
    "dict-es": "Spanish",
    "dict-et": "Estonian",
    "dict-fa": "Persian",
    "dict-fr": "French",
    "dict-gd": "Scottish Gaelic",
    "dict-gl": "Galician",
    "dict-gu": "Gujarati",
    "dict-he": "Hebrew",
    "dict-hi": "Hindi",
    "dict-hr": "Croatian",
    "dict-hu": "Hungarian",
    "dict-id": "Indonesian",
    "dict-is": "Icelandic",
    "dict-it": "Italian",
    "dict-ko": "Korean",
    "dict-lo": "Lao",
    "dict-lt": "Lithuanian",
    "dict-lv": "Latvian",
    "dict-mn": "Mongolian",
    "dict-ne": "Nepali",
    "dict-nl": "Dutch",
    "dict-no": "Norwegian",
    "dict-oc": "Occitan",
    "dict-pl": "Polish",
    "dict-pt-BR": "Portuguese (Brazil)",
    "dict-pt-PT": "Portuguese (Portugal)",
    "dict-ro": "Romanian",
    "dict-ru": "Russian",
    "dict-si": "Sinhala",
    "dict-sk": "Slovak",
    "dict-sl": "Slovene",
    "dict-sq": "Albanian",
    "dict-sr": "Serbian",
    "dict-sv": "Swedish",
    "dict-te": "Telugu",
    "dict-th": "Thai",
    "dict-tr": "Turkish",
    "dict-uk": "Ukrainian",
    "dict-vi": "Vietnamese",
    "dict-zu": "Zulu",
}


def normalize_dict_name(name: str) -> str:
    """
    Convierte:
        dict-pt_BR -> dict-pt-BR
    para compararlo con la tabla.
    """
    return name.replace("_", "-")


def find_dictionary_pairs(folder: Path):
    """
    Busca pares .aff y .dic con el mismo nombre base.
    """
    aff_files = {p.stem: p.name for p in folder.glob("*.aff")}
    dic_files = {p.stem: p.name for p in folder.glob("*.dic")}

    pairs = []

    for stem in sorted(aff_files):
        if stem in dic_files:
            pairs.append((aff_files[stem], dic_files[stem]))

    return pairs


def main():
    base_dir = Path("dicts")

    if not base_dir.exists():
        print('ERROR: No existe la carpeta "dicts".')
        return

    output_lines = []

    dict_folders = sorted(
        p for p in base_dir.iterdir()
        if p.is_dir() and p.name.startswith("dict-")
    )

    for folder in dict_folders:

        normalized_name = normalize_dict_name(folder.name)

        language = LANGUAGES.get(
            normalized_name,
            "Unknown language"
        )

        pairs = find_dictionary_pairs(folder)

        if not pairs:
            continue

        output_lines.append(
            f"{folder.name}/            # {language}"
        )

        files = []

        for aff, dic in pairs:
            files.append(aff)
            files.append(dic)

        for index, filename in enumerate(files):

            connector = (
                "└──"
                if index == len(files) - 1
                else "├──"
            )

            output_lines.append(
                f"{connector} {filename}"
            )

        output_lines.append("")

    output_text = "\n".join(output_lines)

    # Mostrar en pantalla
    print(output_text)

    # Guardar archivo
    output_file = Path("dictionary_report.txt")

    output_file.write_text(
        output_text,
        encoding="utf-8"
    )

    print(f'\nArchivo creado: "{output_file}"')


if __name__ == "__main__":
    main()
