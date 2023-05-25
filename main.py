import random

class ghost():

    def __init__(self, ans = None, count=0, life = 3) -> None:
        self.ans = ans
        self.life = life
        self.count = count
        pass

    def getCountry(self):     
        with open("countries.txt", "r") as fh:
            self.words = fh.read().split("\n")
        while True:
            self.word = random.choice(self.words).replace("\n", "")
            if self.tempMemory(self.word):
                return self.word, [x for x in self.words if (x.startswith(self.word[0]) and x != self.word and self.tempMemory(x))]
        
    def tempMemory(self, new):
        with open("history.txt", "w+") as history_fh:
            temp_words = history_fh.read().split("\n")
        if self.word == None: pass
        else:
            for i in temp_words:
                if i == new: return False
            return True

    def history(self, old=""):
        with open("history.txt", "w+") as history_fh: pass
        if old == None: pass
        elif old == "terminate": history_fh.write()
        else: history_fh.write(old)

    def motivation(self, num):
        if num > 0: return "Great!"
        else: return "You can do better!"

    def game(self):
        test_word, alt_list = ghost.getCountry()

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


