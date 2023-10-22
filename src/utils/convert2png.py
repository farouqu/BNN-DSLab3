import os
import cairosvg

def convert_svg_to_png(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # List all files in the input folder
    files = os.listdir(input_folder)

    for file in files:
        if file.endswith(".svg"):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file.replace(".svg", ".png"))

            # Convert SVG to PNG
            cairosvg.svg2png(url=input_path, write_to=output_path)

if __name__ == "__main__":
    input_folder = "../datasets/Finnish_dataset/svg/"
    output_folder = "../datasets/Finnish_dataset/png/"

    convert_svg_to_png(input_folder, output_folder)
