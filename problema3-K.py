time = input().strip()

h, m = map(int, time.split(":"))

hour_angle = (h % 12) * 30 + m * 0.5
minute_angle = m * 6

print(hour_angle, minute_angle)