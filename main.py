import pygame
import pygame_gui
import sys
import random
import time
import concurrent.futures
from tkinter import messagebox
import tkinter
from pygame import mixer

channel = 0

pygame.init()
mixer.init()
mixer.Channel(channel).play(pygame.mixer.Sound("Wii Theme.mp3"),loops=-1)
channel += 1
time.sleep(0.15)
mixer.Channel(channel).play(pygame.mixer.Sound("Wii Theme.mp3"),loops=-1)
channel += 1

def poppups():
    while True:
        time.sleep(random.randint(5, 10))
        match random.randint(0, 1):
            case 0:
                pringles()
            case 1:
                error()


def pringles():
    messagebox.showinfo("Important!!!!", "Hot pringles in your area!!")

def error():
    messagebox.showerror("Error", "Missing admin permissions cannot delete system32\nplease run this program as administrator")
    time.sleep(0.1)
    messagebox.showerror("Error", "Missing admin permissions cannot delete system32\nplease run this program as administrator")
    time.sleep(0.1)
    messagebox.showerror("Error", "Missing admin permissions cannot delete system32\nplease run this program as administrator")
    time.sleep(0.1)
    messagebox.showerror("Error", "Missing admin permissions cannot delete system32\nplease run this program as administrator")
    time.sleep(0.1)
    messagebox.showerror("Error", "Missing admin permissions cannot delete system32\nplease run this program as administrator")

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
pool.submit(poppups)

image = None

x_vel = 1
y_vel = 1

def dvd():
    root = tkinter.Tk()
    root.overrideredirect(True)
    root.attributes('-transparentcolor', "white")
    root.wm_attributes("-topmost", True)
    global image
    image = tkinter.PhotoImage(file=r"image.png", width=1100, height=650)
    image = image.subsample(3)
    b = tkinter.Button(root, image=image, borderwidth=0, bg="white", command=root.destroy).pack()

    def update():
        right = 1100 / 3
        bottom = 650 / 3
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        x = root.winfo_x()
        y = root.winfo_y()

        global x_vel
        global y_vel

        if x <= 0:
            x_vel = 1
        if y <= 0:
            y_vel = 1
        if x + right >= width:
            x_vel = -1
        if y + bottom >= height:
            y_vel = -1

        root.geometry(f"+{x + x_vel}+{y + y_vel}")
        root.after(1, update)
    root.after(1, update)
    root.mainloop()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

def close():
    pygame.quit()
    global pool
    pool.shutdown(wait=False)
    sys.exit()

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
                close()
                
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
                close()
                
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
                close()
                
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
                close()
                
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
                close()
                
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
            relative_rect=pygame.Rect((100, 225), (400, 50)),
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
                close()
                
            self.manager.process_events(event)

            if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                # UI Events
                if event.ui_element == self.input:
                    length = len(self.input.get_text())
                    if length == 102 and self.input.get_text() == self.pi:
                        self.done = True
                    elif (length - 2) % 10 == 0:
                        if self.input.get_text() == self.pi[:length]:
                            self.text.set_text("Your doing grate keap going")
                        else:
                            self.text.set_text("at least one of these digits {} is wrong".format(self.input.get_text()[-10:]))

        self.manager.update(delta)

        self.manager.draw_ui(window_surface)
        return self.done

class DVD(Step):
    def __init__(self):
        super().__init__()
        self.done = False

    def run(self, window_surface, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
                
            self.manager.process_events(event)

        self.manager.update(delta)

        self.manager.draw_ui(window_surface)

        dvd()

        return True


clock = pygame.time.Clock()

step = 0
steps = [
    HighLow(),
    Username(),
    Birthday(),
    MaidenName(),
    Pi(),
    DVD(),
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
            if step % 2 == 0:
                mixer.Channel(channel).play(pygame.mixer.Sound("Wii Theme.mp3"),loops=-1)
                channel += 1
    else:
        manager.update(time_delta)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            
            manager.process_events(event)

        manager.draw_ui(window_surface)

    pygame.display.update()

