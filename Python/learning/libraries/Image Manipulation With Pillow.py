# -------------------------------------------------
# -- Practical => Image Manipulation With Pillow --
# -------------------------------------------------
# Pillow is a fork of PIL (Python Imaging Library) and is used for opening, manipulating, and saving many different image file formats.
# Pillow is a powerful library for image processing in Python.
# you can do alot of things with it like:
# 1. Open and display images
# 2. Resize and crop images
# 3. Rotate and flip images
# 4. Apply filters and effects
# 5. Convert between different image formats
# 6. Draw shapes and text on images
# 7. Create thumbnails
# 8. Save images in different formats
# 9. Work with image metadata
# 10. Create animated GIFs
# 11. Perform image analysis and manipulation
# 12. Create image montages
# 13. Create image collages
# 14. Create image mosaics
# 15. Create image slideshows
# 16. Create image galleries
# 17. Create image maps and alot of things
# the url of the pillow library is: https://pillow.readthedocs.io/en/stable/ you can find all the information you need in this url
# to install pillow in linux use the command: sudo apt-get install python3-pil
# to install pillow in windows use the command: pip install pillow
from PIL import Image

# Open The Image
myImage = Image.open("/home/omersalem/Documents/VsCode Projects/Python/learning/libraries/mountain.jpg") # Open The Image

# Show The Image
myImage.show() # Show The Image 

# My Cropped Image
myBox = (300, 300, 800, 800) # Define The Box (Left, Top, Right, Bottom)
myNewImage = myImage.crop(myBox) # Crop The Image by cropping the image to the box we defined

# Show The New Image
myNewImage.show() #

# My Converted Mode Image
myConverted = myImage.convert("L")  # Convert To Grayscale
myConverted.show()

print('' * 50)

from PIL import Image, ImageDraw, ImageFont  # استيراد الأدوات اللازمة للكتابة على الصور

image = Image.open("/home/omersalem/Documents/VsCode Projects/Python/learning/libraries/mountain.jpg")  # فتح الصورة الأصلية

draw = ImageDraw.Draw(image)  # إنشاء كائن يسمح بالرسم أو الكتابة على الصورة

#font = ImageFont.load_default()  # تحميل خط افتراضي (يمكن تغييره لاحقاً)
font = ImageFont.truetype("/home/omersalem/Documents/VsCode Projects/Python/learning/libraries/Marhey.ttf", size=50) # تحميل خط مخصص (يجب أن يكون الخط موجودًا في المسار المحدد)

draw.text((100, 100), "Hello, Pillow!", font=font, fill="black")  # كتابة نص في إحداثيات (10, 10) باللون الأبيض

image.show()  # عرض الصورة بعد الكتابة عليها

image.save("text_added.jpg")  # حفظ الصورة المعدلة باسم جديد

#and we have alot of options to do with the images

#you can go to this link of chatgpt and see all the options https://chatgpt.com/share/6819d2f0-6b30-8009-b269-cc2c298a0811
