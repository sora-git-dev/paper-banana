"""
PaperBanana local demo.

This script creates a clean SVG diagram from a text prompt. It is a lightweight
reference implementation for the repository, so it runs without a hosted model,
GPU, or API key.

Example:
    python inference.py --input "Dataset, encoder, attention block, decoder, evaluation"
"""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path
from typing import Dict, List

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


DEFAULT_CONFIG: Dict[str, Dict[str, object]] = {
    "styles": {
        "clean_tech": {
            "colors": ["#1d4ed8", "#2563eb", "#60a5fa", "#dbeafe"],
            "font": "Inter, Arial, sans-serif",
            "line_width": 2,
        },
        "classic_journal": {
            "colors": ["#111827", "#374151", "#9ca3af", "#f3f4f6"],
            "font": "Georgia, Times New Roman, serif",
            "line_width": 1,
        },
        "modern_ai": {
            "colors": ["#6d28d9", "#7c3aed", "#c4b5fd", "#f5f3ff"],
            "font": "Inter, Arial, sans-serif",
            "line_width": 2,
        },
    },
    "output": {
        "format": "svg",
        "width": 1180,
        "height": 520,
    },
}


def load_config(config_path: str = "default.yaml") -> Dict[str, Dict[str, object]]:
    """Load YAML config when available, otherwise fall back to defaults."""
    path = Path(config_path)
    if not path.exists() or yaml is None:
        return DEFAULT_CONFIG
    with path.open("r", encoding="utf-8") as file:
        loaded = yaml.safe_load(file) or {}
    merged = DEFAULT_CONFIG.copy()
    merged.update(loaded)
    return merged


def split_prompt(prompt: str) -> List[str]:
    """Convert a free-form prompt into diagram node labels."""
    cleaned = re.sub(r"\s+", " ", prompt.strip())
    parts = re.split(r"\s*(?:,|->|=>|;|\bthen\b|\bto\b)\s*", cleaned, flags=re.I)
    nodes = [part.strip(" .:-") for part in parts if len(part.strip(" .:-")) > 2]
    if len(nodes) >= 3:
        return nodes[:7]
    words = cleaned.split()
    if len(words) <= 4:
        return [cleaned, "Plan layout", "Render diagram", "Review output"]
    chunks = [
        " ".join(words[0:3]),
        " ".join(words[3:6]),
        " ".join(words[6:9]) or "Visualize",
        "Review output",
    ]
    return [chunk for chunk in chunks if chunk]


def wrap_label(label: str, max_chars: int = 18) -> List[str]:
    """Wrap node text into SVG-friendly lines."""
    words = label.split()
    lines: List[str] = []
    current: List[str] = []
    for word in words:
        candidate = " ".join(current + [word])
        if len(candidate) > max_chars and current:
            lines.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        lines.append(" ".join(current))
    return lines[:3]


def render_svg(prompt: str, style: str, config: Dict[str, Dict[str, object]]) -> str:
    """Render a horizontal workflow diagram as SVG."""
    styles = config.get("styles", {})
    style_config = styles.get(style, styles["clean_tech"])
    colors = style_config["colors"]
    font = style_config["font"]
    line_width = style_config["line_width"]
    width = int(config.get("output", {}).get("width", 1180))
    height = int(config.get("output", {}).get("height", 520))
    nodes = split_prompt(prompt)

    margin_x = 80
    card_w = 160
    card_h = 96
    center_y = 245
    usable_w = width - margin_x * 2 - card_w
    step = usable_w / max(len(nodes) - 1, 1)

    cards = []
    arrows = []
    for index, node in enumerate(nodes):
        x = margin_x + int(index * step)
        y = center_y - card_h // 2
        label_lines = wrap_label(node)
        text_lines = []
        for line_index, line in enumerate(label_lines):
            text_lines.append(
                f'<text x="{x + card_w / 2}" y="{y + 42 + line_index * 19}" '
                f'text-anchor="middle" font-size="15" fill="#111827">{html.escape(line)}</text>'
            )
        cards.append(
            f"""
            <g>
              <rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" rx="14"
                    fill="white" stroke="{colors[1]}" stroke-width="{line_width}"/>
              <circle cx="{x + 22}" cy="{y + 22}" r="12" fill="{colors[1]}"/>
              <text x="{x + 22}" y="{y + 27}" text-anchor="middle" font-size="13"
                    font-weight="700" fill="white">{index + 1}</text>
              {''.join(text_lines)}
            </g>
            """
        )
        if index < len(nodes) - 1:
            start_x = x + card_w + 12
            end_x = margin_x + int((index + 1) * step) - 12
            arrows.append(
                f'<path d="M {start_x} {center_y} L {end_x} {center_y}" '
                f'stroke="{colors[0]}" stroke-width="{line_width}" marker-end="url(#arrow)" />'
            )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3"
            orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="{colors[0]}" />
    </marker>
    <linearGradient id="bg" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="{colors[3]}" />
      <stop offset="100%" stop-color="#ffffff" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#bg)" />
  <text x="80" y="72" font-family="{font}" font-size="34" font-weight="800" fill="#0f172a">
    PaperBanana Diagram Draft
  </text>
  <text x="80" y="108" font-family="{font}" font-size="16" fill="#475569">
    Prompt: {html.escape(prompt[:120])}
  </text>
  <g font-family="{font}">
    {''.join(arrows)}
    {''.join(cards)}
  </g>
  <text x="{width - 80}" y="{height - 42}" text-anchor="end" font-family="{font}"
        font-size="14" fill="#64748b">Generated with PaperBanana local demo</text>
</svg>
"""


def generate_diagram(
    prompt: str,
    style: str = "clean_tech",
    output_format: str = "svg",
    output_dir: str = "outputs",
    config_path: str = "default.yaml",
) -> Path:
    """Generate an SVG diagram and return its path."""
    if output_format != "svg":
        raise ValueError("The local demo currently supports SVG output.")
    config = load_config(config_path)
    output_path = Path(output_dir) / "diagram.svg"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_svg(prompt, style, config), encoding="utf-8")
    print(f"[PaperBanana] Created {output_path}")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="PaperBanana local SVG diagram generator")
    parser.add_argument("--input", "-i", required=True, help="Text description of the diagram")
    parser.add_argument(
        "--style",
        "-s",
        default="clean_tech",
        choices=["clean_tech", "classic_journal", "modern_ai"],
        help="Visual style preset",
    )
    parser.add_argument("--format", "-f", default="svg", choices=["svg"], help="Output format")
    parser.add_argument("--output", "-o", default="outputs", help="Output directory")
    parser.add_argument("--config", "-c", default="default.yaml", help="Path to YAML config")
    args = parser.parse_args()
    generate_diagram(args.input, args.style, args.format, args.output, args.config)


if __name__ == "__main__":
    main()
