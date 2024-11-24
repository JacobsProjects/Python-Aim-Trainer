import pygame
import random
import math
import time
from datetime import datetime
import os
import sys

def resource_path(relative_path):
    try:

        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def trainer():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    score = 0
    clicks = 0
    pygame.display.set_caption("Aim trainer")
    try:
        icon = pygame.image.load(resource_path("imgs/icon.jpg"))
        pygame.display.set_icon(icon)
    except:
        print("Could not load icon file - continuing without icon")
    target_x = random.randint(0, 1280)
    target_y = random.randint(0, 720)
    ballsize = random.randint(5, 30)
    growthspeed = .15
    maxballsize = 50
    game_over = False
    font = pygame.font.Font(None, 48)
    mouseX, mouseY = -100, -100  
    running = True
    game_over_start_time = None
    score_saved = False  

    def reset():
        nonlocal score, clicks, ballsize, target_x, target_y, game_over, score_saved
        score = 0
        clicks = 0
        ballsize = random.randint(5, 30)
        target_x = random.randint(0, 1280)
        target_y = random.randint(0, 720)
        game_over = False
    
    def save_score():
        accuracy = (score / clicks * 100) if clicks > 0 else 0
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        randomnumber = random.randint(300, 5000)
        
        with open(f"aim_trainer_scores{randomnumber}.txt", "a") as file:
            file.write(f"Date: {current_time}\n")
            file.write(f"Score: {score}\n")
            file.write(f"Clicks: {clicks}\n")
            file.write(f"Accuracy: {accuracy:.2f}%\n")
            file.write("-" * 30 + "\n")


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                mouseX, mouseY = pos  
                print('Detected click:', mouseX, mouseY)
                clicks = clicks + 1
                print(f"You have clicked {clicks} times")

        currentsize = ballsize
        ballsize += growthspeed
        if currentsize >= maxballsize:
            print('game over')
            game_over = True
            if game_over_start_time is None:
                game_over_start_time = pygame.time.get_ticks()
                if not score_saved:
                 save_score()
                 score_saved = True

        screen.fill("gray")
        
        distance = math.sqrt((mouseX - target_x)**2 + (mouseY - target_y)**2)
        if distance < ballsize:  
            print('Hit!')
            score = score + 1
            target_x = random.randint(0, 1280)
            target_y = random.randint(0, 720)
            ballsize = random.randint(10, 40)
            print(f'score: {score}')

        pygame.draw.circle(screen, (255, 35, 12), (target_x, target_y), ballsize)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        clicks_text = font.render(f"Clicks: {clicks}", True, (255, 255, 255))
        total_width = score_text.get_width() + clicks_text.get_width() + 20 
        textpos = (1280 - total_width) // 2
        screen.blit(score_text, (textpos, 10))
        screen.blit(clicks_text, (textpos + score_text.get_width() + 10, 10))

        if game_over:
            game_over_text = font.render("Game Over", True, (255, 0, 0))
            text_rect = game_over_text.get_rect(center=(1280//2, 720//2))
            screen.blit(game_over_text, text_rect)
            
            if pygame.time.get_ticks() - game_over_start_time > 3000:  
                reset()
                game_over_start_time = None

        pygame.display.flip()
        clock.tick(144)

    pygame.quit()

trainer()