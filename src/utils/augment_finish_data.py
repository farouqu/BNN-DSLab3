import os
from PIL import Image
import Augmentor

def perform_augmentation(input_folder, num_augmented_samples=9):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Create an Augmentor pipeline for augmentation
    pipeline = Augmentor.Pipeline(input_folder)

    # Define augmentation operations (you can customize these based on your requirements)
    pipeline.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
    pipeline.flip_left_right(probability=0.5)
    pipeline.zoom_random(probability=0.5, percentage_area=0.8)
    pipeline.flip_top_bottom(probability=0.5)

    # Set the number of augmented samples to generate
    pipeline.sample(num_augmented_samples)

if __name__ == "__main__":
    input_folder = "../../datasets/Finnish_dataset/png/"
    output_folder = "../../datasets/Finnish_dataset/png/augmented/"
    num_augmented_samples = 9

    perform_augmentation(input_folder, num_augmented_samples)
