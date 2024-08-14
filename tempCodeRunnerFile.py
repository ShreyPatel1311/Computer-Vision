success = cv.imwrite("gray_image_2.jpg", gray)
if not success:
    print("Error: Could not save grayscale image!")