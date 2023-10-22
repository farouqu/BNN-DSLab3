import os
import pandas as pd

def create_dataframe(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)

    # Filter out non-image files if needed
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Create a Pandas DataFrame
    df = pd.DataFrame({'ImagePath': image_files})

    return df

if __name__ == "__main__":
    folder_path = "../../datasets/Finnish_dataset/png/"

    # Create the DataFrame
    image_df = create_dataframe(folder_path)

    # Display the DataFrame (optional)
    print(image_df)

    # Save the DataFrame to a CSV file
    image_df.to_csv("../../datasets/Finnish_dataset/annotations.csv", index=False)
