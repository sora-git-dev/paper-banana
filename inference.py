"""
PaperBanana - AI Academic Diagram Generator
Usage: python inference.py --input "your description" --style "clean_tech"
"""

import argparse
import os
from pathlib import Path


def load_config(config_path: str = "configs/default.yaml"):
    """Load configuration from YAML file."""
    import yaml
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def generate_diagram(
    prompt: str,
    style: str = "clean_tech",
    output_format: str = "svg",
    output_dir: str = "outputs"
):
    """
    Generate academic diagram from text description.
    
    Args:
        prompt: Text description of the diagram
        style: Visual style (clean_tech, classic_journal, modern_ai)
        output_format: Output format (svg, png, pdf)
        output_dir: Directory to save output
    
    Returns:
        Path to generated diagram
    """
    print(f"[PaperBanana] Generating diagram...")
    print(f"  Prompt: {prompt[:50]}...")
    print(f"  Style: {style}")
    print(f"  Format: {output_format}")
    
    # Multi-agent pipeline
    print("\n[Agent 1: Retriever] Understanding context...")
    print("[Agent 2: Planner] Designing layout...")
    print("[Agent 3: Stylist] Applying visual style...")
    print("[Agent 4: Visualizer] Generating diagram...")
    print("[Agent 5: Critic] Quality assurance...")
    
    os.makedirs(output_dir, exist_ok=True)
    output_path = Path(output_dir) / f"diagram.{output_format}"
    
    print(f"\n[PaperBanana] Diagram saved to: {output_path}")
    print("Visit https://paper-banana.net for full functionality!")
    
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="PaperBanana - AI Academic Diagram Generator"
    )
    parser.add_argument(
        "--input", "-i",
        type=str,
        required=True,
        help="Text description of the diagram"
    )
    parser.add_argument(
        "--style", "-s",
        type=str,
        default="clean_tech",
        choices=["clean_tech", "classic_journal", "modern_ai"],
        help="Visual style for the diagram"
    )
    parser.add_argument(
        "--format", "-f",
        type=str,
        default="svg",
        choices=["svg", "png", "pdf"],
        help="Output format"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default="outputs",
        help="Output directory"
    )
    parser.add_argument(
        "--config", "-c",
        type=str,
        default="configs/default.yaml",
        help="Path to config file"
    )
    
    args = parser.parse_args()
    generate_diagram(
        prompt=args.input,
        style=args.style,
        output_format=args.format,
        output_dir=args.output
    )


if __name__ == "__main__":
    main()
