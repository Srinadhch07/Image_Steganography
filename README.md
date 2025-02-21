# Secure Data Hiding in Images Using Steganography

## Overview
This project implements **LSB-based steganography** to securely embed sensitive data within images while maintaining visual integrity. It provides a lightweight, efficient, and secure solution for **data confidentiality**, making it ideal for cybersecurity, forensics, and private communication.

## Features
- **Least Significant Bit (LSB) Encoding:** Hides data without noticeable visual changes.
- **Command-Line Interface (CLI):** Lightweight and easy to integrate.
- **High Performance:** Developed in Python for efficiency and speed.
- **Multi-Format Support:** Works with various image types with planned extensions.

## Technologies Used
- **Operating System:** Windows 11  
- **Development Environment:** Visual Studio  
- **Programming Language:** Python  

## Installation & Usage
### Prerequisites
- Python 3.x installed
- Required dependencies (`pip install -r requirements.txt`)

### Running the Application
#### **Encoding Data:**
```bash
python steganography.py --hide --image input.jpg --output encoded.png --data secret.txt
```
#### **Decoding Data:**
```bash
python steganography.py --extract --image encoded.png --output extracted.txt
```

## Target Users
- **Cybersecurity Professionals** – Secure communication.
- **Forensic Experts** – Data retrieval in digital investigations.
- **Government Agencies** – Secure intelligence operations.
- **Privacy Advocates** – Protecting confidential information.

## Future Enhancements
- **Graphical User Interface (GUI)** for improved accessibility.
- **Two-Factor Authentication** for enhanced security.
- **Data Compression** for faster decryption.
- **Custom Encryption Methods** for greater flexibility.

## Repository Contents
📂 **Source Code** – Python scripts for encryption and decryption  
📂 **Sample Data** – Includes original and encoded images  
📂 **Documentation** – Project reports and presentations  

## Contributing
Contributions are welcome! Feel free to fork the repository, submit issues, or open pull requests.

## License
This project is licensed under the **MIT License**.

## Contact
For any queries, reach out via **[GitHub Issues](https://github.com/Srinadhch07/Image_Steganography/issues)**.
