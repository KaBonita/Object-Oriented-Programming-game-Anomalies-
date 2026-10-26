import time

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
    ANOMALIES = {1: "Delayed Speech",
        2: "Unusual Pallor",
        3: "Irregular Breathing",
        4: "Irregular Tremors",
        5: "Speech Impediment",
        6: "Inappropriate Responses"}

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
# Functions / Methods para sa individuals (Sila Ten n dito)
#_____________________________________________________________

    def answer_question(self, question_id):
        if question_id not in self.dialogues:
            return "Invalid question."

        if question_id in self.asked_questions:
            return "You have already asked this question."

        self.asked_questions.add(question_id)
        response = self.dialogues[question_id]

        # Apply a dialogue anomaly when appropriate.
        if self.anomaly_id == 1:
            time.sleep(3)

        elif self.anomaly_id == 3:
            pass

        elif self.anomaly_id == 4:
            pass

        elif self.anomaly_id == 5:
            pass

        elif self.anomaly_id == 6:
            pass

        return response

    def inspect_appearance(self):
        self.is_inspected = True
        description = self.appearance

        # Apply physical anomaly descriptions when appropriate.
        if self.anomaly_id == 2:
            description += " Their skin is unusually pale."

        elif self.anomaly_id == 4:
            pass

        return description

    def get_anomaly_name(self):
        if self.anomaly_id is None:
            return "No anomaly"

        return self.ANOMALIES.get(self.anomaly_id, "Unknown anomaly")


#_____________________________________________________________
# Characters. Define each subclass of individual as each character
#_____________________________________________________________

class Pandemic_Survivor_1(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Pandemic Survivor 1",
            backstory="Survived the pandemic. Has nowhere to settle in and goes around different places in hopes of finding refuge and someone he/she might know.",
            appearance="A traveller who appears to have been travelling for years. They are wearing a worn-out backpack, and have dark circles under their eyes.",
            dialogues={
                1: "I come from the east, I've been moving from place to place since I left my home. I hope I can finally find a place to stay.",
                2: "I don't have a lot to offer, I just need a shelter to stay in.",
                3: "I've been feeling tired lately, but I guess that's normal when you've been walking for days.",
                4: "In my hometown, everybody was living so peacefully, it was a rather quiet place in the countryside, but everything just fell apart so quickly.",
                5: "Not that I know of, but hopefully I can find somebody I know in there.",
            }, anomaly_id=anomaly_id)

class Walang_Pagkain_Buseng(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Walang Pagkain Buseng",
            backstory="Locked themselves in for months after the pandemic announcement and survived on a huge stock of food and rations. Only went out now because the food ran out, and is going around asking people for rations.",
            appearance="An individual carrying an empty sack, they look visibly undernourished and is wearing old dusty house clothes.",
            dialogues={
                1: "My house. I haven't left that place in months. I thought my supplies would last, but I guess I overestimated.",
                2: "Because I'm hungry! I've got nothing left to eat. I'm just looking for food and somewhere safe.",
                3: "Unusual? I'm starving! I've barely eaten anything these past few days. What else do you expect?",
                4: "At home. The moment the announcements came out, I locked everything up and stocked as much food as I could.",
                5: "No. I've been alone this entire time. Honestly, I'm just hoping someone here has food to spare.",
            }, anomaly_id=anomaly_id)

class Doctor(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Doctor",
            backstory="Came from the nearest hospital. Desperately tried to find a cure but failed, and ended up in a depressive state, especially since all his colleagues also succumbed to the virus.",
            appearance="Wears an old lab coat which is visibly torn and worn-out, a face mask, and broken glasses.",
            dialogues={
                1: "I came from the hospital but I am unaffected by the virus, I swear.",
                2: "I'm a doctor. I can be of help to anyone who has injuries… even those who have possible symptoms. Although we did not finish the cure, I have studied it enough to at least assist the survivors.",
                3: "No… not as of late, anyway. I don't know, really. Everything is unusual when half of the world's population is gone because of the outbreak.",
                4: "The hospital. I was working. We experienced the first surge of patients, how they panicked, how everyone was dying right in front of my eyes.",
                5: "No. I'm the only one who made it out alive.",
            }, anomaly_id=anomaly_id)

