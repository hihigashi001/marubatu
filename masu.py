class Masu:
    def __init__(self):
        self._masu1 = "1"
        self._masu2 = "2"
        self._masu3 = "3"
        self._masu4 = "4"
        self._masu5 = "5"
        self._masu6 = "6"
        self._masu7 = "7"
        self._masu8 = "8"
        self._masu9 = "9"

    def write(self, masu_id, player):
        if (masu_id == "1"):
            if (self._masu1 != "1"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu1 = player
        if (masu_id == "2"):
            if (self._masu2 != "2"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu2 = player
        if (masu_id == "3"):
            if (self._masu3 != "3"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu3 = player
        if (masu_id == "3"):
            if (self._masu3 != "3"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu3 = player
        if (masu_id == "4"):
            if (self._masu4 != "4"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu4 = player
        if (masu_id == "5"):
            if (self._masu5 != "5"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu5 = player
        if (masu_id == "6"):
            if (self._masu6 != "1"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu6 = player
        if (masu_id == "7"):
            if (self._masu7 != "7"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu7 = player
        if (masu_id == "8"):
            if (self._masu8 != "8"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu8 = player
        if (masu_id == "9"):
            if (self._masu9 != "9"):
                print(f'[ {masu_id} ]番は、すでに入力されています。別の場所を選択してください。')
            else:
                self._masu9 = player

    def print(self):
        print('')
        print(f'{self._masu1}  {self._masu2}  {self._masu3}')
        print(f'{self._masu4}  {self._masu5}  {self._masu6}')
        print(f'{self._masu7}  {self._masu8}  {self._masu9}')
        print('')
