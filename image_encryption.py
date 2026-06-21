from PIL import Image

def process_image(image_path, output_path, key):
    try:
        # Open the image
        img = Image.open(image_path)
        pixels = img.load() # Load pixel data into memory
        
        width, height = img.size
        
        # Iterate through every single pixel
        for x in range(width):
            for y in range(height):
                pixel = pixels[x, y]
                
                # Check if image is RGB or RGBA (handles transparency if present)
                if len(pixel) == 3:
                    r, g, b = pixel
                    # Apply XOR mathematical operation to each RGB value using the key
                    pixels[x, y] = (r ^ key, g ^ key, b ^ key)
                elif len(pixel) == 4:
                    r, g, b, a = pixel
                    # Leave the Alpha (transparency) channel untouched so image structure stays valid
                    pixels[x, y] = (r ^ key, g ^ key, b ^ key, a)
                    
        # Save the manipulated image
        img.save(output_path)
        print(f"Success! Image processed and saved to: {output_path}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("--- Prodigy Infotech: Pixel Manipulation Tool ---")
    
    choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").strip().upper()
    if choice not in ['E', 'D']:
        print("Invalid choice! Exiting.")
        return
        
    img_path = input("Enter the path to your source image (e.g., input.jpg): ").strip()
    out_path = input("Enter the path for the output image (e.g., output.png): ").strip()
    
    try:
        key = int(input("Enter a secret encryption key (integer 1-255): "))
        if not (1 <= key <= 255):
            print("Please keep the key between 1 and 255.")
            return
    except ValueError:
        print("Invalid key! Must be an integer.")
        return
        
    print("Processing image... Please wait...")
    process_image(img_path, out_path, key)

if __name__ == "__main__":
    main()