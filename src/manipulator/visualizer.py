import matplotlib.pyplot as plt

def draw_workspace(link_1_length, link_2_length):
    outer_radius = link_1_length + link_2_length
    inner_radius = abs(link_1_length - link_2_length)

    outer_circle = plt.Circle(
        (0, 0),
        outer_radius,
        fill=False,
        linestyle="--",
        label="Max reach"
    )

    plt.gca().add_patch(outer_circle)

    if inner_radius > 0:
        inner_circle = plt.Circle(
            (0, 0),
            inner_radius,
            fill=False,
            linestyle=":",
            label="Min reach"
        )

        plt.gca().add_patch(inner_circle)

def visualize_manipulator(first_point,second_point, link_1_length, link_2_length, target_point=None):
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


    draw_workspace(link_1_length, link_2_length)
    plt.show()  # Показывает окно с графиком
#draw_workspace(2,2)