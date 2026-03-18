def draw_grid_2x2():
    def horizontal():
        print('+', '- ' * 4, '+', '- ' * 4, '+', sep='')
    def vertical():
        print('|', ' ' * 8, '|', ' ' * 8, '|', sep='')
    for i in range(2):
        horizontal()
        for j in range(4):
            vertical()
    horizontal()
draw_grid_2x2()
def draw_grid_4x4():
    def horizontal():
        print('+', '- ' * 4, '+', '- ' * 4, '+', '- ' * 4, '+', '- ' * 4, '+', sep='')
    def vertical():
        print('|', ' ' * 8, '|', ' ' * 8, '|', ' ' * 8, '|', ' ' * 8, '|', sep='')
    for i in range(4):
        horizontal()
        for j in range(4):
            vertical()
    horizontal()
draw_grid_4x4()