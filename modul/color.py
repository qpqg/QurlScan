from os import system
class colorku():
    __W = '\033[0m'  # white (default)
    __R = '\033[31m'  # red
    __G = '\033[1;32m'  # green bold
    __O = '\033[33m'  # orange
    __B = '\033[34m'  # blue
    __P = '\033[35m'  # purple
    __C = '\033[36m'  # cyan
    __GR = '\033[37m'  # gray
    __bold = '\033[01m'
    def baleho(self, x, judul=None):
        system("clear")
        print self.dflt_end()
        print self.dflt_G(judul.center(x))
        print self.dflt_R("Qiuby Zhukhi".center(x))
        print self.dflt_O("-=[ PBM TEAM]=-".center(x))
        print self.dflt_end()
    def warning_red(self, text):
        return "{}{}[!] {} [!]{}".format(colorku.__bold, colorku.__R, text, colorku.__W)
    def help_B(self, text):
        return "{}{}[?] {} [?]{}".format(colorku.__bold, colorku.__B, text, colorku.__W)
    def info_G(self, text):
        return "{}{}[!] {} [!]{}".format(colorku.__bold, colorku.__G, text, colorku.__W)
    def info_O(self, text):
        return "{}{}[!] {} [!]{}".format(colorku.__bold, colorku.__O, text, colorku.__W)
    def info_C(self, text):
        return "{}{}[!] {} [!]{}".format(colorku.__bold, colorku.__C, text, colorku.__W)
    def info_GR(self, text):
        return "{}{}[!] {} [!]{}".format(colorku.__bold, colorku.__GR, text, colorku.__W)
    def info_P(self, text):
        return "{}{}[!] {} [!]{}".format(colorku.__bold, colorku.__P, text, colorku.__W)
    def menus_GR(self, text):
        return "{}{}{}{}".format(colorku.__bold, colorku.__O, text, colorku.__W)
    def dflt_G(self, text):
        return "{}{}{}{}".format(colorku.__G, colorku.__bold, text,colorku.__W)
    def dflt_O(self,text):
        return "{}{}{}{}".format(colorku.__O, colorku.__bold, text,colorku.__W)
    def dflt_C(self,text):
        return "{}{}{}{}".format(colorku.__C, colorku.__bold, text,colorku.__W)
    def dflt_GR(self,text):
        return "{}{}{}{}".format(colorku.__GR, colorku.__bold, text,colorku.__W)
    def dflt_P(self,text):
        return "{}{}{}{}".format(colorku.__P, colorku.__bold, text,colorku.__W)
    def dflt_R(self,text):
        return "{}{}{}{}".format(colorku.__R, colorku.__bold, text, colorku.__W)
    def dflt_end(self):
        return "{}{}{}{}".format(colorku.__G, colorku.__bold, "[+]"+"="*34+"[+]", colorku.__W)