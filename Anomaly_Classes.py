import time
import random
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
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
        self.shape = pygame.Rect(x, y, width, height)

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
                print('Welcome to AnomalEEE...')

            if instructions_button.is_clicked(event):
                print('Opening Instructions Screen...')

            if quit_button.is_clicked(event):
                pygame.quit()
                sys.exit()

        # drawing      
        screen.fill(Color_Background)
        title_surface = font_title.render('AnomalEEE', True, Color_Title)
        title_rectangle = title_surface.get_rect(800 // 2, 150)
        screen.blit(title_surface, title_rectangle)

        subtitle_surface = font_subtitles.render('Verify who enters. Protect your sanity.', True, (120, 120, 130))
        subtitle_rectangle = subtitle_surface.get_rect(center = (800 // 2, 205))
        screen.blit(subtitle_surface, subtitle_rectangle)

        start_button.draw(screen)
        instructions_button.draw(screen)
        quit_button.draw(screen)

if __name__ == '__main__':
    main_menu()


START_SANITY = 100
ACTION_COST = 5
WRONG_GUESS_COST = 20

questions = {1: "Where have you come from?",
             2: "Why should I let you in?",
             3: "Have you noticed anything unusual about yourself lately?",
             4: "Where were you when the first outbreak occurred?",
             5: "Is there anyone waiting for you inside?"}

#_____________________________________________________________
# Individual parent class
#_____________________________________________________________

class Individual:
    # All anomaly defenitions.
    ANOMALIES = {
        #Speech Anomalies
        1: "Delayed Speech",
        2: "Irregular Breathing",
        3: "Irregular Tremors",
        4: "Speech Impediment",
        5: "Inappropriate Responses",
        6: "Eerie Echo",
        7: "Weird Slips",

        # Physical/Appearance Anomalies
        8: "Unusual Pallor",
        9: "Infrequent Blinking",
        10: "Faint Discoloration",
        11: "Lag in Expression",}

    #initializing code for each subclass/objject
    def __init__(self,
        name,
        backstory,
        appearance,
        dialogues,
        anomaly_id=None):
        self.name = name
        self.backstory = backstory
        self.appearance = appearance
        self.dialogues = dialogues
        self.anomaly_id = anomaly_id

        self.asked_questions = set()
        self.is_inspected = False

    #_____________________________________________________________
    # Functions / Methods para sa individuals
    #_____________________________________________________________

    def answer_question(self, question_id):
        #Make the character answer a question, requires positional argument for the question number. Applies dialogue anomaly if appropriate
            if question_id not in self.dialogues:
                return "Invalid question."

            if question_id in self.asked_questions:
                return "You have already asked this question."

            self.asked_questions.add(question_id)
            response = self.dialogues[question_id]

            if self.anomaly_id == 1:  # Delayed Speech
                sys.stdout.write("... They stare through the glass, hesitating ")
                for _ in range(3):
                    time.sleep(0.7)
                    sys.stdout.write(".")
                    sys.stdout.flush()
                print("\n")

            elif self.anomaly_id == 2:  # Irregular Breathing
                words = response.split()
                if len(words) > 4:
                    mid = random.randint(1, len(words) - 2)
                    breath_sounds = ["... ahh ...", "... wheeze ...", "... gasp ...", "... hss ..."]
                    words.insert(mid, random.choice(breath_sounds))
                response = " ".join(words)

            elif self.anomaly_id == 3:  # Verbal Tremors (Max is 3 tremors to avoid too many/it being unnatural.)
                words = response.split()
                valid = [i for i, w in enumerate(words) if len(w.strip(".,!?-")) > 3]
                if valid:
                    for i in random.sample(valid, min(random.randint(1, 3), len(valid))): 
                        clean = words[i].strip(".,!?-")
                        words[i] = f"{clean[0]}-{words[i]}"
                response = " ".join(words)

            elif self.anomaly_id == 4:  # Speech Impediment (Max is 5 tremors to avoid too many/it being unnatural.)
                words = response.split()
                valid = [i for i, w in enumerate(words) if len(w.strip(".,!?-")) > 4]
                if valid:
                    for i in random.sample(valid, min(random.randint(2, 5), len(valid))):
                        clean = words[i].strip(".,!?-")
                        chars = list(clean[1:-1])
                        random.shuffle(chars)
                        words[i] = words[i].replace(clean, clean[0] + "".join(chars) + clean[-1])
                response = " ".join(words)

            elif self.anomaly_id == 5:  # Inappropriate Responses
                other_keys = [k for k in self.dialogues.keys() if k != question_id]
                if other_keys:
                    wrong_key = random.choice(other_keys)
                    response = f"... {self.dialogues[wrong_key]}"

            elif self.anomaly_id == 6:  # Eerie Echo
                words = response.split()
                if words:
                    last_word = words[-1].strip(".,!?-")
                    response += f".. {last_word}..."

            elif self.anomaly_id == 7:  # Weird Slips
                weird_slips = [
                    " It is surprisingly quiet inside my head.",
                    " I... sorry, I lost my train of thought for a second.",
                    " It's hard to remember what day of the week it is.",
                    " Everything just... feels so quiet lately.",
                    " I guess I'm... we're all just tired of walking.",
                ]
                response += random.choice(weird_slips)

            return response

            
    def inspect_appearance(self):
            #Provides a description of character appearance. Applies anomaly when appropriate
            self.is_inspected = True
            description = self.appearance

            if self.anomaly_id == 3:  # Physical Tremors
                tremor_descriptions = [
                    " Their knuckles look stiff and slightly rigid.",
                    " Their fingers twitch with a faint tremor.",
                    " They keep shifting their weight from one foot to the other.",
                    " They adjust their collar twice in a row."
                ]
                description += random.choice(tremor_descriptions)

            elif self.anomaly_id == 8:  # Unusual Pallor
                pallor_descriptions = [
                    " Their skin looks unusually pale.",
                    " They look a bit washed out under the room's lighting.",
                    " Their skin looks slightly dull, like someone who needs sleep.",
                    " They have faint shadows under their eyes and pale cheeks."
                ]
                description += random.choice(pallor_descriptions)

            elif self.anomaly_id == 9:  # Infrequent Blinking
                blinking_descriptions = [
                    " Their eyes stay wide and fixed on you the whole time.",
                    " They don't seem to look away or glance around at all.",
                    " Their eyelids barely move, even when you lean in closer."
                ]
                description += random.choice(blinking_descriptions)

            elif self.anomaly_id == 10:  # Faint Discoloration
                discoloration_descriptions = [
                    " There's a tiny dark spot near the corner of their mouth.",
                    " Their lower lip looks slightly dry and purple on one side.",
                    " A faint mark sits near their bottom lip, almost like a smudge of purple."
                ]
                description += random.choice(discoloration_descriptions)

            elif self.anomaly_id == 11:  # Lag in Expression
                lag_descriptions = [
                    " They blink once, then slowly nod a second later.",
                    " Their mouth twitches slightly before they settle into a neutral look.",
                    " Their expression settles a beat too late.",
                    " Their head turns toward you first, followed by their gaze."
                ]
                description += random.choice(lag_descriptions)
            
            return description

    def get_anomaly_name(self):
        #Gets the name of the anomaly
        if self.anomaly_id is None:
            return "No anomaly"

        return self.ANOMALIES.get(self.anomaly_id, "Unknown anomaly")

    def talk_to_character(self):
        #asks the character a question.
        for number, question in questions.items(): 
            print(f"{number}. {question}")

        choice = input("\nAsk which question? ")

        if choice.isdigit():
            print(self.answer_question(int(choice)))
        else:
            print("Invalid question.")

    def guess_anomaly(self, sanity):
        #Guess the anomaly, reduces sanity if wrong.
        if (input("Is the character an anomaly? (y/n)") == "y") == (self.anomaly_id is not None):
            print("Correct.")
            return sanity

        print("Wrong guess!") # if wrong guess
        return sanity - WRONG_GUESS_COST

    def character_encounter(self, character, sanity):
        #Gives choices for what to do when a character is encountered.
        print("\nAN INDIVIDUAL APPROACHES YOU\n")
        print(f"Character: {character}\n")
        print(self.backstory)

        while sanity > 0:
            print(f"\nSanity: {sanity}")
            print("1. Inspect their body")
            print("2. Talk to them")
            print("3. Make your decision")
            choice = input("> ")

            if choice == "1":
                print(self.inspect_appearance())
                sanity -= ACTION_COST

            elif choice == "2":
                self.talk_to_character()
                sanity -= ACTION_COST

            elif choice == "3":
                return self.guess_anomaly(sanity)

            else:
                print("Invalid choice.")




#_____________________________________________________________
# Characters. Define each subclass of individual as each character
#_____________________________________________________________

class Pandemic_Survivor_1(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Pandemic Survivor 1",
            backstory="Survived the pandemic. Has nowhere to settle in and goes around different places in \nhopes of finding refuge and someone he/she might know.",
            appearance="A traveller who appears to have been travelling for years. They are wearing a worn-out backpack, and have dark circles under their eyes.",
            dialogues={1: "I come from the east, I've been moving from place to place since I left my home. \nI hope I can finally find a place to stay.",
                2: "I don't have a lot to offer, I just need a shelter to stay in.",
                3: "I've been feeling tired lately, but I guess that's normal when you've been walking for days.",
                4: "In my hometown, everybody was living so peacefully, it was a rather quiet place in the \ncountryside, but everything just fell apart so quickly.",
                5: "Not that I know of, but hopefully I can find somebody I know in there.",
            }, anomaly_id=anomaly_id)

class Walang_Pagkain_Buseng(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Walang Pagkain Buseng",
            backstory="Locked themselves in for months after the pandemic announcement and survived on a huge \nstock of food and rations. Only went out now because the food ran out, and is going \naround asking people for rations.",
            appearance="An individual carrying an empty sack, they look visibly undernourished and is wearing \nold dusty house clothes.",
            dialogues={
                1: "My house. I haven't left that place in months. I thought my supplies would last, but I guess \nI overestimated.",
                2: "Because I'm hungry! I've got nothing left to eat. I'm just looking for food and somewhere safe.",
                3: "Unusual? I'm starving! I've barely eaten anything these past few days. What else do you expect?",
                4: "At home. The moment the announcements came out, I locked everything up and stocked as much \nfood as I could.",
                5: "No. I've been alone this entire time. Honestly, I'm just hoping someone here has food to spare.",
            }, anomaly_id=anomaly_id)

class Doctor(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Doctor",
            backstory="Came from the nearest hospital. Desperately tried to find a cure but failed, and ended up \nin a depressive state, especially since all his colleagues also succumbed to the \nvirus.",
            appearance="Wears an old lab coat which is visibly torn and worn-out, a face mask, and broken glasses.",
            dialogues={
                1: "I came from the hospital but I am unaffected by the virus, I swear.",
                2: "I'm a doctor. I can be of help to anyone who has injuries… even those who have possible symptoms. \nAlthough we did not finish the cure, I have studied it enough to at least \nassist the survivors.",
                3: "No… not as of late, anyway. I don't know, really. Everything is unusual when half of the world's \npopulation is gone because of the outbreak.",
                4: "The hospital. I was working. We experienced the first surge of patients, how they panicked, how \neveryone was dying right in front of my eyes.",
                5: "No. I'm the only one who made it out alive.",
            }, anomaly_id=anomaly_id)

class Politician(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="The Politician",
            backstory="A politician who was well-protected in the comfort of his home. Once he found out people were \nbecoming immune to the virus, he started reaching out to the nearest survivors, \nbuilding connections and trying to lead the newly established group.",
            appearance="Unlike the other survivors who came before him, he was more well-kept and clean, in a way. The \nonly tell-tale sign that he was ever in a pandemic was the mask on his \nface. His clothes are clean and simple, hair swept back, and his posture means business.",
            dialogues={
                1: "Do you not know me? I suppose you do not watch the news. I came from the neighboring city.",
                2: "Huh. Nobody has ever asked me that question. I guess you really have no idea who I am. Does this \ncity have a leader? Someone competent enough to lead the citizens? If not, \nthen I see no reason why you should not let me in.",
                3: "I am perfectly fine. What's more unusual is you asking more and more questions.",
                4: "I was at the city hall. I was the one who issued the lockdown announcement. You probably know who \nI am now?",
                5: "I'm sure everyone is waiting for someone to step up and help them.",
            }, anomaly_id=anomaly_id)

class Bleeding_Love(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Bleeding Love",
            backstory="Lost the love of their life, and is unsure whether said significant other is dead or simply \nlost, since they were separated during the \"hoarding incidents\" where people \nransacked all the stores. After gaining immunity, they are deadset on finding their \nsignificant other.",
            appearance="A person with intensely swollen eyes yet is still in the middle of crying. He is at his most \nvulnerable and disheveled state, carrying nothing but a locket with a picture \nof a person that he is desperately trying to find.",
            dialogues={
                1: "I came from nearby, but I have been going around, I'm trying to find someone… Have you seen them?",
                2: "I need to find someone. I need to know if she's inside, please, I don't know where she went \nafter we got separated during the hoarding incident in our city. I can only hope \nthat she is safe inside this city.",
                3: "Nothing… I don't care what's happening to me. I need to know what happened to her.",
                4: "We were together. We were outside. We immediately looked for refuge. I don't clearly remember \nwhere, all that was important to me at that time was that we were together.",
                5: "Her… she might be waiting for me inside. I promised her that I'll find her no matter what, that \nwe will be together forever.",
            }, anomaly_id=anomaly_id)

class Dorothea(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Dorothea",
            backstory="The player's old friend from high school. She moved to a different city but ended up back \nhere when her local government unit tried to transfer/evacuate citizens to other \nsites due to lack of resources. She does not know anyone in the neighborhood and is \ntrying to find help.",
            appearance="A student still wearing her uniform, worn-out shoes, and carries a black backpack. Her hair \nis tied up in a messy bun, with strands of hair covering her face which was also \nstained with dirt and dust. She is awfully familiar to the player, a face that you \nhave not seen in a long, long time.",
            dialogues={
                1: "Oh… I don't know how I got here. We were transferred from our city, but I didn't think we'd end \nup here. When I woke up, I was surprised as well. The only familiar face I know \nis you, so..",
                2: "All of the people I was with suddenly disappeared. I have no idea what to do and where to go. I \nwas hoping that you—or, people here can help me.",
                3: "Nope. I'm perfectly fine. I've been regularly taking the vitamins they gave us from back home.",
                4: "Ah… I was at school. I ended up staying there for the entirety of the lockdown until we ran out of \nsupplies and we had to get transferred to a different site.",
                5: "Maybe? I was with a group, so, there's a chance that they found this place before I did and they're \nalready inside.",
            }, anomaly_id=anomaly_id)

class Bata_Bata(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Bata, Bata",
            backstory="A random kid who lost his parents and is trying to find them. Owns a small teddy bear, the \nlast thing he can remember of his parents. Thinks the player is his mother/father \nand is crying at their doorstep because he is mad that his parents left him to get \nfood.",
            appearance="An awfully malnourished kid wearing tattered clothes, holding the arm of a dirty teddy \nbear. He looks like someone around the age of 5 or 6, with eyes that are on the verge \nof tears. His feet are bare and both his arms are covered in soot.",
            dialogues={
                1: "I don't know… I want my mama.",
                2: "My mama and papa. They leave…",
                3: "Huh? I don't know.. I don't know!",
                4: "With mama and papa… Playing with bear.",
                5: "Mama and papa… Find mama and papa inside!",
            }, anomaly_id=anomaly_id)

class Tomboy_Iskrambol(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Tomboy Iskrambol",
            backstory="A vendor already trying to earn a profit early in the post-pandemic period. One of the \npeople hit by the economic crisis caused by the virus, and desperate to regain all of \nher past businesses.",
            appearance="A short-haired woman wearing a faded graphic shirt, knee-length denim shorts, and \nslippers. She has a small towel draped over one shoulder and a worn waist pouch. Her \nclothes have a few stains of iskrambol.",
            dialogues={
                1: "From the market near the highway. I was trying to sell some stuff there, but barely \nanyone was buying.",
                2: "I can help out around here, too. Just need somewhere safe to stay.",
                3: "Unusual? Nah. I'm just tired. Haven't had a decent night's sleep since the outbreak \nstarted.",
                4: "At my stall, selling iskrambol near the school. One minute, people were buying snacks; \nthe next, everyone was running for their lives. I had to leave everything behind.",
                5: "No. Just me. I used to have a proper business before all this happened. Lost everything, \nand now I'm back to selling whatever I can find.",
            }, anomaly_id=anomaly_id)

class Hi_Vlog_Welcome_To_My_Guys(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Hi Vlog Welcome To My Guys",
            backstory="An influencer before the pandemic who documented life during the outbreak, with \nrecordings of living underground, looking for food, and who they were with whenever they \nevacuated. After gaining immunity, they started vlogging again, going around interviewing \npeople about their livelihood and how they survived.",
            appearance="A young man in his early 20s wearing an oversized hoodie. A digital camera hangs \nfrom his neck. His hair is unevenly cut, and there are dark circles under his eyes.",
            dialogues={
                1: "What's up, guys- okay sorry force of habit. Just came from one of the underground shelters \ndowntown. I stayed there for a long time, but food was running out.",
                2: "Look, I've got recordings of places I've been to, evacuation routes, shelters, supply \nlocations, all kinds of stuff. I can show you what I found. Might even help you locate \nother survivors. And hey, if you're okay with it, maybe I could document how this \nsettlement is rebuilding. History's gotta be recorded, right?",
                3: "Well, I got sick a while back, but somehow I recovered. People started saying I might be \nimmune. I feel mostly fine now, though. I mean, I'm exhausted, my sleep schedule is \ncompletely destroyed, and my hair looks like I cut it with a spoon, but that's not \nexactly newsworthy.",
                4: "At home, recording a video. I was doing one of those ordinary daily vlogs, you know, food, \nrandom stuff, talking about my day. Then people started evacuating, and suddenly I \nwas recording something nobody could've prepared for. At first, I thought I'd document \neverything until things went back to normal. Didn't realize how long I'd be waiting.",
                5: "Not that I know of. I got separated from my group while we were moving between shelters. \nI've replayed my recordings so many times, looking for familiar faces or clues about \nwhere they went. Sometimes I wonder if I should've put the camera down and just stayed \nwith them. But the footage is all I've got left of that time. If they're still out there, I want \nto find them.",
            }, anomaly_id=anomaly_id)

class Ghouster(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Ghouster",
            backstory="Your ex-lover, who broke up with you 2 weeks before the pandemic. They settled near their \nold school with their circle of friends and never got the chance to go home to \ntheir families because of the deadly virus. They are searching for the people they've lost, \nand also seeking help and refuge.",
            appearance="A young adult wearing a faded school varsity jacket over a plain shirt, worn jeans, \nand scuffed shoes. Their patched backpack holds a water bottle.",
            dialogues={
                1: "From our old school. Remember that place? My friends and I stayed there when the outbreak \nstarted. We thought we'd be safe there, at least until things settled down. Guess we \nwere a little too optimistic.",
                2: "I know I probably shouldn't be asking you for anything, considering how we left things. \nBut I really need somewhere safe to stay. I'm not here to cause you trouble.",
                3: "Nothing, I think. I've been tired, probably from walking around all day. Why? Are you asking \nbecause of your job, or are you actually worried about me? Sorry. Bad joke. I guess \nold habits die hard.",
                4: "I was at school with my friends. We were just finishing up some lab work before heading \nhome. I kinda wish we got to talk before everything went down.",
                5: "No. I'm still looking for my friends and my family. Didn't expect to see you here, though... \nhaha guess we're really not getting rid of each other that easily?",
            }, anomaly_id=anomaly_id,)






# Test dito:

if __name__ == "__main__":

    question = questions[1]
    person = Pandemic_Survivor_1(anomaly_id=1) #Define the person first. Call <Character_name>(anomaly_id) to define the character. anomaly_id is set to None if the character is not an anomaly. Once defined, assign it to a variable.

    person.character_encounter("Pandemic Survivor 1", START_SANITY) #Call methods/functions using the syntax object_variable.method(*arguments)