class Politician(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="The Politician",
            backstory="A politician who was well-protected in the comfort of his home. Once he found out people were becoming immune to the virus, he started reaching out to the nearest survivors, building connections and trying to lead the newly established group.",
            appearance="Unlike the other survivors who came before him, he was more well-kept and clean, in a way. The only tell-tale sign that he was ever in a pandemic was the mask on his face. His clothes are clean and simple, hair swept back, and his posture means business.",
            dialogues={
                1: "Do you not know me? I suppose you do not watch the news. I came from the neighboring city.",
                2: "Huh. Nobody has ever asked me that question. I guess you really have no idea who I am. Does this city have a leader? Someone competent enough to lead the citizens? If not, then I see no reason why you should not let me in.",
                3: "I am perfectly fine. What's more unusual is you asking more and more questions.",
                4: "I was at the city hall. I was the one who issued the lockdown announcement. You probably know who I am now?",
                5: "I'm sure everyone is waiting for someone to step up and help them.",
            }, anomaly_id=anomaly_id)

class Bleeding_Love(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Bleeding Love",
            backstory="Lost the love of their life, and is unsure whether said significant other is dead or simply lost, since they were separated during the \"hoarding incidents\" where people ransacked all the stores. After gaining immunity, they are deadset on finding their significant other.",
            appearance="A person with intensely swollen eyes yet is still in the middle of crying. He is at his most vulnerable and disheveled state, carrying nothing but a locket with a picture of a person that he is desperately trying to find.",
            dialogues={
                1: "I came from nearby, but I have been going around, I'm trying to find someone… Have you seen them?",
                2: "I need to find someone. I need to know if she's inside, please, I don't know where she went after we got separated during the hoarding incident in our city. I can only hope that she is safe inside this city.",
                3: "Nothing… I don't care what's happening to me. I need to know what happened to her.",
                4: "We were together. We were outside. We immediately looked for refuge. I don't clearly remember where, all that was important to me at that time was that we were together.",
                5: "Her… she might be waiting for me inside. I promised her that I'll find her no matter what, that we will be together forever.",
            }, anomaly_id=anomaly_id)

class Dorothea(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Dorothea",
            backstory="The player's old friend from high school. She moved to a different city but ended up back here when her local government unit tried to transfer/evacuate citizens to other sites due to lack of resources. She does not know anyone in the neighborhood and is trying to find help.",
            appearance="A student still wearing her uniform, worn-out shoes, and carries a black backpack. Her hair is tied up in a messy bun, with strands of hair covering her face which was also stained with dirt and dust. She is awfully familiar to the player, a face that you have not seen in a long, long time.",
            dialogues={
                1: "Oh… I don't know how I got here. We were transferred from our city, but I didn't think we'd end up here. When I woke up, I was surprised as well. The only familiar face I know is you, so..",
                2: "All of the people I was with suddenly disappeared. I have no idea what to do and where to go. I was hoping that you—or, people here can help me.",
                3: "Nope. I'm perfectly fine. I've been regularly taking the vitamins they gave us from back home.",
                4: "Ah… I was at school. I ended up staying there for the entirety of the lockdown until we ran out of supplies and we had to get transferred to a different site.",
                5: "Maybe? I was with a group, so, there's a chance that they found this place before I did and they're already inside.",
            }, anomaly_id=anomaly_id)

