class Head:
    def __init__(self):
        pass

class Torso:
    def __init__(self,arm,leg,head):
        self.arm = arm
        self.leg =leg
        self.head = head
        

class Arm:
    def __init__(self,hand):
        self.hand = hand

class Hand:
    def __init__(self):
        pass

class Leg:
    def __init__(self,feet):
        self.feet = feet

class Feet:
    def __init__(self):
        pass

class Human:
    def __init__(self,head,torso,):
        self.head = head
        self.torso = torso

hand = Hand()
feet = Feet()
arm = Arm(hand)
leg = Leg(feet)
head = Head()
torso = Torso(arm,leg,head)
human = Human(head,torso)



        
        

        
    


















        





        

    
