class Player:
    def __init__(self):
        self._player1 = 'o'
        self._player2 = 'x'
        self._teban = self._player1

    def write(self, masu_number):
        print(f'{self._teban}さんが、{masu_number}を選びました。')
        if (self._teban == self._player1):
            self._teban = self._player2
        else:
            self._teban = self._player1

    def get_teban(self):
        return self._teban