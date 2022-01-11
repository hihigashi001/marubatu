from masu import Masu
from player import Player

class Game:
    def __init__(self):
        self._winner_message = ""
        self._masu = Masu()
        self._player = Player()

    def game_start(self):
        self._masu.print()
        while (self._winner_message == ""):
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

    def _hantei(self):
        retu_row1 = [self._masu.get(0), self._masu.get(1), self._masu.get(2)]
        retu_row2 = [self._masu.get(3), self._masu.get(4), self._masu.get(5)]
        retu_row3 = [self._masu.get(6), self._masu.get(7), self._masu.get(8)]
        retu_cal1 = [self._masu.get(0), self._masu.get(3), self._masu.get(6)]
        retu_cal2 = [self._masu.get(1), self._masu.get(4), self._masu.get(7)]
        retu_cal3 = [self._masu.get(2), self._masu.get(5), self._masu.get(8)]
        retu_naname1 = [self._masu.get(0), self._masu.get(4), self._masu.get(8)]
        retu_naname2 = [self._masu.get(2), self._masu.get(4), self._masu.get(6)]

        if (self._masu.end_check()):
            self._winner_message = "引き分けです。"

        if (retu_row1[0] == retu_row1[1] == retu_row1[2]):
            self._winner_message = self._player.get_teban() + " の勝ちです。"
        
        if (retu_row2[0] == retu_row2[1] == retu_row2[2]):
            self._winner_message = self._player.get_teban() + " の勝ちです。"
        
        if (retu_row3[0] == retu_row3[1] == retu_row3[2]):
            self._winner_message = self._player.get_teban() + " の勝ちです。"
        
        if (retu_cal1[0] == retu_cal1[1] == retu_cal1[2]):
            self._winner_message = self._player.get_teban() + " の勝ちです。"
        
        if (retu_cal2[0] == retu_cal2[1] == retu_cal2[2]):
            self._winner_message = self._player.get_teban() + " の勝ちです。"
        
        if (retu_cal3[0] == retu_cal3[1] == retu_cal3[2]):
            self._winner_message = self._player.get_teban() + " の勝ちです。"
        
        if (retu_naname1[0] == retu_naname1[1] == retu_naname1[2]):
            self._winner_message = self._player.get_teban() + " の勝ちです。"
        
        if (retu_naname2[0] == retu_naname2[1] == retu_naname2[2]):
            self._winner_message = self._player.get_teban() + " の勝ちです。"
