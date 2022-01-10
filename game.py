from masu import Masu
from player import Player

class Game:
    def __init__(self):
        self._retu_row1 = []
        self._retu_row2 = []
        self._retu_row3 = []
        self._retu_cal1 = []
        self._retu_cal2 = []
        self._retu_cal3 = []
        self._retu_naname1 = []
        self._retu_naname2 = []
        self._syouhai = ""
        self._masu = Masu()
        self._player = Player()

    def game_start(self):
        self._one_play()
        self._one_play()
        self._one_play()

    def _one_play(self):
        masu_id = input(f'{self._player.print_teban()} さん、マスを選んでください : ')
        if (masu_id == "1"):
            if (self._masu._masu1 != "1"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu.write(masu_id, self._player.print_teban())
                self._player.write(masu_id)
                self._masu.print()
        if (masu_id == "2"):
            if (self._masu._masu2 != "2"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu.write(masu_id, self._player.print_teban())
                self._player.write(masu_id)
                self._masu.print()
        if (masu_id == "3"):
            if (self._masu._masu3 != "3"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu.write(masu_id, self._player.print_teban())
                self._player.write(masu_id)
                self._masu.print()
        if (masu_id == "4"):
            if (self._masu._masu4 != "4"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu.write(masu_id, self._player.print_teban())
                self._player.write(masu_id)
                self._masu.print()
        if (masu_id == "5"):
            if (self._masu._masu5 != "5"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu.write(masu_id, self._player.print_teban())
                self._player.write(masu_id)
                self._masu.print()
        if (masu_id == "6"):
            if (self._masu._masu6 != "6"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu.write(masu_id, self._player.print_teban())
                self._player.write(masu_id)
                self._masu.print()
        if (masu_id == "7"):
            if (self._masu._masu7 != "7"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu.write(masu_id, self._player.print_teban())
                self._player.write(masu_id)
                self._masu.print()
        if (masu_id == "8"):
            if (self._masu._masu8 != "8"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu.write(masu_id, self._player.print_teban())
                self._player.write(masu_id)
                self._masu.print()
        if (masu_id == "9"):
            if (self._masu._masu9 != "9"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu.write(masu_id, self._player.print_teban())
                self._player.write(masu_id)
                self._masu.print()

    # def _retu_add(self, masu):

    
    # def _hantei(self, masu):
        





