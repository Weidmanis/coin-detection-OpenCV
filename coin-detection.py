import cv2
import numpy as np
import copy

def radius(circles):
    """Extract the values of radius for the coins"""
    radius = []
    for i in circles[0,:]:
        radius.append(i[2])
    return radius


# Read the given image
img = cv2.imread('capstone_coins.png', cv2.IMREAD_COLOR) 

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# Blur using blur kernel, the tuple needs a pair of odd numbers
gray_blurred = cv2.blur(gray, (7,7))

# Apply Hough transform on the blurred image
# Returns an array with x-coor, y-coor, radius
# Need to adjust the parameters
detected_circles = cv2.HoughCircles(gray_blurred,  
                   cv2.HOUGH_GRADIENT, 2, 150, param1 = 37, 
                   param2 = 95, minRadius = 65, maxRadius = 130)

# Make a list of radiuses
radius = radius(detected_circles)
det_circ = detected_circles.tolist()

# Draw circles that are detected. 
# First check if there are any circles found
if detected_circles is not None: 
    
    # Convert the circle parameters a, b and r to integers. 
    detected_circles = np.uint16(np.around(detected_circles)) 
    for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2] 

        # Draw the circumference of the circle. (Green Circle)
        cv2.circle(img, (a, b), r, (0, 255, 0), 2) 

        # Draw a small circle (of radius 1) to show the center. (Red Circle)
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)


# Set value = 0, to add up the amount for the coins
value = 0

# Loop through radius values to detect the value of the coin
# Find the value and print it on the coin 
for i in range(0, len(radius)): 

    if radius[i] > 88 and radius[i] <= 90:
        # 5p coin
        value += 5
        cv2.putText(img, "5p", 
                    (int(det_circ[0][i][0]) + 5, int(det_circ[0][i][1]) +5),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    elif radius[i] > 101 and radius[i] <= 108:
        # 1p coin
        value += 1
        cv2.putText(img, "1p",
                    (int(det_circ[0][i][0]) +5, int(det_circ[0][i][1]) +5),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    elif radius[i] > 116 and radius[i] <= 119:
        # 10p coin
        value += 10
        cv2.putText(img, "10p",
                    (int(det_circ[0][i][0]) +5, int(det_circ[0][i][1]) +5),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    elif radius[i] > 125 and radius[i] <= 130:
        # 2p coin
        value += 2
        cv2.putText(img, "2p",
                    (int(det_circ[0][i][0]) +5, int(det_circ[0][i][1]) +5),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

# Add total value of the coins in the top corner of the image
cv2.putText(img, f'Total amount of the coins in the image is: {value}',(50, 50), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

# Show the image at the end
cv2.imwrite("Capstone_project_fin.png", img)
cv2.imshow('Coins', img)
cv2.waitKey(0)