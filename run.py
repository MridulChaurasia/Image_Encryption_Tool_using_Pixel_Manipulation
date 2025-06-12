from PIL import Image
import os

def encrypt_decrypt_image(image_path, key, mode='encrypt'):
    try:
        img = Image.open(image_path)
        img = img.convert('RGB')
        pixels = img.load()

        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                r_new = r ^ key
                g_new = g ^ key
                b_new = b ^ key

                pixels[x, y] = (r_new, g_new, b_new)

        filename = os.path.basename(image_path)
        name, ext = os.path.splitext(filename)
        new_name = f"{name}_{mode}ed{ext}"
        img.save(new_name)

        print(f"\nImage successfully {mode}ed and saved as: {new_name}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    print("=== Image Encryption Tool ===")
    path = input("Enter path to the image file: ").strip()
    try:
        key = int(input("Enter numeric key (0-255): "))
        if not (0 <= key <= 255):
            raise ValueError("Key must be between 0 and 255.")
    except ValueError as e:
        print(f"Invalid key: {e}")
        return

    mode = input("Type 'encrypt' or 'decrypt': ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode.")
        return

    encrypt_decrypt_image(path, key, mode)

if __name__ == "__main__":
    main()
