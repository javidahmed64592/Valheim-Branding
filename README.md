[![Python](https://img.shields.io/badge/Python-3.13-3776AB.svg?style=flat&logo=python&logoColor=ffd343)](https://docs.python.org/3.13/)
[![CI](https://img.shields.io/github/actions/workflow/status/javidahmed64592/valheim-branding/ci.yml?branch=main&style=flat-square&label=CI&logo=github)](https://github.com/javidahmed64592/valheim-branding/actions/workflows/ci.yml)
[![Build](https://img.shields.io/github/actions/workflow/status/javidahmed64592/valheim-branding/build.yml?branch=main&style=flat-square&label=Build&logo=github)](https://github.com/javidahmed64592/valheim-branding/actions/workflows/build.yml)
[![Docs](https://img.shields.io/github/actions/workflow/status/javidahmed64592/valheim-branding/docs.yml?branch=main&style=flat-square&label=Docs&logo=github)](https://github.com/javidahmed64592/valheim-branding/actions/workflows/docs.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<!-- omit from toc -->
# Valheim-Branding

Visual branding rules and icon generator for the Aestelwen Valheim mods.

One tile, one frame, one seal. Only the middle changes. See [BRAND.md](BRAND.md) for the rules.

<!-- omit from toc -->
## Table of Contents
- [Quick start](#quick-start)
- [Layout](#layout)
- [Mods](#mods)
- [License](#license)

## Quick start

```bash
uv sync --all-extras

# Build dist/<Mod>/icon.png for every mod
uv run build-icons
```

## Layout

| Path | What it is |
| --- | --- |
| `tokens/palette.json` | Colour tokens |
| `tokens/layout.json` | Sizes and positions for the tile, studs, glyph and seal |
| `assets/mark/` | The Longhouse A |
| `assets/glyphs/` | One 100x100 SVG per mod |
| `mods.json` | Which mods exist, glyph and accent |
| `src/build_icons.py` | Composes the 256x256 icons |
| `scripts/apply-icons.sh` | Copies built icons into the mod repos |
| `dist/` | Built icons, committed so each mod can pull the current one |

## Mods

DvergrWorkers, HalfBeam, HomeBubble, NoHammerBuildMenu, PortalNetwork, TarExtractor.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
