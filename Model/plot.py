# библиотека для рисования математических графиков
import matplotlib.pyplot as plt


# Метод использовался для отрисовки полей Record()'ов
def plot(records, id):
    param_list = []
    counter = 0
    for pi in id:
        user_list = records[pi]
        for c in range(len(user_list)):
            if c > len(param_list) - 1:
                param_list.append(0)
            param_list[c] += user_list[c].charge
            counter += 1
    for p in param_list:
        p /= counter
    plt.title('negative_charge')
    plt.plot(param_list)
    plt.show()
