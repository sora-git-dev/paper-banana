# PaperBanana Usage Guide

This guide explains how to run the local PaperBanana demo and generate an SVG diagram from a text prompt.

## Install

```bash
pip install -r requirements.txt
```

The repository demo only requires `pyyaml`. It does not need a GPU or model download.

## Generate a diagram

```bash
python inference.py \
  --input "Dataset, preprocessing, encoder, attention block, decoder, evaluation" \
  --style clean_tech
```

The output is saved to:

```text
outputs/diagram.svg
```

## Try different styles

```bash
python inference.py -i "Patient cohort, feature extraction, model training, validation, report" -s classic_journal
```

```bash
python inference.py -i "Prompt, agent planner, renderer, critic, final figure" -s modern_ai
```

## Prompt tips

PaperBanana works best when the prompt names the main steps or components:

- Use comma-separated steps for workflow diagrams.
- Use short nouns for architecture diagrams.
- Keep labels concise for cleaner SVG output.

Good example:

```text
Dataset, preprocessing, encoder, attention block, decoder, evaluation
```

Less useful example:

```text
Make a nice research diagram.
```

## Configuration

Edit `default.yaml` to change:

- Style colors
- Font family
- Line width
- Canvas width and height

## Output format

The local demo currently writes SVG. SVG is easy to edit in Figma, Illustrator, Inkscape, VS Code, and many paper-writing workflows.

## Online version

For richer AI-assisted diagram generation, visit:

https://paper-banana.net/
