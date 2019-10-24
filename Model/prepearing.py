# импортируем все из get_records и selection
from get_records import *
from selection import *


# Функция, которая создаёт два списка(positive_id, negative_id), в которых соответственно хранятся положительные
# и отрицательные ключи(id абонентов) от records
def get_sort_id(records):
    positive_id = []
    non_positive_id = []
    for key in records:
        user_list = records[key]
        tariff_id_list = []
        for ul in user_list:
            tariff_id_list.append(ul.tariff_id)
        length = len(tariff_id_list)
        tariff_id_list = set(tariff_id_list)
        if length > 2:
            if len(tariff_id_list) > 1:
                positive_id.append(key)
            else:
                non_positive_id.append(key)
    negative_id = select_random(non_positive_id)
    return positive_id, negative_id


# Функция, которая оздаёт список со всеми данными пользователя
def get_training_list(rec, user_id):
    user = rec[user_id]
    user_rec = []
    for u in range(len(user) - 1):
        # user_rec.append(fild_calc(user[u + 1].charge, user[u].charge))
        user_rec.append(fild_calc(user[u + 1].support_4G, user[u].support_4G))
        # user_rec.append(fild_calc(user[u + 1].support_3G, user[u].support_3G))
        # user_rec.append(fild_calc(user[u + 1].LTE_traffic_flag, user[u].LTE_traffic_flag))
        # user_rec.append(fild_calc(user[u + 1].SMS_in_CNT, user[u].SMS_in_CNT))
        # user_rec.append(fild_calc(user[u + 1].SMS_out_CNT, user[u].SMS_out_CNT))
        user_rec.append(fild_calc(user[u + 1].calls_in_CNT, user[u].calls_in_CNT))
        user_rec.append(fild_calc(user[u + 1].calls_out_CNT, user[u].calls_out_CNT))
        # user_rec.append(fild_calc(user[u + 1].life_time, user[u].life_time))
        # user_rec.append(fild_calc(user[u + 1].duration_in_min, user[u].duration_in_min))
        user_rec.append(fild_calc(user[u + 1].duration_out_min, user[u].duration_out_min))
        user_rec.append(fild_calc(user[u + 1].data_traffic_MB, user[u].data_traffic_MB))
        # user_rec.append(fild_calc(user[u + 1].sessions_CNT, user[u].sessions_CNT))
        # user_rec.append(fild_calc(user[u + 1].recharge, user[u].recharge))
        # user_rec.append(fild_calc(user[u + 1].recharge_CNT, user[u].recharge_CNT))
    return user_rec


# Функция, которая предварительно собирает данные для обучения нейронной сети
def prepearing(puth):
    records = get_records(puth)
    positive_id, negative_id = get_sort_id(records)
    training_dict = {}
    x = []
    y = []
    count = min(len(positive_id), len(negative_id))
    for iter in range(count):
        training_dict[positive_id[iter]] = 1
        training_dict[negative_id[iter]] = 0
    for rtd in training_dict:
        x.append(get_training_list(records, rtd))
        y.append(training_dict[rtd])
    return x, y


# Функция, вызываемая из get_training_list, она сравнивает значения за текущий и следующий период
def fild_calc(a, b):
    if a > b:
        return 1
    else:
        return 0
