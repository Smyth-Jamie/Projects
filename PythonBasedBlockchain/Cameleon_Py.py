class Cameleon:
    reset = "\033[0m"
    bold = "\033[01m"
    disable = "\033[02m"
    underline = "\033[04m"
    reverse = "\033[07m"
    strikethrough = "\033[09m"
    invisible = "\033[08m"

    class txt:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

        colourDICT = {
            'black': black,
            'red': red,
            'green': green,
            'orange': orange,
            'blue': blue,
            'purple': purple,
            'cyan': cyan,
            'lightgrey': lightgrey,
            'darkgrey': darkgrey,
            'lightred': lightred,
            'lightgreen': lightgreen,
            'yellow': yellow,
            'lightblue': lightblue,
            'pink': pink,
            'lightcyan':lightcyan
        }

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'
        dict = {
            'Black': black,
            'Red': red,
            'Green': green,
            'Orange': orange,
            'Blue': blue,
            'Purple': purple,
            'Cyan': cyan,
            'LightGrey': lightgrey
        }

        def change(self, string):
            if string in self.dict:
                return self.dict[string]

    def __init__(self):
        default_txt = self.txt.lightgrey
        default_bg = self.bg.black
        print('Remember txt = text , bg = background')
        print(default_txt, default_bg)

    def change_txt(self, colour):
        return self.txt.colourDICT[colour]

    def change_bg(self, colour):
        return self.bg.dict[colour]

lines = Cameleon()
print(lines.change_bg('Red'),  lines.bold, lines.underline, lines.strikethrough, lines.change_txt('green'), 'hello', lines.change_txt('black'), 'world!')
