#!/bin/bash

input_folder="./datasets/Finnish_dataset/svg/"
output_folder="./datasets/Finnish_dataset/png/"

# Ensure the output folder exists
mkdir -p "$output_folder"

# Loop through SVG files in the input folder
for svg_file in "$input_folder"/*.svg; do
    # Extract the filename without the extension
    base_name=$(basename -- "$svg_file")
    filename_no_extension="${base_name%.svg}"

    # Generate the output PNG filename
    png_file="$output_folder/$filename_no_extension.png"

    # Convert SVG to PNG using ImageMagick
    convert "$svg_file" "$png_file"
done
