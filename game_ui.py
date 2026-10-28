import sys
import pygame
import random

from Anomaly_Classes import(Individual, Pandemic_Survivor_1, Doctor, Dorothea, Walang_Pagkain_Buseng, Bata_Bata, Politician, Tomboy_Iskrambol, Hi_Vlog_Welcome_To_My_Guys, Ghouster, Bleeding_Love, questions, START_SANITY, ACTION_COST, WRONG_GUESS_COST)

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('AnomalEEE')

# ui colors
Color_Background = (15, 15, 18)
Color_Title = (220, 50, 50)
Color_Text = (200, 200, 200)

# ui fonts - to be edited, arial is only a placeholder
font_title = pygame.font.SysFont('arial', 48, bold=True)
font_buttons = pygame.font.SysFont('arial', 28)
font_subtitles = pygame.font.SysFont('arial', 18, italic=True)

# button class
class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        text_surface = font_buttons.render(self.text, True, Color_Text)
        text_rectangle = text_surface.get_rect(center=self.rect.center)
        pygame.draw.rect(surface, Color_Text, self.rect, 2, border_radius=4)
        surface.blit(text_surface, text_rectangle)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

def game():
    clock = pygame.time.Clock()

    # pick individual to approach the player and decide whether anomalous or not
    characters = [Pandemic_Survivor_1, Doctor, Dorothea, Bleeding_Love, Politician, Hi_Vlog_Welcome_To_My_Guys, Walang_Pagkain_Buseng, Ghouster, Bata_Bata, Tomboy_Iskrambol]
    choose_char = random.choice(characters)
    has_anomaly = random.choice([True, False])
    anomaly = random.randint(1, 11) if has_anomaly else None
    individual = choose_char(anomaly_id=anomaly)
    sanity = START_SANITY

    game = 'starting'

    # action buttons
    inspect_button = Button('Inspect Individual', 50, 520, 220, 40)
    talk_button = Button('Talk to the Individual', 290, 520, 220, 40)
    decision_button = Button('Anomaly or Not?', 530, 520, 220, 40)

    # talk/question buttons
    question_buttons = []
    for id, dialogues in questions.items():
        question_buttons.append((id, Button(f'Q{id}: {dialogues[:40]}...', 50, 290 + (id * 40), 500, 35)))
        back_button = Button('Back', 570, 520, 180, 40)

    # decisions
    yes_button = Button('Anomaly', 200, 380, 140, 45)
    no_button = Button('Human', 420, 380, 180, 45)
    

    while sanity > 0:
        for event in pygame.event.get():
            if game == 'starting':

                if inspect_button.is_clicked(event):
                    sanity -= ACTION_COST
                    message = individual.inspect_appearance()
                elif talk_button.is_clicked(event):
                    game == 'talking'

                elif decision_button.is_clicked(event):
                    game == 'deciding'

            elif game == 'talking':
                if back_button.is_clicked(event):
                    game == 'starting'

                for id, button in question_buttons:
                    if button.is_clicked(event):
                        sanity -= ACTION_COST
                        message = individual.answer_question(id)

            elif game == 'deciding':
                if back_button.is_clicked(event):
                    game == 'starting'
                if yes_button.is_clicked(event):
                    if individual.anomaly_id is not None:
                        message = 

        

    pygame.display.flip()
    clock.tick(60)

# main menu function
def main_menu():
    button_width, button_height = 250, 50
    center = 800 // 2 - button_width // 2

    # menu buttons
    start_button = Button('START GAME', center, 280, button_width, button_height)
    instructions_button = Button('INSTRUCTIONS', center, 350, button_width, button_height)
    quit_button = Button('QUIT GAME', center, 420, button_width, button_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if start_button.is_clicked(event):
                game()

            if instructions_button.is_clicked(event):
                print('Opening Instructions Screen...')

            if quit_button.is_clicked(event):
                pygame.quit()
                sys.exit()

        # drawing      
        screen.fill(Color_Background)
        title_surface = font_title.render('AnomalEEE', True, Color_Title)
        title_rectangle = title_surface.get_rect(center=(screen_width // 2, 150))
        screen.blit(title_surface, title_rectangle)

        subtitle_surface = font_subtitles.render('Verify who enters. Protect your sanity.', True, (120, 120, 130))
        subtitle_rectangle = subtitle_surface.get_rect(center = (screen_width // 2, 205))
        screen.blit(subtitle_surface, subtitle_rectangle)

        start_button.draw(screen)
        instructions_button.draw(screen)
        quit_button.draw(screen)

        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(60)

