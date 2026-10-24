"""Build Thunderstore icons (256x256 PNG) for every glyph in assets/glyphs.

Every icon is the same tile: bronze frame, warm umber glow, one centred glyph,
and the ember-gold Longhouse A in a round seal at the bottom right.
"""

import json
import re
from pathlib import Path

import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent


def load_json(rel: str) -> dict:
    """Load a JSON file relative to the project root and return it as a dictionary."""
    return json.loads((ROOT / rel).read_text())


def inner_svg(path: Path) -> str:
    """Return the markup inside the outer <svg> of an asset file."""
    match = re.search(r"<svg[^>]*>(.*)</svg>", path.read_text(), re.DOTALL)
    if not match:
        error_msg = f"{path} is not a valid SVG"
        raise ValueError(error_msg)
    return match.group(1)


def place(markup: str, cx: float, cy: float, size: float) -> str:
    """Fit a 100x100 asset into a square of `size` centred on (cx, cy)."""
    scale = size / 100
    return f'<g transform="translate({cx - size / 2:.2f},{cy - size / 2:.2f}) scale({scale:.4f})">{markup}</g>'


def build_svg(glyph_markup: str, mark_markup: str, palette: dict, layout: dict) -> str:
    """Build the complete SVG for a mod icon using the given glyph, mark, palette, and layout."""
    g, f = palette["ground"], palette["frame"]
    size = layout["size"]
    fr, il, st = layout["frame"], layout["innerLine"], layout["studs"]
    gl, se = layout["glyph"], layout["seal"]

    studs = "".join(f'<circle cx="{x}" cy="{y}" r="{st["radius"]}" fill="url(#bronze)"/>' for x, y in st["positions"])
    defs = (
        "<defs>"
        '<radialGradient id="glow" cx="50%" cy="46%" r="70%">'
        f'<stop offset="0" stop-color="{g["umberGlow"]}"/>'
        f'<stop offset="1" stop-color="{g["umberBlack"]}"/>'
        "</radialGradient>"
        '<linearGradient id="bronze" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="{f["bronzeLight"]}"/>'
        f'<stop offset=".5" stop-color="{f["bronze"]}"/>'
        f'<stop offset="1" stop-color="{f["bronzeDark"]}"/>'
        "</linearGradient>"
        "</defs>"
    )
    fx, fw = fr["inset"], size - 2 * fr["inset"]
    ix, iw = il["inset"], size - 2 * il["inset"]
    seal = (
        f'<circle cx="{se["centerX"]}" cy="{se["centerY"]}" r="{se["radius"]}" '
        f'fill="{g["umberBlack"]}" stroke="url(#bronze)" stroke-width="{se["ringWidth"]}"/>'
        f'<circle cx="{se["centerX"]}" cy="{se["centerY"]}" r="{se["radius"] - se["innerRingInset"]}" '
        f'fill="none" stroke="{f["bronzeDark"]}" stroke-width="1.2"/>'
        + place(mark_markup, se["centerX"], se["centerY"], se["radius"] * se["markScale"])
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}">'
        + defs
        + f'<rect width="{size}" height="{size}" fill="url(#glow)"/>'
        + f'<rect x="{fx}" y="{fx}" width="{fw}" height="{fw}" rx="{fr["radius"]}" fill="none" '
        f'stroke="url(#bronze)" stroke-width="{fr["strokeWidth"]}"/>'
        + f'<rect x="{ix}" y="{ix}" width="{iw}" height="{iw}" rx="{il["radius"]}" fill="none" '
        f'stroke="{f["bronzeDark"]}" stroke-width="{il["strokeWidth"]}"/>'
        + studs
        + place(glyph_markup, gl["centerX"], gl["centerY"], gl["size"])
        + seal
        + "</svg>"
    )


def main() -> None:
    """Main entry point for the build-icons script."""
    palette = load_json("tokens/palette.json")
    layout = load_json("tokens/layout.json")
    glyphs = sorted((ROOT / "assets" / "glyphs").glob("*.svg"))

    mark = inner_svg(ROOT / "assets" / "mark" / "longhouse-a.svg").replace("#F0B04A", palette["signature"]["emberGold"])
    out_root = ROOT / "dist"
    built = []
    for glyph in glyphs:
        svg = build_svg(inner_svg(glyph), mark, palette, layout)
        out_dir = out_root / glyph.stem
        out_dir.mkdir(parents=True, exist_ok=True)
        png = out_dir / "icon.png"
        cairosvg.svg2png(
            bytestring=svg.encode(), write_to=str(png), output_width=layout["size"], output_height=layout["size"]
        )
        built.append(png)
        print(f"built {png.relative_to(ROOT)}")

    sheet = Image.new("RGB", (layout["size"] * len(built), layout["size"]), (40, 40, 40))
    for i, png in enumerate(built):
        sheet.paste(Image.open(png).convert("RGB"), (i * layout["size"], 0))
    sheet.save(out_root / "contact-sheet.png")
    print(f"built {(out_root / 'contact-sheet.png').relative_to(ROOT)}")
