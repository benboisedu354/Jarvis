class JarvisState:
    def __init__(self):
        self.running = True
        self.active = False  # wake word

state = JarvisState()

def sleep():
    state.active = False

def wake():
    state.active = True

def is_awake():
    return state.active