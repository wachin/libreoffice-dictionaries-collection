# Convertir diccionarios a UTF-8

Este documento explica cómo convertir los diccionarios que usan encodings
ISO-8859 a UTF-8 usando `iconv` en Linux/Debian.

## Por qué convertir

11 diccionarios usan encodings ISO-8859 en lugar de UTF-8. Sin conversión,
los diccionarios compilados con MSVC (sin libiconv) fallan con estos idiomas.

## Encodings originales

| Carpeta | Idioma | Encoding original |
|---------|--------|-------------------|
| dict-an | Aragonese | ISO-8859-1 |
| dict-bs | Bosnian | ISO-8859-2 |
| dict-de | German | ISO-8859-1 |
| dict-el | Greek | ISO-8859-7 |
| dict-et | Estonian | ISO-8859-15 |
| dict-id | Indonesian | ISO-8859-1 |
| dict-lt | Lithuanian | ISO-8859-13 |
| dict-no | Norwegian | ISO-8859-1 |
| dict-pl | Polish | ISO-8859-2 |
| dict-sl | Slovene | ISO-8859-2 |
| dict-ar | Arabic | WINDOWS-1256 |
| dict-pt-BR | Portuguese (Brazil) | *(no declarado)* |

## Requisitos

- Linux/Debian/Ubuntu
- `iconv` (viene preinstalado con `libc-bin`)

## Pasos

### 1. Navegar al directorio del submódulo

```bash
cd /ruta/a/libreoffice-dictionaries-collection
```

### 2. Ejecutar la conversión

Copia y pega este script en tu terminal:

```bash
#!/bin/bash
# Convert non-UTF8 dictionaries to UTF-8
set -e

DICTS="dicts"

# Function: convert files and update SET line
convert_dict() {
    local dir="$1"
    local enc="$2"
    local code="$3"

    if [ ! -d "$DICTS/$dir" ]; then
        echo "SKIP: $dir not found"
        return
    fi

    echo "Converting $dir ($enc -> UTF-8)..."

    for ext in aff dic; do
        for f in "$DICTS/$dir"/*."$ext"; do
            [ -f "$f" ] || continue
            iconv -f "$enc" -t UTF-8 "$f" > "$f.tmp" && mv "$f.tmp" "$f"
            echo "  Converted $(basename "$f")"
        done
    done

    # Update SET line in .aff files
    for aff in "$DICTS/$dir"/*.aff; do
        [ -f "$aff" ] || continue
        sed -i 's/^SET .*/SET UTF-8/' "$aff"
        echo "  Updated SET line in $(basename "$aff")"
    done
}

# Run conversions
convert_dict "dict-an"     "ISO-8859-1"   "an"
convert_dict "dict-bs"     "ISO-8859-2"   "bs"
convert_dict "dict-de"     "ISO-8859-1"   "de"
convert_dict "dict-el"     "ISO-8859-7"   "el"
convert_dict "dict-et"     "ISO-8859-15"  "et"
convert_dict "dict-id"     "ISO-8859-1"   "id"
convert_dict "dict-lt"     "ISO-8859-13"  "lt"
convert_dict "dict-no"     "ISO-8859-1"   "no"
convert_dict "dict-pl"     "ISO-8859-2"   "pl"
convert_dict "dict-sl"     "ISO-8859-2"   "sl"
convert_dict "dict-ar"     "WINDOWS-1256" "ar"
convert_dict "dict-pt-BR"  "ISO-8859-1"   "pt-BR"

echo ""
echo "Conversion complete!"
```

### 3. Verificar

Después de convertir, verifica que los archivos dicen UTF-8:

```bash
# Verificar la línea SET en un .aff convertido
grep "^SET " dicts/dict-de/de.aff
# Debe mostrar: SET UTF-8

# Verificar encoding con file
file dicts/dict-de/de.dic
# Debe mostrar algo como: UTF-8 Unicode text
```

### 4. Hacer commit

```bash
git add dicts/
git commit -m "Convert all dictionaries to UTF-8 encoding"
```

## Notas

- `iconv` con `//TRANSLIT` no es necesario aquí — los diccionarios de LibreOffice
  no tienen bytes inválidos.
- Si algún archivo falla, puedes usar `iconv -f ISO-8859-1 -t UTF-8//IGNORE`
  para ignorar bytes problemáticos.
- El script actualiza automáticamente la línea `SET UTF-8` en cada `.aff`.
