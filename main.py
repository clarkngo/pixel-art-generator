from PIL import Image
import json

def lookup_pixel_color(pixel_value, pixel_colors):
    """
    Lookup method to get the corresponding color for a pixel value.
    If the pixel value is not found in the dictionary, it returns the default color.
    """
    return pixel_colors.get(pixel_value, (255, 255, 255))  # Default color: White (RGB: 255, 255, 255)

def generate_pixel_art_image(json_file, output_image_path, pixel_colors):
    with open(json_file, 'r') as file:
        data = json.load(file)

    if "width" not in data or "height" not in data or "pixels" not in data:
        raise ValueError("Invalid JSON format. Make sure 'width', 'height', and 'pixels' are present.")

    width = data["width"]
    height = data["height"]
    pixels = data["pixels"]

    if len(pixels) != height or any(len(row) != width for row in pixels):
        raise ValueError(f"Pixel data does not match specified width ({width}) and height ({height}).")

    pixel_size = 10  # Adjust this value to set the size of each pixel in the output image
    image_width = width * pixel_size
    image_height = height * pixel_size

    image = Image.new("RGB", (image_width, image_height), color=(255, 255, 255))  # White background

    for y in range(height):
        for x in range(width):
            pixel_value = pixels[y][x]
            pixel_color = lookup_pixel_color(pixel_value, pixel_colors)

            x_start = x * pixel_size
            y_start = y * pixel_size
            x_end = x_start + pixel_size
            y_end = y_start + pixel_size

            for i in range(x_start, x_end):
                for j in range(y_start, y_end):
                    image.putpixel((i, j), pixel_color)

    image.save(output_image_path)
    print(f"Image saved to {output_image_path}")

if __name__ == "__main__":
    json_file_path = "example_pixel_art.json"
    output_image_path = "pixel_art_output.png"

    # Define the pixel_colors dictionary mapping pixel values to RGB colors
    # Add or modify entries here as needed
    pixel_colors = {
        0: (255, 255, 255),  # White
        1: (0, 0, 0),        # Black
        2: (255, 0, 0),      # Red
        3: (0, 255, 0),      # Green
        4: (0, 0, 255),      # Blue
        5: (255, 255, 0),    # Yellow
        6: (255, 0, 255),    # Magenta
        7: (0, 255, 255),    # Cyan
        8: (255, 165, 0),    # Orange
        9: (165, 42, 42),    # Brown
        10: (245, 204, 176),  # Flesh
        # Add more colors and pixel values here if desired
    }

    generate_pixel_art_image(json_file_path, output_image_path, pixel_colors)
