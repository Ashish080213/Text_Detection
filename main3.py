import numpy as np
from PIL import Image

# Load image and convert to grayscale
img = Image.open('DEMO.png').convert('L')
img_data = np.array(img)

# Apply adaptive thresholding to obtain binary image
bin_data = np.zeros_like(img_data)
for i in range(1, img_data.shape[0] - 1):
    for j in range(1, img_data.shape[1] - 1):
        window = img_data[i-1:i+2, j-1:j+2]
        threshold = np.mean(window) - 2 * np.std(window)
        bin_data[i, j] = 255 if img_data[i, j] > threshold else 0

# Find contours in binary image
contours = []
for i in range(1, bin_data.shape[0] - 1):
    for j in range(1, bin_data.shape[1] - 1):
        if bin_data[i, j] == 255 and bin_data[i-1, j] == 0:
            contour = []
            curr_pos = (i, j)
            while bin_data[curr_pos] == 255:
                contour.append(curr_pos)
                bin_data[curr_pos] = 0
                if bin_data[curr_pos[0], curr_pos[1]+1] == 255:
                    curr_pos = (curr_pos[0], curr_pos[1]+1)
                elif bin_data[curr_pos[0]+1, curr_pos[1]] == 255:
                    curr_pos = (curr_pos[0]+1, curr_pos[1])
                elif bin_data[curr_pos[0], curr_pos[1]-1] == 255:
                    curr_pos = (curr_pos[0], curr_pos[1]-1)
                elif bin_data[curr_pos[0]-1, curr_pos[1]] == 255:
                    curr_pos = (curr_pos[0]-1, curr_pos[1])
            contours.append(np.array(contour))


# Get bounding box of each contour
bounding_boxes = []
for contour in contours:
    min_x = min([pt[1] for pt in contour])
    max_x = max([pt[1] for pt in contour])
    min_y = min([pt[0] for pt in contour])
    max_y = max([pt[0] for pt in contour])
    bounding_boxes.append((min_x, min_y, max_x - min_x + 1, max_y - min_y + 1))

# Draw bounding boxes on original image
img_data_rgb = np.stack([img_data]*3, axis=-1)
for bbox in bounding_boxes:
    x, y, w, h = bbox
    img_data_rgb[y:y+h, x:x+w, 1] = 0

# Display image with bounding boxes
Image.fromarray(img_data_rgb).show()