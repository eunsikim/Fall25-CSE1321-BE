class button:
    def __init__(self, text, link):
        self.background = "black"
        self.background_hover = "grey"
        self.font = "arial"
        self.font_size = 12

        self.text = text
        self.link = link

def main():
    button1 = button("APPLY", "https://www.kennesaw.edu/apply.php")
    button2 = button("VISIT", "https://www.kennesaw.edu/visit.php")
    button3 = button("GIVE", "https://www.kennesaw.edu/give.php")
    button4 = button("CALENDAR", "https://www.kennesaw.edu/calendar.php")
    button5 = button("A-Z INDEX", "https://www.kennesaw.edu/index.php")

    