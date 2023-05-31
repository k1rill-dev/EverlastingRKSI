label second_day:
    th "Как же я не хочу вставать… Ну еще пять минуточек… "
    th "Ладно, через силу, через боль, встаем!"
    th "В такую погоду  не то, что на улицу, с кровати не хочется вставать!"
    th "Но делать нечего…"
    th "Хотя может…"
    th "Смутное чувство дежавю какое-то... Ну да ладно."

    if is_go_to_first_seminar:
        jump go_to_first_seminar_sec_day
    elif is_go_to_sec_seminar:
        jump go_to_sec_seminar_sec_day
    elif is_stay_home_homie:
        jump stay_home_sec_day


label go_to_first_seminar_sec_day:
    
    jump seven_eight_day

label go_to_sec_seminar_sec_day:

    jump seven_eight_day

label stay_home_sec_day:

    jump seven_eight_day


label seven_eight_day:

    return