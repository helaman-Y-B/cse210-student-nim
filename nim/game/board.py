import random

# TODO: Define the Board class here


class Board:
    def __init__(self) -> None:
        self._piles = []

    def apply(self):
        """The apply method applies a move to the playing surface. In this case, that means removing a number of stones from a pile. The apply method accepts one argument, an instance of Move."""

        # You will need to separate each 'o' inside the list
        if self.choice == '1':
            self._piles[0] = 'o'*self.user_play
        elif self.choice == '2':
            self._piles[1] = 'o'*self.user_play
        elif self.choice == '3':
            self._piles[2] = 'o'*self.user_play
        elif self.choice == '4':
            self._piles[3] = 'o'*self.user_play
        elif self.choice == '5':
            self._piles[4] = 'o'*self.user_play
        else:
            print("There is no corresponding number")

    def is_empty(self):
        """The is_empty method determines if all the stones have been removed from the board. It returns True if the board has no stones on it; false if otherwise."""

        if self._piles[0] and self._piles[1] and self._piles[2] and self._piles[3] and self._piles[4] == '':
            return True
        else:
            return False

    def to_string(self):
        """The to_string method converts the board data to its string representation and returns it to the caller."""
        return print(
            f"1:{self._piles[0]}\n2:{self._piles[1]}\n3:{self._piles[2]}\n4:{self._piles[3]}\n5:{self._piles[4]}")

    def _prepare(self):
        """The _prepare method sets up the board with a random number of piles (2 - 5) containing a random number of stones (1 - 9)."""
        piles = random.randint(2, 5)
        for i in range(piles):
            self._piles.append(str(i))
