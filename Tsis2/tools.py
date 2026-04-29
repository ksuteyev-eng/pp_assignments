import pygame

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
            if 0 <= nx < surface.get_width() and 0 <= ny < surface.get_height():
                if surface.get_at((nx, ny)) == target_color:
                    queue.append((nx, ny))