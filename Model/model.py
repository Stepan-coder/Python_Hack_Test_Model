# Импортируем библиотеки для работы с keras'ом, рисования графиков
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense, Dropout, LeakyReLU
from tensorflow.keras.models import Sequential, load_model
# Импортируем всё из prepearing
from prepearing import *

# Финально доготавливаем данные, разделяем на учебную и тестовую выборку(для авто тестирования)
x, y = prepearing('Данные-по-Data_Motiv.csv')
x = x[:768]
y = y[:768]
count_examples = len(y)
count_train = int(count_examples * 0.4)
x_train = np.array(x[:count_train])
y_train = np.array(y[:count_train])
x_test = np.array(x[count_train + 1:])
y_test = np.array(y[count_train + 1:])
# Выводим данные для визуального осмотра входных и желаемых выходных значений
for t in range(len(x_train)):
    print(x_train[t], y_train[t])
for t in range(len(x_test)):
    print(x_test[t], y_test[t])

# # Создаём, компилируем,обучаем и сохраняем модель
# model = Sequential()
# model.add(Dense(64, input_dim=10, activation='relu'))
# model.add(Dropout(0.8))
# model.add(LeakyReLU())
# model.add(Dense(64, activation='relu'))
# model.add(Dropout(0.8))
# model.add(LeakyReLU())
# model.add(Dense(1, activation='sigmoid'))
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# history = model.fit(x_train, y_train, epochs=1536, batch_size=256, validation_data=(x_test, y_test), verbose=2)
# model.save('motive.h5')
#
# # Рисуем график ответов
# plt.plot(history.history['acc'])
# plt.plot(history.history['val_acc'])
# plt.title('Model accuracy')
# plt.ylabel('Accuracy')
# plt.xlabel('Epoch')
# plt.legend(['Train', 'Test'], loc='upper left')
# plt.show()
#
# # Рисуем график ошибок
# plt.plot(history.history['loss'])
# plt.plot(history.history['val_loss'])
# plt.title('Model loss')
# plt.ylabel('Loss')
# plt.xlabel('Epoch')
# plt.legend(['Train', 'Test'], loc='upper left')
# plt.show()
#
# # Выводим % обучения модели
# print(np.mean(history.history["val_acc"]))


model = load_model('motive.h5')
to_predict = []
to_predict.append(x_test[2])
print(model.predict_classes(np.array(to_predict)), y_test[2])
