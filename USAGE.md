# PaperBanana Usage Guide

## Quick Start

### Online (Recommended)
Visit [paper-banana.net](https://paper-banana.net) for the full web experience.

### Local Installation

```bash
# Clone repository
git clone https://github.com/sora-git-dev/paper-banana.git
cd paper-banana

# Install dependencies
pip install -r requirements.txt

# Run inference
python inference.py --input "Neural network architecture with 3 layers" --style clean_tech
```

## Styles

| Style | Best For |
|-------|----------|
| `clean_tech` | ML/AI papers, technical diagrams |
| `classic_journal` | Nature, Science, traditional journals |
| `modern_ai` | NeurIPS, ICML, modern AI conferences |

## Multi-Agent Pipeline

PaperBanana uses 5 specialized agents:

1. **Retriever** - Understands scientific context
2. **Planner** - Designs optimal layout
3. **Stylist** - Applies visual styling
4. **Visualizer** - Generates the diagram
5. **Critic** - Ensures quality standards

## Examples

### Architecture Diagram
```bash
python inference.py -i "Transformer architecture with attention mechanism"
```

### Flowchart
```bash
python inference.py -i "Data preprocessing pipeline: load, clean, transform, save"
```

### Statistical Plot
```bash
python inference.py -i "Bar chart comparing model accuracy across datasets"
```

## Output Formats

- **SVG** - Best for LaTeX, scalable
- **PNG** - Universal compatibility
- **PDF** - Print-ready

## Configuration

Edit `configs/default.yaml` to customize:
- Model settings
- Agent behavior
- Style definitions
- Output preferences

## Need Help?

- Documentation: https://paper-banana.net/docs
- Issues: https://github.com/sora-git-dev/paper-banana/issues
