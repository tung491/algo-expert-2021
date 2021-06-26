def class_photos(red_shirt_heights, blue_shirt_heights):
    red_shirt_heights.sort()
    blue_shirt_heights.sort()

    red_sitting_back, blue_sitting_back = True, True

    for red, blue in zip(red_shirt_heights, blue_shirt_heights):
        red_sitting_back = red_sitting_back and (red > blue)
        blue_sitting_back = blue_sitting_back and (blue > red)
    return red_sitting_back or blue_sitting_back


if __name__ == '__main__':
    red_shirt_heights = [5, 8, 1, 3, 4]
    blue_shirt_heights = [6, 9, 2, 4, 5]
    expected = True

    print(f"Actual result: {class_photos(red_shirt_heights, blue_shirt_heights)}. Expected: {expected}")