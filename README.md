[![Python](https://img.shields.io/badge/Python-3.13-3776AB.svg?style=flat&logo=python&logoColor=ffd343)](https://docs.python.org/3.13/)
[![CI](https://img.shields.io/github/actions/workflow/status/javidahmed64592/valheim-branding/ci.yml?branch=main&style=flat-square&label=CI&logo=github)](https://github.com/javidahmed64592/valheim-branding/actions/workflows/ci.yml)
[![Docs](https://img.shields.io/github/actions/workflow/status/javidahmed64592/valheim-branding/docs.yml?branch=main&style=flat-square&label=Docs&logo=github)](https://github.com/javidahmed64592/valheim-branding/actions/workflows/docs.yml)
[![Icons](https://img.shields.io/github/actions/workflow/status/javidahmed64592/valheim-branding/icons.yml?branch=main&style=flat-square&label=Icons&logo=github)](https://github.com/javidahmed64592/valheim-branding/actions/workflows/icons.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<!-- omit from toc -->
# Valheim-Branding

Visual branding rules and icon generator for the Aestelwen Valheim mods.

One tile, one frame, one seal. Only the middle changes. See [BRAND.md](BRAND.md) for the rules.

<!-- omit from toc -->
## Table of Contents
- [Quick start](#quick-start)
- [Layout](#layout)
- [License](#license)

## Quick start

```bash
uv sync --all-extras

# Build dist/<Mod>/icon.png for every glyph, plus dist/contact-sheet.png
uv run build-icons
```

The [Icons workflow](.github/workflows/icons.yml) runs the same command on every push and pull request and uploads `dist/` as an artifact named `valheim-branding-icons`. It can also be run by hand from the Actions tab.

## Layout

| Path | What it is |
| --- | --- |
| `tokens/palette.json` | Colour tokens |
| `tokens/layout.json` | Sizes and positions for the tile, studs, glyph and seal |
| `assets/mark/` | The Longhouse A |
| `assets/glyphs/` | One 100x100 SVG per mod; each file becomes one icon |
| `valheim_branding/build_icons.py` | Composes the 256x256 icons |
| `dist/` | Built icons (not committed); the Icons workflow uploads them as an artifact |

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
