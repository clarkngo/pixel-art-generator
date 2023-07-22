from pixel_colors import pixel_colors
from utils import generate_pixel_art_image

if __name__ == "__main__":
    json_file_path = "json/example_pixel_art.json"
    output_image_path = "output/pixel_art_output.png"

    generate_pixel_art_image(json_file_path, output_image_path, pixel_colors)
