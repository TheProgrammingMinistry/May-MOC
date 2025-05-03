Sure! Here's a customized `README.md` for the exact code you provided:

---

````markdown
# 🖼️ Basic Image Processing with OpenCV

This project demonstrates **basic image processing techniques** using the OpenCV library in Python. It covers reading an image, converting it to grayscale, resizing it, and displaying all variations in separate windows.

---

## 📌 What the Script Does

1. Loads an image from the local directory.
2. Converts the image to **grayscale**.
3. Resizes the grayscale image to **50x50 pixels**.
4. Displays:
   - The original image
   - The grayscale image
   - The resized grayscale image

---

## 💻 Code Used

```python
import cv2 as cv

image = cv.imread("May/retaurant 6.jpg")
gray_scale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

resize = cv.resize(gray_scale, (50, 50), interpolation=cv.INTER_AREA)

cv.imshow("resize image", resize)
cv.imshow("Normal image", image)
cv.imshow("Gray image", gray_scale)

cv.waitKey(0)
````

---

## 🧠 Explanation of Each Step

* `cv.imread(...)`: Loads an image from a specified file path.
* `cv.cvtColor(..., cv.COLOR_BGR2GRAY)`: Converts the color image to grayscale.
* `cv.resize(..., (50, 50), interpolation=cv.INTER_AREA)`: Shrinks the grayscale image to 50x50 pixels using area-based interpolation (good for reducing size).
* `cv.imshow(...)`: Displays the images in separate windows.
* `cv.waitKey(0)`: Keeps the display open until a key is pressed.

---

## 📁 Project Structure

```
.
├── May/
│   └── retaurant 6.jpg
├── image_processing.py
└── README.md
```

---

## 🛠️ Requirements

* Python 3.x
* OpenCV

Install OpenCV via pip:

```bash
pip install opencv-python
```

---

## 🚀 How to Run

1. Clone or download the repo.
2. Make sure the image path is correct.
3. Run the script:

   ```bash
   python image_processing.py
   ```

---

## 📌 Notes

* Ensure that `"May/retaurant 6.jpg"` exists, and the path is correct.
* You can use a different image by changing the file path in the script.

---

## 📜 License

This project is for educational purposes only.
