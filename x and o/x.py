import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение констант
WIDTH, HEIGHT = 600, 600
LINE_COLOR = (0, 0, 0)
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS

# Цвета
WHITE = (255, 255, 255)
PLAYER_X_COLOR = (255, 0, 0)
PLAYER_O_COLOR = (0, 0, 255)

# Инициализация экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")

# Рисование игровой доски
def draw_board():
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Рисование крестика или нолика в клетке
def draw_symbol(row, col, symbol):
    x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    y = row * SQUARE_SIZE + SQUARE_SIZE // 2

    if symbol == 'X':
        pygame.draw.line(screen, PLAYER_X_COLOR, (x - 50, y - 50), (x + 50, y + 50), LINE_WIDTH)
        pygame.draw.line(screen, PLAYER_X_COLOR, (x + 50, y - 50), (x - 50, y + 50), LINE_WIDTH)
    elif symbol == 'O':
        pygame.draw.circle(screen, PLAYER_O_COLOR, (x, y), 50, LINE_WIDTH)

# Основной цикл игры
def main():
    board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    current_player = 'X'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if board[clicked_row][clicked_col] == ' ':
                    board[clicked_row][clicked_col] = current_player
                    draw_symbol(clicked_row, clicked_col, current_player)

                    # Проверка на победителя или ничью
                    if check_winner(board, current_player):
                        print(f'Игрок {current_player} выиграл!')
                        pygame.quit()
                        sys.exit()
                    elif check_draw(board):
                        print('Ничья!')
                        pygame.quit()
                        sys.exit()

                    current_player = 'O' if current_player == 'X' else 'X'

        draw_board()
        pygame.display.flip()

# Проверка наличия победителя
def check_winner(board, player):
    # Проверка по строкам и столбцам
    for i in range(BOARD_ROWS):
        if all(board[i][j] == player for j in range(BOARD_COLS)) or \
           all(board[j][i] == player for j in range(BOARD_COLS)):
            return True

    # Проверка по диагоналям
    if all(board[i][i] == player for i in range(BOARD_ROWS)) or \
       all(board[i][BOARD_COLS - 1 - i] == player for i in range(BOARD_ROWS)):
        return True

    return False

# Проверка на ничью
def check_draw(board):
    return all(board[i][j] != ' ' for i in range(BOARD_ROWS) for j in range(BOARD_COLS))

if __name__ == "__main__":
    main()
