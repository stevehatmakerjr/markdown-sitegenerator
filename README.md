# Markdown SiteGen

A minimal **Markdown-to-HTML static site generator** written in Python.

## Features
- Converts `.md` files in `/content` into `.html` files in `/output`
- Automatically generates navigation links for all Markdown files
- Uses Jinja2 templates for consistent page structure
- Configurable title and author via `config.yaml`

## How It Works
1. Put your Markdown files in the `content/` folder.
2. Run:
   ```bash
   python generator.py
   ```
3. Your site appears in the `output/` folder.

## Requirements
```bash
pip install markdown jinja2 pyyaml
```
## License
MIT
