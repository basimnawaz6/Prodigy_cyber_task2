from PIL import Image
import numpy as np

# Function to encrypt an image
def encrypt_image(image, swap_pixels):
    if swap_pixels:
        # Swap pixel values (example: swapping red and blue channels)
        image_array = np.array(image)
        image_array[:, :, [0, 2]] = image_array[:, :, [2, 0]]
        return Image.fromarray(image_array)
    else:
        # Apply a basic mathematical operation to each pixel (example: invert colors)
        return Image.eval(image, lambda x: 255 - x)

# Function to decrypt an image (same as encryption)
def decrypt_image(image, swap_pixels):
    return encrypt_image(image, swap_pixels)

def main():
    while True:
        # Load the image
        input_image_path = input("Enter the path of the image file: ")
        if input_image_path.lower() == 'exit':
            print("Terminating program.")
            return

        try:
            image = Image.open(input_image_path)
        except FileNotFoundError:
            print("Error: Unable to load image.")
            continue

        while True:
            # Ask the user whether to encrypt or decrypt
            print("\nChoose operation:")
            print("1. Encrypt")
            print("2. Decrypt")
            print("3. Terminate")
            choice = input("Enter your choice (1, 2, or 3): ")

            if choice == '1':
                # Ask the user whether to swap pixels or apply a basic mathematical operation for encryption
                print("\nChoose encryption method:")
                print("1. Swap pixels")
                print("2. Apply a basic mathematical operation")
                encryption_choice = input("Enter your choice (1 or 2): ")

                if encryption_choice not in ['1', '2']:
                    print("Invalid choice. Please enter 1 or 2.")
                    continue

                swap_pixels = (encryption_choice == '1')

                # Encrypt the image
                processed_image = encrypt_image(image.copy(), swap_pixels)
                output_image_path = "encrypted_image.jpg"
                print("Image encrypted successfully.")
                break

            elif choice == '2':
                # Ask the user whether to swap pixels or apply a basic mathematical operation for decryption
                print("\nChoose decryption method:")
                print("1. Swap pixels")
                print("2. Apply a basic mathematical operation")
                decryption_choice = input("Enter your choice (1 or 2): ")

                if decryption_choice not in ['1', '2']:
                    print("Invalid choice. Please enter 1 or 2.")
                    continue

                swap_pixels = (decryption_choice == '1')

                # Decrypt the image
                processed_image = decrypt_image(image.copy(), swap_pixels)
                output_image_path = "decrypted_image.jpg"
                print("Image decrypted successfully.")
                break

            elif choice == '3':
                print("\nTerminating program.")
                return

            else:
                print("\nInvalid choice. Please enter 1, 2, or 3.")

        # Save the result as a new image file
        processed_image.save(output_image_path)
        print("Image saved as", output_image_path)


if __name__ == "__main__":
    main()
