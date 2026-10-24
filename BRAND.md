# Aestelwen Valheim mod branding

The rules every mod icon follows.
The goal: from the icon alone you can tell "this is an Aestelwen mod" and roughly what it does, and it feels like Valheim.

Icons are 256x256 PNGs (the Thunderstore size), built by `valheim_branding/build_icons.py` from the tokens, the mark and one glyph per mod.
Never hand-edit a built icon.

## The anatomy

Every icon has exactly these layers, back to front:

1. **Ground**: radial glow from Umber Glow (centre) to Umber Black (edge).
2. **Frame**: bronze gradient border, a Bronze Dark hairline inside it, and a stud in three corners.
3. **Glyph**: one subject, centred slightly up and left of the tile centre.
4. **Maker's seal**: the ember-gold Longhouse A in a round bronze seal, bottom right. The fourth corner has no stud because the seal sits there.

All positions and sizes live in `tokens/layout.json`.

## Palette

Defined in `tokens/palette.json`.

| Group | Token | Hex | Use |
| --- | --- | --- | --- |
| Ground | Umber Black | `#14100D` | Tile edge, seal fill |
| Ground | Umber | `#221A14` | Panels, inner discs |
| Ground | Umber Glow | `#3A2A1C` | Light behind the glyph |
| Frame | Bronze | `#B07A3C` | Border, rings |
| Frame | Bronze Dark | `#6E4A22` | Hairlines, shading |
| Frame | Bronze Light | `#D9A15A` | Frame highlight |
| Signature | Ember Gold | `#F0B04A` | The A, and tiny highlights only |
| Accent | Wood | `#B77C3F` | Building mods |
| Accent | Frost | `#7CC4E8` | Protection |
| Accent | Portal Cyan | `#43D3E6` | Travel |
| Accent | Tar | `#0B0B0E` | Tar and shadow |

**The rule:** umber ground, bronze frame, ember-gold A, and at most one subject accent.

## The mark

The Longhouse A (`assets/mark/longhouse-a.svg`): a solid gable silhouette with a window and a doorway cut out.
Always Ember Gold, always in the seal, never resized outside the seal.

## Glyph rules

- One subject per icon. If you need two ideas, pick the one a player would search for.
- Drawn in a 100x100 box in `assets/glyphs/<Mod>.svg`, self-contained (any gradients defined inside the file).
- Flat or lightly shaded. No glossy highlights beyond a single small glint.
- Dark outline in Bronze Dark or a darker shade of the fill, about 2 units wide.
- One accent colour from the palette. Everything else is wood, bronze or umber tones.
- No text or numbers inside a glyph. They do not survive small sizes.
- Keep the bottom-right corner of the glyph box quiet: the seal overlaps it.

## Adding a mod

1. Draw `assets/glyphs/<Mod>.svg` following the glyph rules.
2. Regenerate with `uv run build-icons`. The icon is written to `dist/<Mod>/icon.png`; no registry file to update.
