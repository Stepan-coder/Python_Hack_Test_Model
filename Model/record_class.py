# Библиотека для работы с датой и временем
import datetime
# Библиотека для работы с числами
import numpy as np


# Класс записей прочтённых из .csv файла
class Record():
    # Конструктор в котором мы передаём данные из каждой строки .csv файла
    def __init__(self,
                 subs_id, date_calc,
                 tariff_id, charge,
                 support_4G, support_3G,
                 LTE_traffic_flag, SMS_in_CNT,
                 SMS_out_CNT, calls_in_CNT,
                 calls_out_CNT, life_time,
                 duration_in_min, duration_out_min,
                 data_traffic_MB, sessions_CNT,
                 recharge, recharge_CNT,
                 chose):
        self.subs_id = subs_id
        self.date = self.parse_date_and_time(date_calc)
        self.tariff_id = tariff_id
        self.charge = charge
        self.support_4G = support_4G
        self.support_3G = support_3G
        self.LTE_traffic_flag = LTE_traffic_flag
        self.SMS_in_CNT = SMS_in_CNT
        self.SMS_out_CNT = SMS_out_CNT
        self.calls_in_CNT = calls_in_CNT
        self.calls_out_CNT = calls_out_CNT
        self.life_time = life_time
        self.duration_in_min = duration_in_min
        self.duration_out_min = duration_out_min
        self.data_traffic_MB = data_traffic_MB
        self.sessions_CNT = sessions_CNT
        self.recharge = recharge
        self.recharge_CNT = recharge_CNT
        self.chose = chose

    # Функция, которая конвертирует время из "8/1/2019 0:00" в понятное библиотеке datetime "08-01-2019 00:00"
    def parse_date_and_time(self, string):
        string = str(string)
        split_string = string.split(' ')
        date_str = split_string[0].split('/')
        time_str = split_string[1].split(':')
        date = datetime.datetime(int(date_str[2]), int(date_str[1]), int(date_str[0]), int(time_str[1]),
                                 int(time_str[0]))
        return date

    # Функция, которая проверяет на nan
    def check_if_not_null(self):
        return False if np.isnan(self.LTE_traffic_flag) \
                        or np.isnan(self.tariff_id) \
                        or np.isnan(self.life_time) \
            else True
