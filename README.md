# Image Encryption Tool

## Description
A simple Python tool that encrypts and decrypts images by manipulating pixel values. This tool demonstrates basic image-level cryptographic concepts by applying simple operations like pixel value shifting or XOR to obscure and recover image data.

This is meant for **educational use only**, to understand how basic image encryption can work at the pixel level using Python.

## Features
- Encrypts image files using pixel-based operations
- Decrypts encrypted images back to the original form
- Works with standard image formats (e.g., PNG, JPEG)
- Command-line interface for ease of use

## Usage

1. Install required dependencies:

```bash
pip install pillow
```

2. Run the script and follow prompts:

```bash
python3 Image_Encryption.py
```

Choose whether to encrypt or decrypt and provide the image path and key/operation value.

## Example Workflow
- Input image: `photo.png`
- Operation: Pixel value shifting or XOR with a given key
- Output: Encrypted image saved as `encrypted_photo.png`
- Decrypted using the same key to restore original

## Concepts Demonstrated
- Image processing with `PIL` (Python Imaging Library)
- Pixel-level manipulation
- Reversible encryption using mathematical operations
- File I/O and user input handling

## Requirements
- Python 3.x
- `pillow` library

## Disclaimer
This encryption method is not secure for production use. It is a basic demonstration of image encryption principles. For secure image encryption, use well-established cryptographic libraries and algorithms.
