def average_speed(distance, hours):
    if hours == 0:
        return 'На ноль делить нельзя'
    else:
        return distance / hours


assert(average_speed(180, 3)) == 60
assert(average_speed(180, 0)) == 'На ноль делить нельзя'
assert(average_speed(100, 2)) == 50

words = ["лес", "парк", "площадь"]
print(sorted(words, key=lambda word: len(words)))