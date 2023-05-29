import random

class ghost():
    # AppData = {"temporal":[], "permanent": []}
    def __init__(self, word = None, ans = "", status = True, count=1, life = 3) -> None:
        self.ans = ans.lower()
        self.life = life
        self.count = count
        self.status = status
        self.word = word

    @classmethod
    def pull_data_gameWords(self):
        with open("countries.txt", "r") as fh_countries:
            all_words = fh_countries.read().split("\n")

        with open("history.txt", "r") as fh_history:
            del_words = fh_history.read().split("\n")
        
        ghost.words = [i for i in all_words if i not in del_words]

            

    def getCountry(self):
        if self.status:
            if self.ans == "":
                random.shuffle(ghost.words)
                self.word = random.choice(ghost.words).lower()
                self.status = bool([i for i in ghost.words if i.startswith(self.word[0])])

            else:
                lst = [i for i in ghost.words if i.startswith(self.ans) == self.ans]
                if bool(lst):
                    random.shuffle(lst)
                    self.word = random.choice(lst).lower()

                    if len(lst) <= 2: self.status = False
                    elif len(lst) > 2: self.status = True
                else:
                    self.status = None
    
    def game(self):
        self.getCountry()
        if self.ans == "":
            return self.word, self.word[0].upper(), self.status, self.count, self.life
        else:
            self.count += 2
            if self.word == self.ans:
                self.life += 1
                self.push_data_gameWordsHistory()
                return None, self.motivation(), True, 1, self.life
            
            elif self.word[:self.count] == self.word:
                self.life += 1
                self.push_data_gameWordsHistory()
                return None, self.motivation(), True, 1, self.life
             
            elif self.status == None:
                self.life -= 1
                return None, self.motivation(False), True, 1, self.life
            
            else:
                return self.word, self.word[:self.count].upper(), self.status, self.count, self.life
   
    def push_data_gameWordsHistory(self):
        with open("history.txt", "a+") as fh_history:
            fh_history.write(self.word+"\n")

    def motivation(self, num):
        if num > 0: return "Great!"
        else: return "You can do better!"

    # def game(self):
    #     test_word = ghost.getCountry()

    #     if self.ans == None:
    #         self.count+=1
    #         return test_word[:self.count], self.count, self.life
        
    #     elif test_word.startswith(self.ans):
    #         self.count += 2
    #         try:
    #             return test_word[:self.count], self.count, self.life
    #         except:
    #             if self.ans == test_word: return ghost.motivation(+1), 0, self.life
        
    #     else:
    #         alt_list = [ i for i in alt_list if i.startswith(self.ans)]
    #         if alt_list == []: return test_word+"\n" + ghost.motivation(-1), 0, self.life-1
    #         test_word = random.choice(alt_list)
    #         self.count += 2
    #         try:
    #             return test_word[:self.count], self.count, self.life
    #         except:
    #             if self.ans == test_word: return ghost.motivation(+1), 0, self.life

if __name__ == "__main__":
    player = ghost()
    ghost.pull_data_gameWords()
    word, ans, status, count, life = player.game()
    for x in range(12):
        print(ans)
        l = input()
        ans = ans+l
        player = ghost(word, ans, status, count, life)
        word, ans, status, count, life = player.game()


