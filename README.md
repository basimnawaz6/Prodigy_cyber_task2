Pixel Manipulation for Image Encryption
This is image encryption and decryption tool using Python's PIL library. Here's how it works:

It defines two functions encrypt_image and decrypt_image to perform encryption and decryption operations on images, respectively. Encryption involves either swapping pixel values or applying a basic mathematical operation to each pixel.

The main function handles user input and controls the flow of the program. It continuously prompts the user to choose between encrypting or decrypting an image until the user chooses to terminate the program.

When encrypting or decrypting an image, the user can choose between two methods: swapping pixels or applying a basic mathematical operation. Depending on the user's choice, the script performs the selected operation on the image.

After processing the image, the script saves the result as a new image file with the appropriate extension ('.jpg' in this case).

Here's how you can use it:

Run the script.
Enter the path of the image file you want to encrypt or decrypt.
Choose whether to encrypt or decrypt the image.
Choose the encryption or decryption method.
The processed image will be saved in the current directory as either "encrypted_image.jpg" or "decrypted_image.jpg", depending on the operation performed.
