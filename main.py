import pygame
import pygame_gui
import sys
import random
import time
from pygame import mixer
import os

pygame.init()
mixer.init()
mixer.Channel(0).play(pygame.mixer.Sound("Wii Theme.mp3"),loops=-1)
time.sleep(0.15)
mixer.Channel(1).play(pygame.mixer.Sound("Wii Theme.mp3"),loops=-1)

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))


class Step:
    def __init__(self):
        self.manager = pygame_gui.UIManager((800, 600))
    
    def run(self, window_surface: pygame.Surface, delta: float) -> bool:
        return False


class Continue(Step):
    def __init__(self, i):
        super().__init__()
        self.done = False
        self.continue_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((0, 0), (200, 50)),
            text='Continue',
            manager=self.manager,
        );
        self.i = i

    def run(self, window_surface, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            self.manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                # UI Events
                if event.ui_element == self.continue_btn:
                    self.done = True
                    print('Continuing ' + str(self.i))

        self.manager.update(delta)

        self.manager.draw_ui(window_surface)
        return self.done

class HighLow(Step):
    def __init__(self):
        super().__init__()
        self.done = False
        self.text = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((0, -50), (300, 50)),
            text='Enter your favourite number',
            manager=self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )
        self.input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((0, 0), (100, 50)),
            manager=self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )
        self.number = random.randint(0, 100)

    def run(self, window_surface, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            self.manager.process_events(event)

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                guess = int(self.input.get_text())      # make it not crash later
                if guess == self.number:
                    self.done = True
                if guess < self.number:
                    self.text.set_text("Higher")
                if guess > self.number:
                    self.text.set_text("Lower")


        self.manager.update(delta)

        self.manager.draw_ui(window_surface)
        return self.done

    
class Birthday(Step):
    def __init__(self):
        super().__init__()
        
        self.birthday_days = ["Eight", "Eighteen", "Eleven", "Fifteen", "Five", "Four", "Fourteen", "Nine", "Nineteen", "One", "Seven", "Seventeen", "Six", "Sixteen", "Ten", "Thirteen", "Thirty", "Thirty-one", "Three", "Twelve", "Twenty", "Twenty-eight", "Twenty-five", "Twenty-four", "Twenty-nine", "Twenty-one", "Twenty-seven", "Twenty-six", "Twenty-three", "Twenty-two", "Two"]
        self.birthday_months = ["April", "August", "December", "February", "January", "July", "June", "March", "May", "November", "October", "September"]
        self.birthday_years = ["Nineteen eighty", "Nineteen eighty-eight", "Nineteen eighty-five", "Nineteen eighty-four", "Nineteen eighty-nine", "Nineteen eighty-one", "Nineteen eighty-seven", "Nineteen eighty-six", "Nineteen eighty-three", "Nineteen eighty-two", "Nineteen ninety", "Nineteen ninety-eight", "Nineteen ninety-five", "Nineteen ninety-four", "Nineteen ninety-nine", "Nineteen ninety-one", "Nineteen ninety-seven", "Nineteen ninety-six", "Nineteen ninety-three", "Nineteen ninety-two", "Nineteen seventy", "Nineteen seventy-eight", "Nineteen seventy-five", "Nineteen seventy-four", "Nineteen seventy-nine", "Nineteen seventy-one", "Nineteen seventy-seven", "Nineteen seventy-six", "Nineteen seventy-three", "Nineteen seventy-two", "Two thousand", "Two thousand eight", "Two thousand eighteen", "Two thousand eleven", "Two thousand fifteen", "Two thousand five", "Two thousand fourteen", "Two thousand four", "Two thousand nineteen", "Two thousand one", "Two thousand seven", "Two thousand seventeen", "Two thousand six", "Two thousand sixteen", "Two thousand ten", "Two thousand thirteen", "Two thousand three", "Two thousand twelve", "Two thousand twenty", "Two thousand twenty-five", "Two thousand twenty-four", "Two thousand twenty-one", "Two thousand twenty-three", "Two thousand twenty-two", "Two thousand two"]
        random.shuffle(self.birthday_days)
        random.shuffle(self.birthday_months)
        random.shuffle(self.birthday_years)

        self.birthday_days_text = pygame_gui.elements.UILabel(text="Enter your date of birth.", relative_rect=pygame.Rect((0, -240), (250, 50)), manager = self.manager, anchors={'centerx': 'centerx', 'centery' : 'centery'})
        self.birthday_days_text = pygame_gui.elements.UILabel(text="Day", relative_rect=pygame.Rect((0, -177), (250, 50)), manager = self.manager, anchors={'centerx': 'centerx', 'centery' : 'centery'})
        self.birthday_months_text = pygame_gui.elements.UILabel(text="Month", relative_rect=pygame.Rect((0, -97), (250, 50)), manager = self.manager, anchors={'centerx': 'centerx', 'centery' : 'centery'})
        self.birthday_years_text = pygame_gui.elements.UILabel(text="Year", relative_rect=pygame.Rect((0, -17), (250, 50)), manager = self.manager, anchors={'centerx': 'centerx', 'centery' : 'centery'})

        self.birthday_days_entry = pygame_gui.elements.UIDropDownMenu(options_list=self.birthday_days, relative_rect=pygame.Rect((0, -140), (250, 50)), manager = self.manager, starting_option="Eight", anchors={'centerx': 'centerx', 'centery' : 'centery'}, expansion_height_limit=200)
        self.birthday_months_entry = pygame_gui.elements.UIDropDownMenu(options_list=self.birthday_months, relative_rect=pygame.Rect((0, -60), (250, 50)), manager = self.manager, starting_option="April", anchors={'centerx': 'centerx', 'centery' : 'centery'}, expansion_height_limit=200)
        self.birthday_years_entry = pygame_gui.elements.UIDropDownMenu(options_list=self.birthday_years, relative_rect=pygame.Rect((0, 20), (250, 50)), manager = self.manager, starting_option="Nineteen eighty", anchors={'centerx': 'centerx', 'centery' : 'centery'}, expansion_height_limit=200)
        
        self.done_button =  pygame_gui.elements.UIButton(text="Continue", relative_rect=pygame.Rect((0, 150), (100, 50)), manager = self.manager, anchors={'centerx': 'centerx', 'centery' : 'centery'})

        self.done = False

    def run(self, window_surface, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            self.manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                # UI Events
                if event.ui_element == self.done_button:
                    self.done = True

        self.manager.update(delta)

        self.manager.draw_ui(window_surface)
        return self.done

class Username(Step):
    def __init__(self):
        super().__init__()
        self.done = False
        self.text = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((0, -50), (300, 50)),
            text="Enter your Username",
            manager=self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )
        self.input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((0, 0), (200, 50)),
            manager=self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )
        self.usernames = []

    def run(self, window_surface, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            self.manager.process_events(event)

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                username = self.input.get_text()
                if self.usernames.__contains__(username):
                    self.text.set_text("Username Has already been used")
                elif len(self.usernames) < 5:
                    self.text.set_text("Username Has already been used")
                    self.usernames.append(username)
                else:
                    self.done = True


        self.manager.update(delta)

        self.manager.draw_ui(window_surface)
        return self.done


class MaidenName(Step):
    def __init__(self):
        super().__init__()
        self.done = False
        self.text = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((0, -50), (300, 50)),
            text="Enter your second pet's maiden name.",
            manager=self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )
        self.input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((0, 0), (200, 50)),
            manager=self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )
        self.usernames = []

    def run(self, window_surface, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            self.manager.process_events(event)

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                self.done = True


        self.manager.update(delta)

        self.manager.draw_ui(window_surface)
        return self.done

class Pi(Step):
    def __init__(self):
        super().__init__()
        self.done = False
        self.text = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((300, 225), (200, 50)),
            text='Enter Pi to 100 digits',
            manager=self.manager,
        )
        self.input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((350, 275), (100, 50)),
            manager=self.manager,
        )
        self.pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

    def run(self, window_surface, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            self.manager.process_events(event)

            if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                # UI Events
                if event.ui_element == self.input:
                    length = len(self.input.get_text())
                    if length == 102 and self.input.get_text() == self.pi:
                        self.done = True
                    elif (length - 2) % 10 == 0:
                        if self.input.get_text() == self.pi[:length]:
                            print("yes")
                        else:
                            print("no")

        self.manager.update(delta)

        self.manager.draw_ui(window_surface)
        return self.done

class FinishSignUp(Step):
    def __init__(self):
        super().__init__()
        self.done_button =  pygame_gui.elements.UIButton(text="Finish sign-up!", relative_rect=pygame.Rect((350, 300), (120, 50)), manager = self.manager)
        self.timer_time = 6
        self.timer = -1
        self.done = False
    
    def run(self, window_surface, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            self.manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_ON_HOVERED:
                self.timer = self.timer_time

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                # UI Events
                if event.ui_element == self.done_button:
                    self.done = True

        if self.timer > 0:
            self.timer -= 1
        elif self.timer ==0:
            randomx = random.randint(0, 700)
            randomy = random.randint(0, 550)
            mouse_x, mouse_y = pygame.mouse.get_pos()

            while mouse_x in range(randomx, randomx + 120):
                randomx = random.randint(0, 700)
            while mouse_y in range(randomy, randomy + 50):
                randomy = random.randint(0, 550)

            self.done_button.set_relative_position((randomx, randomy))
            self.timer = -1


        self.manager.update(delta)

        self.manager.draw_ui(window_surface)
        return self.done

class Colourblind(Step):
    def __init__(self):
        super().__init__()
        self.done = False

        self.text = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((0, -150), (300, 50)),
            text="Prove you're not colourblind.",
            manager=self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )
        self.input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((0, -100), (200, 50)),
            manager=self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )

        self.colourblind_image = pygame.image.load('colourblind.png')
        #self.colourblind_image = pygame.transform.scale_by(self.colourblind_image, 0.25)
        
    
    def run(self, window_surface, delta):
        window_surface.blit(self.colourblind_image, (250,250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.manager.process_events(event)

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                answer = self.input.get_text()
                if answer != "74":
                    pass#self.text.text_colour=pygame.Color("#FF0000")
                else:
                    self.done = True

        self.manager.update(delta)

        self.manager.draw_ui(window_surface)
        return self.done
    

class Captcha(Step):
    def __init__(self):
        super().__init__()
        self.done = False

        self.text = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((0, -150), (300, 50)),
            text="Prove you're not a robot.",
            manager=self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )
        self.input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((0, -100), (200, 50)),
            manager=self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )

        self.captcha_image = pygame.image.load('captcha.png')
        
        
    
    def run(self, window_surface, delta):
        window_surface.blit(self.captcha_image, (110,260))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.manager.process_events(event)

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                answer = self.input.get_text()
                if answer != "Td4eva":
                    pass#self.text.text_colour=pygame.Color("#FF0000")
                else:
                    self.done = True

        self.manager.update(delta)

        self.manager.draw_ui(window_surface)
        return self.done
    
