#!/usr/bin/env bash

# Change to the markdowns directory
cd track_markdowns

# Define the output directory for PDFs
output_dir="../track_pdfs"

# Ensure the output directory exists
mkdir -p "$output_dir"

# Loop through each markdown file and convert it to PDF
for md_file in *.md; do
    # Get the base name of the file without the extension
    base_name=$(basename "$md_file" .md)

    # Run pandoc to convert the markdown file to PDF
    pandoc "$md_file" -s -c ../style.css -o "$output_dir/${base_name}.pdf"
done
