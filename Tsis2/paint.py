import pygame
from datetime import datetime
from tools import flood_fill

# 1. Инициализация Pygame
pygame.init()
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("KBTU Paint - TSIS 2")

# 2. Создаем холст (белый слой, на котором рисуем)
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

# 3. Настройки и переменные
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

current_color = BLACK
brush_size = 2
tool = 'pencil'  # pencil, line, fill
drawing = False
start_pos = None
last_pos = None

def flood_fill(surface, x, y, new_color):
    """Алгоритм заливки (Flood-fill) через очередь (BFS)"""
    target_color = surface.get_at((x, y))
    if target_color == new_color:
        return
    
    queue = [(x, y)]
    while queue:
        curr_x, curr_y = queue.pop(0)
        if surface.get_at((curr_x, curr_y)) != target_color:
            continue
        
        surface.set_at((curr_x, curr_y), new_color)
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = curr_x + dx, curr_y + dy
            if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
                if surface.get_at((nx, ny)) == target_color:
                    queue.append((nx, ny))

# 4. Основной игровой цикл
running = True
while running:
    # Очищаем экран серым цветом (фон для интерфейса)
    screen.fill((200, 200, 200))
    # Рисуем наш холст поверх фона
    screen.blit(canvas, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Управление кнопками
        if event.type == pygame.KEYDOWN:
            # Выбор толщины (1, 2, 3)
            if event.key == pygame.K_1: brush_size = 2
            if event.key == pygame.K_2: brush_size = 5
            if event.key == pygame.K_3: brush_size = 10
            
            # Выбор инструментов
            if event.key == pygame.K_p: tool = 'pencil'
            if event.key == pygame.K_l: tool = 'line'
            if event.key == pygame.K_f: tool = 'fill'
            
            # Сохранение Ctrl + S
            if event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                filename = f"paint_save_{timestamp}.png"
                pygame.image.save(canvas, filename)
                print(f"Сохранено как {filename}")

        # Логика мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos
            
            if tool == 'fill':
                flood_fill(canvas, *event.pos, current_color)

        if event.type == pygame.MOUSEBUTTONUP:
            if drawing and tool == 'line':
                pygame.draw.line(canvas, current_color, start_pos, event.pos, brush_size)
            drawing = False

        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == 'pencil':
                curr_pos = event.pos
                pygame.draw.line(canvas, current_color, last_pos, curr_pos, brush_size)
                last_pos = curr_pos

    # Превью линии (рисуем на screen, а не на canvas, пока кнопка зажата)
    if drawing and tool == 'line':
        pygame.draw.line(screen, current_color, start_pos, pygame.mouse.get_pos(), brush_size)

    pygame.display.flip()

pygame.quit()
"""
================================================================
            GUIDE FOR TSIS 2: PAINT APPLICATION
================================================================
ГОРЯЧИЕ КЛАВИШИ (HOTKEYS):
  [1] - Малый размер кисти (2 px)
  [2] - Средний размер кисти (5 px)
  [3] - Большой размер кисти (10 px)
  
ИНСТРУМЕНТЫ (TOOLS):
  [P] - Pencil: Свободное рисование (карандаш)
  [L] - Line: Прямая линия (с предпросмотром при перетаскивании)
  [F] - Fill: Заливка области (Flood-fill алгоритм BFS)
  
СИСТЕМНЫЕ (SYSTEM):
  [Ctrl + S] - Сохранить холст в .PNG с временной меткой
================================================================
"""