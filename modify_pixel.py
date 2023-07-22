from pixel_colors import pixel_colors
from utils import modify_pixel_art, generate_pixel_art_image

if __name__ == "__main__":
    json_file_path = "json/example_pixel_art.json"
    modified_json_file_path = "json/modified_pixel_art.json"
    output_image_path = "output/modified_pixel_art_output.png"

    # # Define the modifications you want to make to the pixel values
    # pixel_modifications = {
    #     3: 2,  # Modify pixel value 1 to 2 (replace black with red in this example)
    #     # Add more modifications as needed
    # }

    # Get use r input for pixel modifications
    pixel_modifications = {}
    while True:
        try:
            pixel_value = int(input("Enter the pixel value to modify (integer from 0 to 255), or -1 to finish: "))
            if pixel_value == -1:
                break

            new_pixel_value = int(input("Enter the new pixel value (integer from 0 to 255): "))
            pixel_modifications[pixel_value] = new_pixel_value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Apply modifications and save to new JSON file
    modify_pixel_art(json_file_path, modified_json_file_path, pixel_modifications)

    # Generate the modified pixel art image
    generate_pixel_art_image(modified_json_file_path, output_image_path, pixel_colors)
