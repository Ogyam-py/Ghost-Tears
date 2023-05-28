import random

class ghost():
    AppData = {"temporal":[], "permanent": []}
    words = []
    def __init__(self, ans = None, count=0, life = 3) -> None:
        self.ans = ans
        self.life = life
        self.count = count

    @classmethod
    def loading(self):
        with open("countris.txt", "r") as fh_countries:
            ghost.words.extend(random.shuffle(fh_countries.read().split("\n")))

    def getCountry(self):
        while True:
            if self.ans == "":
                word_range = random.choices(ghost.words, k=5)
            else:
                word_range = random.shuffle([i for i in ghost.words if i.startswith() == self.ans])

            word = random.choice(word_range)
            if word not in ghost.AppData["temporal"] and word not in ghost.AppData["permanent"]:
                return word
            
    
    def gameHistory(self):
        pass

    def motivation(self, num):
        if num > 0: return "Great!"
        else: return "You can do better!"

    def game(self):
        test_word = ghost.getCountry()

        if self.ans == None:
            self.count+=1
            return test_word[:self.count], self.count, self.life
        
        elif test_word.startswith(self.ans):
            self.count += 2
            try:
                return test_word[:self.count], self.count, self.life
            except:
                if self.ans == test_word: return ghost.motivation(+1), 0, self.life
        
        else:
            alt_list = [ i for i in alt_list if i.startswith(self.ans)]
            if alt_list == []: return test_word+"\n" + ghost.motivation(-1), 0, self.life-1
            test_word = random.choice(alt_list)
            self.count += 2
            try:
                return test_word[:self.count], self.count, self.life
            except:
                if self.ans == test_word: return ghost.motivation(+1), 0, self.life

if __name__ == "__main__":
    play = ghost()
    while True:
        ans, count, life = play.game()
        if life > 0:
            l = input(f"Contribute a letter to spell a countries name:\n\t{ans}")
            play = ghost(ans+l, count, life)
        elif count == 0:
            print(ans)
            break


