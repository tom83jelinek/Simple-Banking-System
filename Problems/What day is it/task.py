days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
        5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

reference_time = '10:30'
reference_day = 2

offset = int(input())

reference_time_nums = reference_time.split(':')
calculated_time = int(reference_time_nums[0]) + offset

if calculated_time > 23:
    print(days[reference_day + 1])
elif calculated_time < 0:
    print(days[reference_day - 1])
else:
    print(days[reference_day])
