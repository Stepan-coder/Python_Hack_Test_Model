# Импортируем всё из record_class
from record_class import *
# Библиотека для работы с csv
import pandas as pd


# Функция, которая читает построчно .csv(для целостности данных) и создаёт словарь, ключами в котором служать
# subs_id, а значением - список Record()'ов
def get_records(puth_to_csv_file):
    csv_file = pd.read_csv(puth_to_csv_file, delimiter=',')
    records = {}
    for c in range(len(csv_file)):
        rec = Record(csv_file.at[c, 'SUBS_ID'], csv_file.at[c, 'DATE_CALC'],
                     csv_file.at[c, 'TARIFF_ID'], csv_file.at[c, 'CHARGE'],
                     csv_file.at[c, 'SUPPORT_4G'], csv_file.at[c, 'SUPPORT_3G'],
                     csv_file.at[c, 'DATA_TRAFFIC_MB'], csv_file.at[c, 'SMS_IN_CNT'],
                     csv_file.at[c, 'SMS_OUT_CNT'], csv_file.at[c, 'CALLS_IN_CNT'],
                     csv_file.at[c, 'CALLS_OUT_CNT'], csv_file.at[c, 'LIFE_TIME'],
                     csv_file.at[c, 'DURATION_IN_MIN'], csv_file.at[c, 'DURATION_OUT_MIN'],
                     csv_file.at[c, 'DATA_TRAFFIC_MB'], csv_file.at[c, 'SESSIONS_CNT'],
                     csv_file.at[c, 'RECHARGE'], csv_file.at[c, 'RECHARGE_CNT'],
                     csv_file.at[c, 'CHOOSE'])
        if not rec.check_if_not_null():
            continue
        test_rec = []
        if rec.subs_id in records:
            test_rec = records[rec.subs_id]
        test_rec.append(rec)
        records[rec.subs_id] = test_rec
    return records
