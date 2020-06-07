import numpy as np
import random as rm
import argparse
#Создаем вводимые значения через командую строку и описание для них.
parser = argparse.ArgumentParser(description='Цепь Маркова')
parser.add_argument('days', type=int, help='Введите количество дней для просчета\n')
parser.add_argument('arg1', type=str, help='Введите начальное состояние из трех вариантов:\n1.Сон\n2.Мороженное\n3.Бег\n')
args = parser.parse_args()
# Пространство состояний

states = ["Сон", "Мороженное", "Бег"]

# Возможные последовательности событий

transitionName = [["SS", "SR", "SI"], ["RS", "RR", "RI"], ["IS", "IR", "II"]]

# Матрица вероятностей (переходная матрица)

transitionMatrix = [[0.2, 0.6, 0.2], [0.1, 0.6, 0.3], [0.2, 0.7, 0.1]]

if sum(transitionMatrix[0]) + sum(transitionMatrix[1]) + sum(transitionMatrix[1]) != 3:

    print("Что-то пошло не так")

else: 

	print("Все хорошо")

# Функция, которая реализует марковскую модель для прогнозирования состояния / настроения.

def activity_forecast(days):

    # Выберите начальное состояние
    activityToday = str(args.arg1)
    print("Начальное состояние: " + activityToday)

    # Хранит последовательность принятых состояний. И так, пока это только начальное состояние.

    activityList = [activityToday]
    i = 0

    # Рассчитывает вероятность активности из списка

    prob = 1

    while i != days:

        if activityToday == "Сон":

            change = np.random.choice(transitionName[0], replace=True, p=transitionMatrix[0])

            if change == "SS":

                prob = prob * 0.2
                activityList.append("Сон")

                pass

            elif change == "SR":

                prob = prob * 0.6
                activityToday = "Бег"
                activityList.append("Бег")

            else:

                prob = prob * 0.2
                activityToday = "Мороженное"
                activityList.append("Мороженное")

        elif activityToday == "Бег":

            change = np.random.choice(transitionName[1], replace=True, p=transitionMatrix[1])

            if change == "RR":

                prob = prob * 0.5
                activityList.append("Бег")

                pass

            elif change == "RS":
 
                prob = prob * 0.2
                activityToday = "Сон"
                activityList.append("Сон")

            else:

                prob = prob * 0.3
                activityToday = "Мороженное"
                activityList.append("Мороженное")

        elif activityToday == "Мороженное":

            change = np.random.choice(transitionName[2], replace = True, p = transitionMatrix[2])

            if change == "II":
  
                prob = prob * 0.1
                activityList.append("Мороженное")

                pass

            elif change == "IS":

                prob = prob * 0.2
                activityToday = "Сон"
                activityList.append("Сон")

            else:

                prob = prob * 0.7
                activityToday = "Бег"
                activityList.append("Бег")
        i += 1

    print("Возможные состояния: " + str(activityList))
    print("Конечное состояние после "+ str(days) + " дней: " + activityToday)
    print("Вероятность возможной последовательности состояний: " + str(prob))

# Функция, которая прогнозирует возможное состояние на следующие n дней
activity_forecast(int(args.days))