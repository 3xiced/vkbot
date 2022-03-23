from datetime import datetime, timedelta
from utils.constants_schedule import days, time, day_of_week


class Base():
    
    def schedule(self, start_cell, week_type, group, schedule, group_column, x, day_type):

        day_time_utc = datetime.weekday(datetime.today().utcnow() + timedelta(hours=3)) 

        if day_type == 'завтра':

            if day_time_utc == 6:
            # Обрабатываем исключение воскресенья для вывода, то есть автоматом понедельник в day
                day = start_cell
                day_time_utc = 0
            else:
                day_time_utc += 1
                day = int(day_time_utc) * x + start_cell

        else:
            day = int(day_time_utc) * x + start_cell
        
        schedule_output = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + group.upper() + '\n' \
            + 'День недели: ' + days[day_time_utc].capitalize() + '\n' + 'Неделя: ' + week_type.capitalize() + '\n' \
            + '⸻⸻⸻⸻⸻\n'  # Добавляем заголовок вывода, группа и тд.

        time_para = 1  # Номер пары для времени

        for para_cell in range(day, day + 10, 2):

            try:
                if schedule[group_column + str(para_cell)].value != None:

                    try:
                        schedule_output += str(time[time_para]) + '  ' \
                            + str(schedule[group_column + str(para_cell)].value) + '\n\n' \
                            + '⸻⸻⸻⸻⸻\n'  # Добавляем пару, то есть ячейку если она не пустая

                    except KeyError:
                        # Это обработка что ключ будет существовать во времени, то есть номер пары
                        return 'Ошибка в выводе расписания #1'
                else:
                    # Если же ячейка пустая, значит пары нет
                    schedule_output += 'Пары нет\n' + '⸻⸻⸻⸻⸻\n'
            except:
                # Обрабатываем ошибку в считывании таблицы
                return 'Ошибка в считывании таблицы #1'
            
            time_para += 1  # Счётчик пары плюс один
        
        return schedule_output


    def full_schedule(self, week_type, group, schedule, week_column, start_cell, end, step):

        subject = 1
        full_schedule_tuple = ()
        full_schedule_list = []
        # Формируем список и кортеж для будущего возврата в другой файл, чтобы вернуть пользователю

        full_schedule_list.append('⸻⸻⸻⸻⸻\n' + 'Группа: ' + group.upper() + '\n'
                                  + 'Неделя: ' + (week_type.capitalize()) + '\n'
                                  + '⸻⸻⸻⸻⸻\n')  # Добавляем заголовок вывода расписания с группой и тд.

        for day_of_week_cell in range(start_cell, end, step):

            # Добавление в конечный вывод дня недели то есть значения ячейки из таблицы
            full_schedule = str(day_of_week[str(subject)]) + '\n\n'

            for para_cell in range(day_of_week_cell, day_of_week_cell + 10, 2):

                if schedule[week_column + str(para_cell)].value != None:

                    full_schedule += str(schedule[week_column + str(para_cell)].value) + '\n'\
                        + '⸻⸻⸻⸻⸻\n'
                    # Если ячейка не пустая добавляем значение ячейки в конечный вывод

                else:
                    full_schedule += 'Пары нет\n' + '⸻⸻⸻⸻⸻\n'
                    # Если же пустая, то пары нет

            # Добавляем полученный день в список
            full_schedule_list.append(full_schedule)
            subject += 1

        # Из списка делаем кортеж и возвращаем
        full_schedule_tuple = tuple(full_schedule_list)

        return full_schedule_tuple