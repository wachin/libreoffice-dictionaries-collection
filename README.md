# LibreOffice Dictionaries Collection

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Dictionary Count](https://img.shields.io/badge/Dictionaries-138-green.svg)](https://github.com/usuario/libreoffice-dictionaries-collection)

> Colección completa de diccionarios multilingües extraídos de LibreOffice Portable 25.2.3

## 📚 Descripción
Este repositorio contiene **138 diccionarios** de LibreOffice en 42 idiomas, incluyendo:
- **Corrección ortográfica** (archivos `.aff` + `.dic`)
- **Sinónimos** (archivos `.dat` + `.idx`)
- **División silábica** (archivos `hyph_*.dic`)

Extraídos de la versión [LibreOffice Portable 25.2.3](https://portableapps.com/apps/office/libreoffice_portable) para uso en:
- OpenOffice/LibreOffice
- Navegadores (Firefox, Thunderbird)
- Editores de texto
- Proyectos de software libre

## 🌍 Idiomas disponibles

| **Código** |      **Idioma**      |
| ---------- | -------------------- |
| af         | Afrikaans            |
| an         | Aragonés             |
| ar         | Árabe                |
| be         | Bielorruso           |
| bg         | Búlgaro              |
| bn         | Bengalí              |
| bo         | Tibetano             |
| br         | Bretón               |
| bs         | Bosnio               |
| ca         | Catalán              |
| ckb        | Kurdo central        |
| cs         | Checo                |
| da         | Danés                |
| de         | Alemán               |
| el         | Griego               |
| en         | Inglés               |
| eo         | Esperanto            |
| es         | Español              |
| et         | Estonio              |
| fa         | Persa                |
| fr         | Francés              |
| gd         | Gaélico escocés      |
| gl         | Gallego              |
| gu         | Guyaratí             |
| he         | Hebreo               |
| hi         | Hindi                |
| hr         | Croata               |
| hu         | Húngaro              |
| id         | Indonesio            |
| is         | Islandés             |
| it         | Italiano             |
| ko         | Coreano              |
| lo         | Lao                  |
| lt         | Lituano              |
| lv         | Letón                |
| mn         | Mongol               |
| ne         | Nepalí               |
| nl         | Neerlandés           |
| no         | Noruego              |
| oc         | Occitano             |
| pl         | Polaco               |
| pt-BR      | Portugués (Brasil)   |
| pt-PT      | Portugués (Portugal) |
| ro         | Rumano               |
| ru         | Ruso                 |
| si         | Cingalés             |
| sk         | Eslovaco             |
| sl         | Esloveno             |
| sq         | Albanés              |
| sr         | Serbio               |
| sv         | Sueco                |
| te         | Telugu               |
| th         | Tailandés            |
| tr         | Turco                |
| uk         | Ucraniano            |
| vi         | Vietnamita           |
| zu         | Zulú                 |

Esta tabla incluye los 42 idiomas disponibles en la colección, manteniendo los códigos originales de LibreOffice y sus nombres en español para mayor claridad. Los códigos con guion (como pt-BR y pt-PT) representan variantes regionales específicas del idioma.

La **ruta** donde estaban es esta:

 → PortableApps → LibreOfficePortable → App → libreoffice → share → extensions


## 🚀 Uso en aplicaciones

### Para Firefox/Thunderbird:
1. Copia los archivos `.aff` y `.dic` en el perfil de usuario:
```
[Perfil]/dictionaries/
```
2. Reinicia la aplicación

### Para desarrolladores (Hunspell):
```python
import hunspell
hunspell_object = hunspell.Hunspell("es_ES.dic", "es_ES.aff")
```

## ⚖️ Licencias
Cada diccionario tiene su propia licencia. Verifica los archivos:
- `LICENSE*.txt`
- `COPYING*`
- `README_*.txt`

La mayoría usan:
- **GPL**, **LGPL**, **MPL** (Mozilla Public License)
- Licencias de código abierto (BSD, MIT, etc.)

## 🔧 Estructura de archivos
```
dict-xx/
├── xx_YY.aff       # Reglas de afijos
├── xx_YY.dic       # Diccionario principal
├── hyph_xx_YY.dic  # División silábica
├── th_xx_YY.dat    # Sinónimos (datos)
├── th_xx_YY.idx    # Sinónimos (índice)
├── description.xml # Metadatos
├── dictionaries.xcu# Configuración
└── README_*.txt    # Información del idioma
```

## 🤝 Contribuciones
¡Las contribuciones son bienvenidas! Si encuentras:
- Diccionarios faltantes
- Errores en los archivos
- Problemas de licencia

Abre un *issue* o envía un *pull request*.

## 📄 Créditos
- **Fuente original**: [LibreOffice Portable](https://portableapps.com/)
- **Desarrolladores**: Equipo de LibreOffice y colaboradores de diccionarios
- **Licencias**: Ver archivos específicos de cada idioma

---

**Última actualización**: Extraídos de LibreOffice 25.2.3 (2024)
```

---
