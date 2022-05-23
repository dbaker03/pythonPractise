#Case switching

weekday_int = 6

match weekday_int:
    case 0:
        weekday = 'Monday'
    case 1:
        weekday = 'Tuesday'
    case 2:
        weekday = 'Wednesday'
    case 3:
        weekday = 'Thursday'
    case 4:
        weekday = 'Friday'
    case 5:
        weekday = 'Saturday'
    case 6:
        weekday = 'Sunday'
    case _:
        weekday = 'invalid input'

print(weekday)

#better solution to just looking up values
WEEKDAY_INT_DICT = {
    0: 'Monday',
    1: 'Tuesday'
}