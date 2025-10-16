import os
import yaml
from markdown import markdown
from jinja2 import Environment, FileSystemLoader

# Load config
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# Setup Jinja environment
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("base.html")

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

def build_site():
    content_dir = "content"
    output_dir = "output"

    # Build a list of all markdown pages
    pages = [f for f in os.listdir(content_dir) if f.endswith(".md")]
    nav_links = [
        {
            "name": f.replace(".md", "").capitalize(),
            "href": f.replace(".md", ".html")
        }
        for f in pages
    ]

    for filename in pages:
        filepath = os.path.join(content_dir, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            markdown_text = f.read()

        html_content = markdown(markdown_text)
        html_output = template.render(
            site_title=config.get("site_title", "My Site"),
            content=html_content,
            page_title=filename.replace(".md", "").capitalize(),
            nav_links=nav_links
        )

        output_filename = filename.replace(".md", ".html")
        output_path = os.path.join(output_dir, output_filename)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_output)

        print(f"Generated: {output_filename}")

if __name__ == "__main__":
    build_site()
    print("Site build complete!")
