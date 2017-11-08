def print_noise(self):
        print(self.noise)
class Little_child:
    noise=5
    show_noise=print_noise
    def __init__ (self,noise):
        self.noise=noise
Vasy=Little_child(500)
Vasy.show_noise()




