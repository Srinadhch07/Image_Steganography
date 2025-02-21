import cv2

def binary_to_text(binary_data):
    password=''
    text = ''
    for i in range(0,len(binary_data),8):
        char = chr(int(binary_data[i:i+8],2))
        if char == '\xFE':
            break
        password +=char

    for i in range(0, len(binary_data), 8):
        char = chr(int(binary_data[i:i+8], 2))
        if char == '\xFF':  # Stop Indicator
            break
        text += char
    text = text[len(password)+1:]
    return password,text


def extract_message(image_path,user_input):
    
    img = cv2.imread(image_path)
    binary_message = ''
    
    rows, cols, channels = img.shape
    for row in range(rows):
        for col in range(cols):
            for channel in range(channels):
                binary_message += str(img[row, col, channel] & 1)

    password,text=binary_to_text(binary_message)
    #user_input = input("Enter password :")
    if user_input == password:
        print("Decoded Message :",text)
    else:
        print("Wrong password")

if __name__ == "__main__":
    image_path = input("Enter Image Path :")
    password = input("Enter Password :")
    extract_message(image_path,password)