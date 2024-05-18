#!/usr/bin/env python3

import yaml
import os
from jinja2 import Environment, FileSystemLoader

# Load the YAML file
with open('tracks.yaml', 'r') as file:
    tracks_data = yaml.safe_load(file)

# Create a directory to store the markdown files
output_directory = "track_markdowns"
os.makedirs(output_directory, exist_ok=True)

# Set up Jinja2 environment and load template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('track_template.md.jinja2')

# Function to create a markdown file for each track
def create_markdown_file(track):
    track_name = track['track_name']
    corners = sorted(track['corners'], key=lambda x: x['number'])

    # Render the template with the track data
    markdown_content = template.render(track_name=track_name, corners=corners)

    # Write the rendered content to a file
    file_path = os.path.join(output_directory, f"{track_name}.md")
    with open(file_path, "w") as f:
        f.write(markdown_content)
    print(f"Created file: {file_path}")

# Process each track in the YAML data
for track in tracks_data['tracks']:
    create_markdown_file(track)