class Password(Step):
    def __init__(self):
        super().__init__()
        self.done = False
        self.text = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((0, -50), (500, 50)),
            text="Enter your Password",
            manager=self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )
        self.input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((0, 0), (200, 50)),
            manager=self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )
        self.password = ''

    def run(self, window_surface, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            self.manager.process_events(event)

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                password = self.input.get_text()
                if not any(char.isdigit() for char in password):
                    self.text.set_text("Password must contain a number.")
                elif all(char.isalnum() for char in password):
                    self.text.set_text("Password must contain a special character.")
                elif '?' not in password:
                    self.text.set_text("Password must contain a specific special character.")
                else:
                    self.done = True


        self.manager.update(delta)

        self.manager.draw_ui(window_surface)
        return self.done


class Calculus(Step):
    def __init__(self):
        super().__init__()
        self.done = False

        self.text = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((0, -150), (300, 50)),
            text="Prove yourself worthy.",
            manager=self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )
        self.input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((0, -100), (200, 50)),
            manager=self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )

        self.calculus_image = pygame.image.load('calculus.png')
        
        
    
    def run(self, window_surface, delta):
        window_surface.blit(self.calculus_image, (210,270))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.manager.process_events(event)

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                answer = self.input.get_text()
                if answer != "3":
                    pass#self.text.text_colour=pygame.Color("#FF0000")
                else:
                    self.done = True

        self.manager.update(delta)

        self.manager.draw_ui(window_surface)
        return self.done

clock = pygame.time.Clock()

step = 0
steps = [
    Username(),
    Password(),
    Captcha(),
    Colourblind(),
    Calculus(),
    HighLow(),
    Birthday(),
    MaidenName(),
    Pi(),    
    FinishSignUp()
]

manager = pygame_gui.UIManager((800, 600))
pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((350, 275), (100, 50)),
    text='Well Done!!',
    manager=manager,
)
pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((300, 325), (200, 50)),
    text='Now please Login',
    manager=manager,
)

while True:
    time_delta = clock.tick(60)/1000.0

    window_surface.blit(background, (0, 0))

    if step < len(steps):
        if steps[step].run(window_surface, time_delta):
            step += 1
    else:
        manager.update(time_delta)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            manager.process_events(event)

        manager.draw_ui(window_surface)

    pygame.display.update()

