import pandas as pd



print('лечебный факультет, группа 308')

student = {
        'ID': ['1','2','3','4','5'],
        'Имя' : ['Анна','Юля','Маша','Владимир','Константин'],
        'Фамилия': ['Бондаренко','Хроменкова','Зурочка','Никитин','Гордеев'],
        'Дата рождения' : ['27.07.1987','01.03.1987','23.04.1987','22.09.1986','24.12.1986'],
        'Средний бал' : ['4,8','4,2','5,0','4,9','3,8']
}
    
sc = pd.DataFrame(data = student)

with open('students.csv', 'a', encoding='UTF-8') as cl:
        cl.write(f'{sc}')
        cl.write('\n')
    
print(sc)