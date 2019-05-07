#! python3
# -*- coding: cp1251 -*-
# renameDates.py - Переименовывает файлы, имена
# которых включают даты, указанные в
# американском формате (ММ-ДД-ГГГГ), приводя
# их в соответствие с европейским форматом
# дат (ДД-ММ-ГГГГ)


import shutil, os, re


# Созданеие регулярного выражения,
# которому соответствуют имена файлов,
# содержащие даты в американском формате.

datePattern = re.compile(r"""^(.*?) # весь текст перед датой
            ((0|1)?\d)-        # одна или две цифры месяца
            ((0|1|2|3)?\d)-    # одна или две цифры числа
            ((19|20)\d\d)      # четырк цифры года
            (.*?)$             # весь текст после даты
            """, re.VERBOSE)
# Организация цикла по файлам в рабочем
# каталоге
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # Пропуск файлов с именами, без дат
    if mo == None:
        continue
    # Получение отдельных частей имен файлов
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)



# TODO: Сформировать имена, соответствующие
# европейскому стилю

# TODO: Получить полные абсолютные пути к
# файлам

# TODO: Переименовать файлы.
