class Masu:
    def __init__(self):
        self._masu = [str(i+1) for i in range(9)]

    def get(self, masu_id: int):
        return self._masu[masu_id]

    def write(self, masu_id: int, player: str):
        self._masu[masu_id - 1] = player

    def print(self):
        print('')
        print(f'{self._masu[0]}  {self._masu[1]}  {self._masu[2]}')
        print(f'{self._masu[3]}  {self._masu[4]}  {self._masu[5]}')
        print(f'{self._masu[6]}  {self._masu[7]}  {self._masu[8]}')
        print('')
    
    def end_check(self):
        for i in range(9):
            if self._masu[i] == str(i+1):
                return False
        return True
        

