import student as st
import room_def as rm


def option():
    print("\n Мониторинг студентов")
    ch = int(input('Выбор действия: \n \
    1: Поиск ID студента по фамилии \n \
    2: Посмотреть локацию студент \n \
    3: Выход\n \
    Ваш выбор: '))

    if ch == 1:
        Surn = str(input("Введите фамилию: "))
        if Surn in st.student['Фамилия']:
            index = st.student['Фамилия'].index(Surn)
        print(f"{st.student['ID'][index]}, {st.student['Имя'][index]},{st.student['Фамилия'][index]}\n,{st.student['Дата рождения'][index]}, {st.student['Средний бал'][index]}")
        print('\n Далее? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()

    elif ch == 2:
        c = input('Введите ID студента: ')
        if c in rm.room['ID']:
            index = rm.room['ID'].index(c)
            print(f" аудитория - {rm.room['Предмет'][index]}\n\, парта - {rm.room['Номер парты'][index]}, это {rm.room['Ряд'][index]}, парта - {rm.room['Вид парты'][index]}, Имя: {st.student['Имя'][index]}, Фамилия - {st.student['Фамилия'][index]}, и успеваемость студента: {st.student['Средний бал'][index]}")
            print('\nХотите выполнить другую операцию??? Y или N: ')
            num = input()
            if num == 'Y' or 'y' or 'У' or 'у':
                option()
            exit()
    else:
        print('еще раз')
    exit()


option()
