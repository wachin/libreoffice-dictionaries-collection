# Hunspell & Mythes Dictionaries for Desktop Applications

This release contains **Hunspell** (spell-checking `.aff`/`.dic`) and **Mythes**
(thesaurus `.dat`/`.idx`) dictionaries extracted from
[LibreOffice Portable](https://portableapps.com/apps/office/libreoffice_portable)
for Windows, published by PortableApps.com.

These are the same dictionaries used by LibreOffice — standard Hunspell format,
compatible with any application that supports Hunspell spell-checking and
Mythes thesaurus.

## Intended use

These dictionaries are designed to be used by:

- **[GuitarChordStudio](https://github.com/wachin/guitarchordstudio)** —
  ChordPages and ChordFlow applications let users download dictionaries on
  demand from within the app's interface.
- **Other developers** — You are welcome to use these archives in your own
  programs, NSIS installers, or package managers. Each dictionary is packaged
  individually so you can include only the languages your users need.

## How to use

1. Download the `.tar.gz` archive(s) for your language(s) from the Assets
   section below.
2. Extract the contents. Each archive contains a `dict-XX/` folder with:
   - `.aff` and `.dic` files for Hunspell spell-checking
   - `.dat` and `.idx` files for Mythes thesaurus (when available)
3. Point your Hunspell spell-checker to the folder containing the `.aff`/`.dic`
   files, or let the user select their language from the application's UI.

## Dictionary list

| Language | Hunspell (spell) | Mythes (thesaurus) |
|---|---|---|
| Afrikaans | `dict-af` | — |
| Aragonese | `dict-an` | — |
| Arabic | `dict-ar` | `th_ar.dat` / `th_ar.idx` |
| Belarusian | `dict-be` | — |
| Bulgarian | `dict-bg` | `th_bg_BG_v2.dat` / `th_bg_BG_v2.idx` |
| Bengali | `dict-bn` | — |
| Classical Tibetan | `dict-bo` | — |
| Breton | `dict-br` | — |
| Bosnian | `dict-bs` | — |
| Catalan | `dict-ca` | `th_ca_ES_v3.dat` / `th_ca_ES_v3.idx` |
| Central Kurdish | `dict-ckb` | — |
| Czech | `dict-cs` | `thes_cs_CZ.dat` / `thes_cs_CZ.idx` |
| Danish | `dict-da` | `th_da_DK.dat` / `th_da_DK.idx` |
| German | `dict-de` | `th_de_CH_v2`, `th_de_DE_v2` |
| Modern Greek | `dict-el` | — |
| English | `dict-en` | `th_en_US_v2.dat` / `th_en_US_v2.idx` |
| Esperanto | `dict-eo` | `th_eo.dat` / `th_eo.idx` |
| Spanish | `dict-es` | `th_es_v2.dat` / `th_es_v2.idx` |
| Estonian | `dict-et` | — |
| Persian | `dict-fa` | — |
| French | `dict-fr` | `thes_fr.dat` / `thes_fr.idx` |
| Scottish Gaelic | `dict-gd` | — |
| Galician | `dict-gl` | `thesaurus_gl.dat` / `thesaurus_gl.idx` |
| Gujarati | `dict-gu` | — |
| Hebrew | `dict-he` | — |
| Hindi | `dict-hi` | — |
| Croatian | `dict-hr` | — |
| Hungarian | `dict-hu` | `th_hu_HU_v2.dat` / `th_hu_HU_v2.idx` |
| Indonesian | `dict-id` | `th_id_ID_v2.dat` / `th_id_ID_v2.idx` |
| Icelandic | `dict-is` | `th_is.dat` / `th_is.idx` |
| Italian | `dict-it` | `th_it_IT_v2.dat` / `th_it_IT_v2.idx` |
| Korean | `dict-ko` | — |
| Lao | `dict-lo` | — |
| Lithuanian | `dict-lt` | — |
| Latvian | `dict-lv` | `th_lv_LV_v2.dat` / `th_lv_LV_v2.idx` |
| Mongolian | `dict-mn` | — |
| Nepali | `dict-ne` | `th_ne_NP_v2.dat` / `th_ne_NP_v2.idx` |
| Dutch | `dict-nl` | — |
| Norwegian | `dict-no` | `th_nb_NO_v2`, `th_nn_NO_v2` |
| Occitan | `dict-oc` | — |
| Polish | `dict-pl` | `th_pl_PL_v2.dat` / `th_pl_PL_v2.idx` |
| Portuguese (Brazil) | `dict-pt-BR` | `th_pt_BR.dat` / `th_pt_BR.idx` |
| Portuguese (Portugal) | `dict-pt-PT` | `th_pt_PT.dat` / `th_pt_PT.idx` |
| Romanian | `dict-ro` | `th_ro_RO_v2.dat` / `th_ro_RO_v2.idx` |
| Russian | `dict-ru` | `th_ru_RU_M_aot_and_v2` |
| Sinhalese | `dict-si` | — |
| Slovak | `dict-sk` | `th_sk_SK_v2.dat` / `th_sk_SK_v2.idx` |
| Slovenian | `dict-sl` | `th_sl_SI_v2.dat` / `th_sl_SI_v2.idx` |
| Albanian | `dict-sq` | — |
| Serbian | `dict-sr` | — |
| Swedish | `dict-sv` | `th_sv_SE.dat` / `th_sv_SE.idx` |
| Telugu | `dict-te` | — |
| Thai | `dict-th` | — |
| Turkish | `dict-tr` | — |
| Ukrainian | `dict-uk` | `th_uk_UA.dat` / `th_uk_UA.idx` |
| Vietnamese | `dict-vi` | — |
| Zulu | `dict-zu` | — |

## Notes

- **Hunspell dictionaries** — The `.dic` file contains the word list and the
  `.aff` file contains the affix rules. Both are required for spell-checking.
- **Mythes thesaurus dictionaries** — The `.dat` file contains the synonym data
  and the `.idx` file is the index. Both are required for the thesaurus feature.
  The `.idx` file can be regenerated from the `.dat` file if missing.
- Some languages include multiple regional variants (e.g. German has Swiss and
  German variants, Norwegian has Bokmål and Nynorsk).
- These dictionaries are extracted from LibreOffice Portable for Windows and
  are compatible with any application that supports the Hunspell and Mythes
  formats — on Linux, Windows, and macOS.

---

*Source: https://github.com/wachin/libreoffice-dictionaries-collection*
*Original source: https://portableapps.com/apps/office/libreoffice_portable*