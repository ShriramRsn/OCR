import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd ="C:\\Users\\Asus\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

image = cv2.imread(r"N:\OCR\Image\SampleImage.png")
file_path = "N:\OCR\Output\myfile.txt"
text = pytesseract.image_to_string(image) 
with open(file_path, "w") as f:
    f.write(text)
f.close()
img_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

results = pytesseract.image_to_data(img_RGB)
for id, line in enumerate(results.splitlines()):

     if id != 0:
         line = line.split()
         if len(line) == 12:
             x, y, w, h = int(line[6]), int(line[7]), int(line[8]), int(line[9])
             cv2.rectangle(image, (x, y), (w+x, h+y), (0, 255, 0), 2)
             cv2.putText(image, line[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)

cv2.imshow("Input", image)
cv2.waitKey(0)