# ДЗ 6.2. Конвертер із числа в дату

seconds = int(input("Введіть кількість секунд (0..8639999): "))

if not (0 <= seconds < 8640000):
    print("Помилка: число має бути >= 0 і < 8640000")
else:
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 60 * 60
    SECONDS_IN_DAY = 24 * 60 * 60

    days = seconds // SECONDS_IN_DAY
    seconds %= SECONDS_IN_DAY

    hours = seconds // SECONDS_IN_HOUR
    seconds %= SECONDS_IN_HOUR

    minutes = seconds // SECONDS_IN_MINUTE
    seconds %= SECONDS_IN_MINUTE

    # склонение "день"
    last_two = days % 100
    last_one = days % 10

    if 11 <= last_two <= 14:
        day_word = "днів"
    elif last_one == 1:
        day_word = "день"
    elif last_one in (2, 3, 4):
        day_word = "дні"
    else:
        day_word = "днів"
        
    print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
