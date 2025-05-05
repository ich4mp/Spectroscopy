# 🌈 Spectroscopy (Image-Based Approximation)

This project generates a light intensity vs. wavelength graph from an image of a dispersed light spectrum (e.g., from a CFL bulb). The image is processed to extract grayscale intensity information column by column, and the result is plotted as a spectral intensity graph.

---

## ⚙️ How It Works

1. The input image (e.g., `cfl.png`) is read and converted to grayscale.
2. For each vertical column of pixels, the average intensity is computed.
3. These intensities are normalized relative to the brightest column.
4. The horizontal width of the image is linearly mapped to the visible wavelength range (400–800 nm).
5. The final output is a plot of **normalized intensity vs. wavelength**, approximating an emission spectrum.

---

## 📥 Example Input

A sample image `cfl.png` is included to demonstrate how the code works. This should be a photo of a visible light spectrum, such as a CFL bulb viewed through a diffraction grating or prism.

You can replace this image with your own, as long as it contains a horizontally dispersed light spectrum.

---

## ▶️ Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ich4mp/Spectroscopy.git
    cd Spectroscopy
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the script**:

    By default, the script processes the file `cfl.png`. You can replace this with your own image by updating the filename in the script.

    ```bash
    python intensity.py
    ```

    > 💡 You can modify the script to accept command-line arguments if you'd like dynamic image input.

4. **Output**:

    The script will display a graph of **normalized light intensity vs. wavelength (nm)**.

    Local intensity peaks (representing possible emission lines) will also be printed in the terminal output, like:

    ```
    Index :  120 Value :  0.83
    Index :  245 Value :  0.91
    ```

---

## 🛠️ Customization

- **Input Image**:  
  Replace `cfl.png` with any suitable image showing a dispersed light spectrum.

- **Wavelength Mapping**:  
  The default wavelength range is 400–800 nm mapped across the image width. You can change this range in the script if needed:

    ```python
    m = 400 / width
    wavelength = i * m + 400
    ```

- **Peak Detection**:  
  The script identifies local maxima in the normalized intensity to highlight key spectral lines.

---

## 📊 Example Output

A graph is displayed showing:

- **X-axis**: Wavelength (nm)
- **Y-axis**: Normalized light intensity

Optionally, you can save the graph or enhance it with peak labels and annotations.

---

## 📦 Dependencies

- Python 3.x
- OpenCV (`cv2`)
- Matplotlib

Install required libraries with:

```bash
pip install -r requirements.txt
