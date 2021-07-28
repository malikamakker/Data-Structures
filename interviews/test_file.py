class fruits:
    def __init__(self, name, season):
        self.name = name
        self.season = season

    def good_months(self):
        if check_this(self.season):
            if self.season == "summer":
                return "March-June"
            elif self.season == "winter":
                return "Nov-Jan"
        return False

def check_this(season):
    if season in ["summer", "winter"]:
        return True
    else:
        return False
