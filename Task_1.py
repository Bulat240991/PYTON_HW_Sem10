'''
Задача 44:
В ячейке ниже представлен код генерирующий DataFrame,
которая состоит всего из 1 столбца. Ваша задача перевести
его в one hot вид.
Сможете ли вы это сделать без get_dummies?
'''

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})


# print(pd.get_dummies(data.head()))  - эта строка написана, чтоб посмотреть
#                                       как выглядит one hot вид

# функция создает one hot без использования get_dummies
def create_get_dummies(data):
    data['whoAmI_robot'] = 0
    data['whoAmI_human'] = 0
    for i in range(len(data)):
        if data.loc[i, 'whoAmI'] == 'robot':
            data.loc[i, 'whoAmI_robot'] = 1
        elif data.loc[i, 'whoAmI'] == 'human':
            data.loc[i, 'whoAmI_human'] = 1
    return data


new_data = create_get_dummies(data)
new_data = new_data.drop('whoAmI', axis=1)  # удаляем столбец 'whoAmI' для вывода аналогичного функции get_dummies
print(new_data.head())
