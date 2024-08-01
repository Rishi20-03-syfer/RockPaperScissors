import random
import pygame
from sys import exit

def computer(choices):
    return random.choice(choices)

# Initialize Pygame
pygame.init()

# Display constraints
screen = pygame.display.set_mode((950, 400))
pygame.display.set_caption("Rock-Paper-Scissors")
icon = pygame.image.load('rock-paper-scissors.png')
pygame.display.set_icon(icon)

# Load and resize images
rock_img = pygame.image.load('rock.png')
paper_img = pygame.image.load('paper.png')
scissors_img = pygame.image.load('scissors.png')

rock_img_resize = pygame.transform.scale(rock_img, (100, 100))
paper_img_resize = pygame.transform.scale(paper_img, (100, 100))
scissors_img_resize = pygame.transform.scale(scissors_img, (100, 100))

# Define button rectangles
rock_button_user = rock_img_resize.get_rect(topleft=(550, 150))
paper_button_user = paper_img_resize.get_rect(topleft=(650, 150))
scissors_button_user = scissors_img_resize.get_rect(topleft=(750, 150))

rock_button_computer = rock_img_resize.get_rect(topleft=(50, 150))
paper_button_computer = paper_img_resize.get_rect(topleft=(150, 150))
scissors_button_computer = scissors_img_resize.get_rect(topleft=(250, 150))

# Text fonts and surfaces
font_large = pygame.font.Font('freesansbold.ttf', 50)
font_medium = pygame.font.Font('freesansbold.ttf', 30)
font_small = pygame.font.Font('freesansbold.ttf', 20)

computer_text_surface = font_large.render("Computer", True, 'White')
user_text_surface = font_large.render("You", True, "White")
score_text_surface = font_large.render("Winner", True, "white")
rounds_text_surface = font_medium.render("Rounds", True, "white")
total_score_surface = font_medium.render("Total Wins", True, "white")

result_text_surface = font_medium.render("", True, 'white')
comp_choice_surface = font_medium.render("", True, "white")
user_choice_surface = font_medium.render("", True, 'white')
rounds_surface = font_medium.render("", True, "white")
user_score_surface = font_medium.render("0", True, 'white')
comp_score_surface = font_medium.render("0", True, 'white')

# Initialize scores and option list
option = ['rock', 'paper', 'scissors']
comp = 0
user = 0
cnt = 0

# Load sounds
click_sound = pygame.mixer.Sound('click.wav')
win_sound = pygame.mixer.Sound('win.wav')
lose_sound = pygame.mixer.Sound('lose.wav')

# Function to check button click
def is_button_clicked(button_rect, pos):
    return button_rect.collidepoint(pos)

# Function to evaluate choices
def evaluate(comp_choice, user_choice):
    global user, comp
    result = ""
    if user_choice == comp_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and comp_choice == 'scissors') or \
         (user_choice == 'paper' and comp_choice == 'rock') or \
         (user_choice == 'scissors' and comp_choice == 'paper'):
        result = "User"
        user += 1
        pygame.mixer.Sound.play(win_sound)
    else:
        result = "Computer"
        comp += 1
        pygame.mixer.Sound.play(lose_sound)
    return result

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.Sound.play(click_sound)
            mouse_pos = event.pos
            cnt += 1

            cc = computer(option)
            comp_choice_surface = font_medium.render(f"Computer chose: {cc}", True, "white")
            rounds_surface = font_medium.render(f"Round: {cnt}", True, "white")

            if is_button_clicked(rock_button_user, mouse_pos):
                user_choice_surface = font_medium.render("You chose: rock", True, 'white')
                result_text_surface = font_medium.render(evaluate(cc, 'rock'), True, 'white')

            elif is_button_clicked(paper_button_user, mouse_pos):
                user_choice_surface = font_medium.render("You chose: paper", True, 'white')
                result_text_surface = font_medium.render(evaluate(cc, 'paper'), True, 'white')

            elif is_button_clicked(scissors_button_user, mouse_pos):
                user_choice_surface = font_medium.render("You chose: scissors", True, 'white')
                result_text_surface = font_medium.render(evaluate(cc, 'scissors'), True, 'white')

            user_score_surface = font_medium.render(f"User: {user}", True, "white")
            comp_score_surface = font_medium.render(f"Computer: {comp}", True, "white")

    screen.fill((0, 0, 0))

    screen.blit(rock_img_resize, rock_button_computer.topleft)
    screen.blit(paper_img_resize, paper_button_computer.topleft)
    screen.blit(scissors_img_resize, scissors_button_computer.topleft)

    screen.blit(rock_img_resize, rock_button_user.topleft)
    screen.blit(paper_img_resize, paper_button_user.topleft)
    screen.blit(scissors_img_resize, scissors_button_user.topleft)

    screen.blit(computer_text_surface, (70, 50))
    screen.blit(user_text_surface, (650, 50))
    screen.blit(score_text_surface, (370, 100))

    screen.blit(result_text_surface, (370, 180))
    screen.blit(comp_choice_surface, (70, 270))
    screen.blit(user_choice_surface, (650, 270))

    screen.blit(rounds_text_surface, (370, 250))
    screen.blit(rounds_surface, (400, 300))
    screen.blit(total_score_surface, (70, 320))
    screen.blit(total_score_surface, (650, 320))

    screen.blit(comp_score_surface, (70, 360))
    screen.blit(user_score_surface, (650, 360))

    pygame.display.update()
