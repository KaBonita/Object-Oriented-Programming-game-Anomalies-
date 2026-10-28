import sys
import pygame
import random

from Anomaly_Classes import (
    Individual,
    Pandemic_Survivor_1,
    Walang_Pagkain_Buseng,
    Doctor,
    Politician,
    Bleeding_Love,
    Dorothea,
    Bata_Bata,
    Tomboy_Iskrambol,
    Hi_Vlog_Welcome_To_My_Guys,
    Ghouster,
    questions,
    START_SANITY,
    ACTION_COST,
    WRONG_GUESS_COST
)
    
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

def wrap_text(text, font, color, maxwidth):
    # for wrapping rendered text
    
    words = text.split(' ')
    lines = []
    current_line = ''

    for word in words:
        test = current_line + word + ' '
        line_width = font.size(test)[0]

        if line_width <= maxwidth:
            current_line = test
        else: 
            lines.append(current_line)
            current_line = word + ' '

    if current_line != '':
        lines.append(current_line)

    rendered = []
    for line_text in lines:
        surface = font.render(line_text, True, color)
        rendered.append(surface)

    return rendered
    
def game():
    clock = pygame.time.Clock()

    # pick individual to approach the player and decide whether anomalous or not
    character_classes = [
        Pandemic_Survivor_1,
        Walang_Pagkain_Buseng,
        Doctor,
        Politician,
        Bleeding_Love,
        Dorothea,
        Bata_Bata,
        Tomboy_Iskrambol,
        Hi_Vlog_Welcome_To_My_Guys,
        Ghouster
    ]
    choose_char = random.choice(character_classes)
    has_anomaly = random.choice([True, False])
    anomaly = random.randint(1, 11) if has_anomaly else None
    chosen_individual = choose_char(anomaly_id=anomaly)
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
    

    message = f'{chosen_individual.name} has approached the glass window. What will you do?'

    while sanity > 0:
        for event in pygame.event.get():
            if game == 'starting':
                inspect_button.draw(screen)
                talk_button.draw(screen)
                decision_button.draw(screen)

                if inspect_button.is_clicked(event):
                    sanity -= ACTION_COST
                    message = chosen_individual.inspect_appearance()
                elif talk_button.is_clicked(event):
                    game = 'talking'

                elif decision_button.is_clicked(event):
                    game = 'deciding'

            elif game == 'talking':
                if back_button.is_clicked(event):
                    game = 'starting'

                for id, button in question_buttons:
                    if button.is_clicked(event):
                        sanity -= ACTION_COST
                        message = chosen_individual.answer_question(id)
                        game = 'starting'

            elif game == 'deciding':
                if back_button.is_clicked(event):
                    game = 'starting'
                if yes_button.is_clicked(event):
                    if chosen_individual.anomaly_id is not None:
                        message = 'You have guessed correctly.'
                    else:
                        message = 'You have guessed incorrectly.'
                        sanity -= WRONG_GUESS_COST
                    return
                if no_button.is_clicked(event):
                    if chosen_individual.anomaly_id is None:
                        message = 'You have guessed correctly.'
                    else:
                        message = 'You have guessed incorrectly.'
                    return

        # drawing buttons
        screen.fill(Color_Background)

        player_window = pygame.Rect(50, 60, 700, 200)
        pygame.draw.rect(screen, (30, 30, 35), player_window, border_radius=6)
        pygame.draw.rect(screen, Color_Text, player_window, 2, border_radius=6)
        screen.blit(font_subtitles.render(f'Encountering: {chosen_individual.name.upper()}', True, Color_Title), (player_window.x + 20, player_window.y + 15))

        wrapped = wrap_text(chosen_individual.backstory, font_subtitles, Color_Text, 660)
        start_y = player_window.y + 50
        for i in range(len(wrapped)):
            line_surface = wrapped[i]
            screen.blit(line_surface, (player_window.x + 20, start_y + (i * 40)))

        dialogue = pygame.Rect(50, 275, 700, 220)
        pygame.draw.rect(screen, (25, 25, 30), dialogue, border_radius=6)
        pygame.draw.rect(screen, Color_Text, dialogue, 1, border_radius=6)

        if game != 'talking':
            wrapped_dialogue = wrap_text(message, font_buttons, Color_Text, 660)
            dialogue_y = dialogue.y + 20
            for i in range(len(wrapped_dialogue)):
                line_surface = wrapped_dialogue[i]
                screen.blit(line_surface, (dialogue.x + 20, dialogue_y + (i * 45)))

        if game == 'starting':
            inspect_button.draw(screen)
            talk_button.draw(screen)
            decision_button.draw(screen)

        elif game == 'talking':
            for _, button in question_buttons:
                button.draw(screen)
            back_button.draw(screen)    

        elif game == 'deciding':
            screen.blit(font_buttons.render('Is this individual an anomaly or not?', True, Color_Text), (220, 320))
            yes_button.draw(screen)
            no_button.draw(screen)
            back_button.draw(screen)
        
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

    clock = pygame.time.Clock()

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
        clock.tick(60)

if __name__ == '__main__':
    main_menu()
