class dimmer_switch():
    def __init__(self):
        self.switch_is_on = False
        self.brightness = 0
    
    def turn_on(self):
        self.switch_is_on = True

    def turn_off(self):
        self.switch_is_on = False
    
    def raise_level(self):
        if self.brightness < 10:
            self.brightness += 1

    def lower_level(self):
        if self.brightness > 0:
            self.brightness -= 1
    
    # This method reserved for debugging
    def show(self):
        print(f'Switch is on? {self.switch_is_on}')
        print(f'Brightness is: {self.brightness}')

# Main code
obj_dimmer = dimmer_switch()

# Turn switch on, raise level 5 times
obj_dimmer.turn_on()
obj_dimmer.raise_level()
obj_dimmer.raise_level()
obj_dimmer.raise_level()
obj_dimmer.raise_level()
obj_dimmer.raise_level()
obj_dimmer.show()

# Lower level 2 times, turn switch off
obj_dimmer.lower_level()
obj_dimmer.lower_level()
obj_dimmer.turn_off()
obj_dimmer.show()

# Turn switch on, raise level 3 times
obj_dimmer.turn_on()
obj_dimmer.raise_level()
obj_dimmer.raise_level()
obj_dimmer.raise_level()
obj_dimmer.show()