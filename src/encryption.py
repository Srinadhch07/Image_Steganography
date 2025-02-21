
import cv2

# Encryption methods
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def hide_message(image_path, message,password, output_path="EncryptedImage.png"):
    img = cv2.imread(image_path)
    binary_message = text_to_binary(message) + '11111111'  # Stop indicator for message
    binary_password = text_to_binary(password) + '11111110' # Stope indicator for password
    
    full_binary = binary_password + binary_message

    data_index = 0
    message_length = len(full_binary)
    rows, cols, channels = img.shape

    for row in range(rows):
        for col in range(cols):
            for channel in range(channels):
                if data_index < message_length:
                    pixel_value = img[row, col, channel]
                    pixel_value = (pixel_value & ~1) | int(full_binary[data_index])
                    img[row, col, channel] = pixel_value
                    data_index += 1
                else:
                    cv2.imwrite(output_path, img)
                    print("Image Generation Successful")
                    return
                
if __name__ == "__main__":
    image_path = input("Enter image path :")
    message = input("Write message :")
    password = input("Set Password :")
    hide_message(image_path, message,password)
