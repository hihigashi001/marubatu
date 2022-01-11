from masu import Masu
from player import Player

win_patern = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6],
]

class Game:
    def __init__(self):
        self._winner_message = ""
        self._masu = Masu()
        self._player = Player()

    def game_start(self):
        self._masu.print()
        while (self._winner_message == ""):
            if (self._player.is_cpu()):
               self._cpu_play()
            else:
                self._one_play()
            if (self._winner_message != ""):
                break

    def _one_play(self):
        masu_id = input(f'{self._player.get_teban()} さん、マスを選んでください : ')
        for i in range(9):
            range9 = str(i + 1)
            if (masu_id == range9):
                if (self._masu.get(i) != range9):
                    print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
                else:
                    self._masu.write(int(masu_id), self._player.get_teban())
                    self._hantei()
                    self._player.write(masu_id)
                    self._masu.print()
                    print(self._winner_message)
    
    def _cpu_play(self):
        masu_id = self._win_logic1()
        if masu_id == None:
            masu_id = self._win_logic2()
        if masu_id == None:
            masu_id = self._win_logic3()
        self._masu.write(int(masu_id), self._player.get_teban())
        self._hantei()
        self._player.write(masu_id)
        self._masu.print()
        print(self._winner_message)

    def _hantei(self):
        if (self._masu.end_check()):
            self._winner_message = "引き分けです。"
        for win in win_patern:
            if (self._masu.get(win[0]) == self._masu.get(win[1]) == self._masu.get(win[2])):
                self._winner_message = self._player.get_teban() + " の勝ちです。"
                
                
    def _win_logic1(self):
        for win in win_patern:
            win_array = [self._masu.get(win[0]), self._masu.get(win[1]), self._masu.get(win[2])]
            if (win_array.count(self._player._player2) == 2) and (win_array.count(self._player._player1) != 1):
                for number in win_array:
                    if (number != self._player._player2):
                        return number
                    
    def _win_logic2(self):
        for win in win_patern:
            win_array = [self._masu.get(win[0]), self._masu.get(win[1]), self._masu.get(win[2])]
            if (win_array.count(self._player._player1) == 2) and (win_array.count(self._player._player2) != 1):
                for number in win_array:
                    if (number != self._player._player1):
                        return number
                    
    def _win_logic3(self):
        stolong_number = [ 5, 1, 3, 7, 9, 2, 4, 6, 8]
        for number in stolong_number:
            if (self._masu.get(number - 1) == str(number)):
                return number
