import qrcode
import matplotlib.pyplot as plt
import zlib

def generate_qr_code():
    # Prompt the user for input
    data = input("Enter the text or URL to generate a QR code: ")

    if not data.strip():
        print("No input provided. Please enter valid data.")
        return

    try:
        # Compress the data to fit into a QR code
        compressed_data = zlib.compress(data.encode('utf-8'))

        # Generate the QR code
        qr = qrcode.QRCode(
            version=None,  # Automatically determine the best version
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(compressed_data)
        qr.make(fit=True)

        # Create an image of the QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Visualize the QR code
        plt.figure(figsize=(6, 6))
        plt.imshow(img, cmap="gray")
        plt.axis("off")
        plt.title("Generated QR Code")
        plt.show()

    except Exception as e:
        print(f"Error generating QR code: {e}")

if __name__ == "__main__":
    generate_qr_code()