class Bata_Bata(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Bata, Bata",
            backstory="A random kid who lost his parents and is trying to find them. Owns a small teddy bear, the last thing he can remember of his parents. Thinks the player is his mother/father and is crying at their doorstep because he is mad that his parents left him to get food.",
            appearance="An awfully malnourished kid wearing tattered clothes, holding the arm of a dirty teddy bear. He looks like someone around the age of 5 or 6, with eyes that are on the verge of tears. His feet are bare and both his arms are covered in soot.",
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
            backstory="A vendor already trying to earn a profit early in the post-pandemic period. One of the people hit by the economic crisis caused by the virus, and desperate to regain all of her past businesses.",
            appearance="A short-haired woman wearing a faded graphic shirt, knee-length denim shorts, and slippers. She has a small towel draped over one shoulder and a worn waist pouch. Her clothes have a few stains of iskrambol.",
            dialogues={
                1: "From the market near the highway. I was trying to sell some stuff there, but barely anyone was buying.",
                2: "I can help out around here, too. Just need somewhere safe to stay.",
                3: "Unusual? Nah. I'm just tired. Haven't had a decent night's sleep since the outbreak started.",
                4: "At my stall, selling iskrambol near the school. One minute, people were buying snacks; the next, everyone was running for their lives. I had to leave everything behind.",
                5: "No. Just me. I used to have a proper business before all this happened. Lost everything, and now I'm back to selling whatever I can find.",
            }, anomaly_id=anomaly_id)

class Hi_Vlog_Welcome_To_My_Guys(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Hi Vlog Welcome To My Guys",
            backstory="An influencer before the pandemic who documented life during the outbreak, with recordings of living underground, looking for food, and who they were with whenever they evacuated. After gaining immunity, they started vlogging again, going around interviewing people about their livelihood and how they survived.",
            appearance="A young man in his early 20s wearing an oversized hoodie. A digital camera hangs from his neck. His hair is unevenly cut, and there are dark circles under his eyes.",
            dialogues={
                1: "What's up, guys- okay sorry force of habit. Just came from one of the underground shelters downtown. I stayed there for a long time, but food was running out.",
                2: "Look, I've got recordings of places I've been to, evacuation routes, shelters, supply locations, all kinds of stuff. I can show you what I found. Might even help you locate other survivors. And hey, if you're okay with it, maybe I could document how this settlement is rebuilding. History's gotta be recorded, right?",
                3: "Well, I got sick a while back, but somehow I recovered. People started saying I might be immune. I feel mostly fine now, though. I mean, I'm exhausted, my sleep schedule is completely destroyed, and my hair looks like I cut it with a spoon, but that's not exactly newsworthy.",
                4: "At home, recording a video. I was doing one of those ordinary daily vlogs, you know, food, random stuff, talking about my day. Then people started evacuating, and suddenly I was recording something nobody could've prepared for. At first, I thought I'd document everything until things went back to normal. Didn't realize how long I'd be waiting.",
                5: "Not that I know of. I got separated from my group while we were moving between shelters. I've replayed my recordings so many times, looking for familiar faces or clues about where they went. Sometimes I wonder if I should've put the camera down and just stayed with them. But the footage is all I've got left of that time. If they're still out there, I want to find them.",
            }, anomaly_id=anomaly_id)

class Ghouster(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Ghouster",
            backstory="Your ex-lover, who broke up with you 2 weeks before the pandemic. They settled near their old school with their circle of friends and never got the chance to go home to their families because of the deadly virus. They are searching for the people they've lost, and also seeking help and refuge.",
            appearance="A young adult wearing a faded school varsity jacket over a plain shirt, worn jeans, and scuffed shoes. Their patched backpack holds a water bottle.",
            dialogues={
                1: "From our old school. Remember that place? My friends and I stayed there when the outbreak started. We thought we'd be safe there, at least until things settled down. Guess we were a little too optimistic.",
                2: "I know I probably shouldn't be asking you for anything, considering how we left things. But I really need somewhere safe to stay. I'm not here to cause you trouble.",
                3: "Nothing, I think. I've been tired, probably from walking around all day. Why? Are you asking because of your job, or are you actually worried about me? Sorry. Bad joke. I guess old habits die hard.",
                4: "I was at school with my friends. We were just finishing up some lab work before heading home. I kinda wish we got to talk before everything went down.",
                5: "No. I'm still looking for my friends and my family. Didn't expect to see you here, though…haha guess we're really not getting rid of each other that easily?",
            }, anomaly_id=anomaly_id,)

# Test dito:
question = questions[1]
person = Pandemic_Survivor_1(anomaly_id=1)

print(question)
print("\nPandemic Survivor 1:")
print(person.answer_question(1))
print("\nAnomly type:")
print(person.get_anomaly_name())