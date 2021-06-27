def tandem_bicyle(red_shirt_speeds, blue_shirt_speeds, fastest):
    red_shirt_speeds.sort()
    blue_shirt_speeds.sort(reverse=fastest)

    rs_speed = 0
    for red, blue in zip(red_shirt_speeds, blue_shirt_speeds):
        speed = max(red, blue)
        rs_speed += speed
    return rs_speed


if __name__ == '__main__':
    red_shirt_speeds = [5, 5, 3, 9, 2]
    blue_shirt_speeds = [3, 6, 7, 2, 1]
    fastest = True
    expected = 32

    print(f"Actual result: {tandem_bicyle(red_shirt_speeds, blue_shirt_speeds, fastest)}. Expected: {expected}")