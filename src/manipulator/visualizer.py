import matplotlib.pyplot as plt

def visualize_manipulator(first_point,second_point,target_point=None):
    x1, y1 = first_point
    x2, y2 = second_point
    x1points = [0, x1]
    y1points = [0, y1]

    x2points = [x1, x2]
    y2points = [y1, y2]

    target_x, target_y = target_point

    plt.figure() # Создает новое окно для графика
    plt.plot(x1points, y1points, "o-r", linewidth=2, label="Link 1")  # Маркер меняет обозначения на точках. o - точки. : - пунктир. r - red
    plt.plot(x2points, y2points, "o-b", linewidth=2, label="Link 2")
    plt.plot(target_x, target_y, "H-g", label='Target',ms = 10)
    plt.legend()
    plt.plot(0, 0, 'ko')
    plt.axhline(0, color="gray", linewidth=0.8) # Рисует горизонтальную ось y = 0
    plt.axvline(0, color="gray", linewidth=0.8) # Рисует вертикальную ось x = 0
    plt.grid(True) # Включает сетку
    plt.axis("equal") # Делает одинаковым масштаб по x и по y
    plt.title("2-Link Manipulator") # Ставит заголовок
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.text(0, 0, "Base")
    plt.text(x1, y1, "Joint 1")
    plt.text(x2, y2, "End")
    plt.show() # Показывает окно с графиком