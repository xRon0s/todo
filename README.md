# Color Checker

カラーチェッカーは**Pyside6**を用いたGUIアプリケーションで、画像からのHEX,RGB値の取得機能とHEX値を用いた4つの色の比較機能という2つの機能を持っています。

## Features

- **Image Upload**: Load an image from your system to interact with.
- **Color Picker**: Click on the image to pick a color and get its RGB and HEX values.
- **Color Comparison**: Compare the selected color with other color codes entered manually.
- **User-friendly Interface**: Built with PySide6 for a modern, easy-to-use interface.

## Requirements

This project uses the following Python packages:

- PySide6==6.8.1.1
- numpy==2.2.0
- pillow==11.0.0
- python-dateutil==2.9.0.post0
- pyttsx3==2.98
- pywin32==308
- pywinpty==2.0.14
- PyYAML==6.0.2
- webcolors==24.11.1

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/color-checker.git
    cd color-checker
    ```

2. **Set up a virtual environment**:

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - For Windows:
      ```bash
      venv\Scripts\activate
      ```
    - For macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application**:

    ```bash
    python main.py
    ```

2. **Load an Image**:
   - Click on the "Load Image" button to select an image from your computer.

3. **Pick a Color**:
   - Click on any area of the image to select a color.
   - The RGB and HEX values of the selected color will be displayed.

4. **Compare Colors**:
   - Enter up to 4 HEX color codes in the provided fields.
   - Click "Compare Colors" to see which entered color matches the selected color.