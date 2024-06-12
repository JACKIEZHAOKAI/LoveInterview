

# Given a closed, non-intersecting shape boundary, how would you determine whether a user clicked inside or outside of the shape?
# Given - bool isPixelActive(x,y) - returns true if the pixel at x,y is on (black) and false otherwise.

# isTouchInsideShape(x,y) - where x,y is the central touchpoint from the user.  
# This is a boolean to return true if the user touches inside the shape, false otherwise.

# Mocked function to represent a simple rectangular shape
def isPixelActive(x, y):
    # Define a rectangle for simplicity
    # This rectangle is active from (10, 10) to (30, 20)
    if 10 <= x <= 30 and 10 <= y <= 20:
        return True
    return False

def isTouchInsideShape(x, y, maxX, maxY):
    """
    Determine if the touch point (x, y) is inside the shape.
    Assumes isPixelActive(x, y) is available to determine if a pixel is part of the shape.
    maxX and maxY define the boundaries of the pixel data to avoid infinite loops.
    """
    
    inside = False
    # Scan to the right
    for testX in range(x, maxX + 1):
        if isPixelActive(testX, y):
            inside = not inside
        # Break if we reach an inactive pixel after finding an active one
        elif inside:
            break

    return inside

# Define the maximum bounds of the pixel data
maxX, maxY = 40, 30

# Test cases
test_points = [(5, 15), (15, 15), (35, 15), (15, 25)]
results = {point: isTouchInsideShape(point[0], point[1], maxX, maxY) for point in test_points}

for point, result in results.items():
    status = "inside" if result else "outside"
    print(f"Point {point} is {status} the shape.")
