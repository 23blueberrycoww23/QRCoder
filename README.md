# QRCoder
# QR Code Generator

A Python script that generates QR codes from user input and visualizes them directly using Matplotlib.

## Features
- Accepts any text or URL as input.
- Automatically compresses data for longer inputs using zlib.
- Dynamically adjusts QR code size to fit the data.
- Visualizes the generated QR code without saving it to a file.

## Requirements
- Python 3.6+
- Required Python libraries:
  - `qrcode`
  - `matplotlib`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/qrcode-generator.git
   cd qrcode-generator
   ```

2. Install the dependencies:
   ```bash
   pip install qrcode[pil] matplotlib
   ```

## Usage

1. Run the script:
   ```bash
   python generate_qr_code.py
   ```

2. Enter the text or URL you want to generate a QR code for when prompted.

3. The generated QR code will be displayed in a Matplotlib window.

## Example

- Input:
  ```
  Enter the text or URL to generate a QR code: https://example.com
  ```

- Output:
  A QR code visualization opens in a new window.

## Limitations
- For extremely long inputs, the script compresses the data but may still fail if the data exceeds the QR code's maximum capacity.
- For such cases, consider splitting the data into smaller parts and generating multiple QR codes.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [qrcode library](https://pypi.org/project/qrcode/)
- [Matplotlib](https://matplotlib.org/)
