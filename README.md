Image Bars Case Study

📌 Overview

This project is a case study focused on visualizing data using color bars in an image. It is developed using Python and demonstrates how numerical values can be converted into graphical representations.

The program generates a series of vertical color bars, where each bar represents a value through variations in color intensity.

---

🎯 Objectives

- To understand image manipulation using Python
- To visualize numerical data as color bars
- To apply pixel-level operations for graphical representation
- To explore how data can be encoded visually

---

⚙️ Features

- Creates a blank image canvas
- Converts numerical values into colored bars
- Each bar represents a value using RGB color mapping
- Dynamic calculation of bar width based on input size
- Displays the generated image output

---

🛠️ Technologies Used

- Python
- Pillow (PIL)
- Custom "SimpleImage" class for image handling

---

🧠 Concepts Applied

- Image processing fundamentals
- Pixel manipulation (RGB values)
- Data visualization
- Iteration over image pixels
- Mapping numerical values to color intensity

---

📂 Project Structure

Image_Bars_Case_Study/
│
├── simpleimage.py      # Image handling library
├── visualize.py        # Main program for generating color bars
├── README.md

---

▶️ How It Works

- A blank image canvas is created
- A list of values (0.0 to 1.0) is defined
- Each value is converted into a red color intensity
- The canvas is divided into equal vertical sections
- Each section is filled with a color corresponding to the value

---

▶️ How to Run

1. Install required library:

pip install pillow

2. Run the program:

python visualize.py

---

📷 Output

The program generates an image with vertical color bars.
Each bar visually represents a value using variations in red intensity combined with constant green and blue values.

---

📚 Example Logic

- Value "1.0" → Bright red color
- Value "0.5" → Medium red
- Value "0.0" → Minimal red

This creates a gradient-like bar visualization.

---

📚 Conclusion

This project demonstrates how numerical data can be transformed into visual patterns using image processing techniques. It highlights the importance of data visualization and pixel-level manipulation in Python.

---

👨‍🏫 Acknowledgement

This case study was developed based on concepts and guidance provided during classroom sessions by the instructor.
