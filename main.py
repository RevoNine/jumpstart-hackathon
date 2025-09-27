import pygame
import pygame_gui
import sys

pygame.init()

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
            relative_rect=pygame.Rect((350, 275), (100, 50)),
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


clock = pygame.time.Clock()

step = 0
steps = [
    Continue(0),
    Continue(1),
    Continue(2),
    Continue(3),
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

