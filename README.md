# Spectroscopy

This project generates an intensity graph based on a provided light intensity image. The sample implementation uses the image file `cfl.png` as input.

## How It Works

The code processes an input image (e.g., `cfl.png`) to analyze its light intensity and generates a corresponding graph that visualizes the intensity distribution.

### Example Input
A sample image `cfl.png` is used to demonstrate how the code works. You can replace this image with your own light intensity images.

### Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ich4mp/Spectroscopy.git
    cd intensity
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the script**:
    Replace `cfl.png` with your own image file if necessary, or use the sample `cfl.png`.

    ```bash
    python intensity.py cfl.png
    ```

4. **Output**:
    The script will generate an intensity graph based on the image, which can be saved or visualized.

### Customization

You can replace the image file `cfl.png` with any image of your choice. Ensure that the image is properly formatted for intensity analysis (e.g., grayscale or color image).

### Example Output

The generated intensity graph will be saved to a file or displayed depending on how the code is set up. It will show the light intensity distribution of the provided image.

## Dependencies

- Python 3.x
- Required libraries (listed in `requirements.txt`)
