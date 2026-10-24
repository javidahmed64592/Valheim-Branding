"""Tests for the valheim_branding.build_icons module."""

import shutil
from pathlib import Path

import pytest
from PIL import Image

from valheim_branding import build_icons

REPO_ROOT = Path(__file__).resolve().parent.parent
GLYPHS = sorted((REPO_ROOT / "assets" / "glyphs").glob("*.svg"))
ICON_SIZE = 256


@pytest.fixture
def project_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Copy the tokens and assets into a temporary root so builds never touch the real dist folder."""
    for folder in ("tokens", "assets"):
        shutil.copytree(REPO_ROOT / folder, tmp_path / folder)
    monkeypatch.setattr(build_icons, "ROOT", tmp_path)
    return tmp_path


def test_load_json_reads_layout() -> None:
    """Test that load_json reads a file relative to the project root."""
    layout = build_icons.load_json("tokens/layout.json")
    assert layout["size"] == ICON_SIZE


def test_inner_svg_returns_markup_between_svg_tags(tmp_path: Path) -> None:
    """Test that inner_svg strips the outer svg element."""
    svg = tmp_path / "shape.svg"
    svg.write_text('<svg viewBox="0 0 100 100"><circle r="5"/></svg>')
    assert build_icons.inner_svg(svg) == '<circle r="5"/>'


def test_inner_svg_rejects_files_without_svg_tags(tmp_path: Path) -> None:
    """Test that inner_svg raises for a file that is not an SVG."""
    not_svg = tmp_path / "shape.svg"
    not_svg.write_text("hello")
    with pytest.raises(ValueError, match="is not a valid SVG"):
        build_icons.inner_svg(not_svg)


def test_place_centres_and_scales_markup() -> None:
    """Test that place fits a 100x100 asset into a square centred on the given point."""
    placed = build_icons.place("<g/>", 100, 50, 50)
    assert "translate(75.00,25.00)" in placed
    assert "scale(0.5000)" in placed
    assert "<g/>" in placed


def test_build_svg_contains_every_layer() -> None:
    """Test that build_svg includes the glyph, the mark, the studs and the palette colours."""
    palette = build_icons.load_json("tokens/palette.json")
    layout = build_icons.load_json("tokens/layout.json")

    svg = build_icons.build_svg('<g id="glyph"/>', '<g id="mark"/>', palette, layout)

    assert f'viewBox="0 0 {ICON_SIZE} {ICON_SIZE}"' in svg
    assert '<g id="glyph"/>' in svg
    assert '<g id="mark"/>' in svg
    assert svg.count('fill="url(#bronze)"') == len(layout["studs"]["positions"])
    assert palette["ground"]["umberGlow"] in svg
    assert palette["frame"]["bronze"] in svg


def test_mark_is_a_valid_svg() -> None:
    """Test that the Longhouse A mark can be read and contains a path."""
    assert "<path" in build_icons.inner_svg(REPO_ROOT / "assets" / "mark" / "longhouse-a.svg")


@pytest.mark.parametrize("glyph", GLYPHS, ids=lambda glyph: glyph.stem)
def test_glyphs_are_valid_svgs(glyph: Path) -> None:
    """Test that every glyph file can be read and is not empty."""
    assert build_icons.inner_svg(glyph).strip()


def test_main_builds_an_icon_for_every_glyph(project_root: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """Test that main writes a 256x256 icon per glyph plus a contact sheet."""
    build_icons.main()

    for glyph in GLYPHS:
        with Image.open(project_root / "dist" / glyph.stem / "icon.png") as icon:
            assert icon.size == (ICON_SIZE, ICON_SIZE)

    with Image.open(project_root / "dist" / "contact-sheet.png") as sheet:
        assert sheet.size == (ICON_SIZE * len(GLYPHS), ICON_SIZE)

    assert capsys.readouterr().out.count("built ") == len(GLYPHS) + 1
