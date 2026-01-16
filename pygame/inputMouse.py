import pygame

class Mouse:
    def __init__(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.leftPressed = False
        self.rightPressed = False

    def Update(self):
        self.x, self.y = pygame.mouse.get_pos()
        buttons = pygame.mouse.get_pressed()

        # Detect single clicks
        self.leftClicked = buttons[0] and not self.leftPressed
        self.rightClicked = buttons[2] and not self.rightPressed

        # Update held state
        self.leftPressed = buttons[0]
        self.rightPressed = buttons[2]

    def LeftIsPressed(self) -> bool:
        return self.leftPressed

    def RightIsPressed(self) -> bool:
        return self.rightPressed

    def LeftClicked(self) -> bool:
        return self.leftClicked

    def RightClicked(self) -> bool:
        return self.rightClicked
        
    def GetPos(self):
        return (self.x, self.y)