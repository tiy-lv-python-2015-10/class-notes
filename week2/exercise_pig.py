#Each player rolls the die.  If the die is 1 player forfeits all points for
# turn.  If it is not 1 then player keeps the points and chooses whether
# to roll again.  If the player rolls 1 or stops then the other player
# takes a turn.  First player to 100 wins the game.
import random


class Die:

    def roll(self):
        """
        Randomly picks a number between 1 and 6 to simulate dice roll and
        bring back memories of basement D&D games
        :return: int between 1 and 6
        """
        return random.randint(1, 6)


class Player:

    def __init__(self, name):
        self.die = Die()
        self.name = name
        self.score = 0

    def roll_die(self):
        """
        Player rolls the die
        :return: int of die roll
        """
        roll = self.die.roll()
        print("You rolled a {}".format(roll))
        return roll

    def record_score(self, score):
        self.score = score

    def go_again(self, round_score):
        """
        Asks the player if they would like to roll again
        :return: boolean whether to roll again
        """
        answer = input("Roll again?").lower()
        if answer[0] == 'y':
            return True
        else:
            return False

    def __str__(self):
        return "Name: {}".format(self.name)


class StupidHuman(Player):

    def __init__(self, name):
        super().__init__(name)
        self.score = 50


class StupidAI(Player):
    def go_again(self, round_score):
        return False


class LessStupidAI(Player):
    def go_again(self, round_score):
        if round_score <= 6:
            return True
        else:
            return False


class Turn:

    def __init__(self, player):
        self.player = player
        self.score = 0

    def run(self):
        """
        Runs turn asks player to roll then add score.  Then asks player if they
        want to roll again
        :return: int score of turn
        """
        turn_over = False
        print("It is {}'s turn".format(self.player.name))

        while not turn_over:
            roll = self.player.roll_die()

            if roll == 1:
                self.score = 0
                print("You crapped out")
                turn_over = True

            else:
                self.score += roll
                # Basically turn over is the negative of
                # if they want to go again
                turn_over = not self.player.go_again(self.score)

        print("Your turn has ended with a round score of {}"
              .format(self.score))
        return self.score


class Game:

    def __init__(self, player1, player2):
        """
        Player1 set to current player by default
        :param player1:
        :param player2:
        :return:
        """
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.winner = None

    def start(self):
        while not self.winner:
            turn = Turn(self.current_player)
            turn_score = turn.run()
            self.current_player.record_score(self.current_player.score
                                             + turn_score)

            print("{}'s score is now {}".format(self.current_player.name,
                                                self.current_player.score))
            if self.current_player.score > 100:
                print("{} wins!".format(self.current_player.name))
                self.winner = self.current_player
            else:
                self.switch_players()

    def switch_players(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

if __name__ == '__main__':
    player1 = LessStupidAI("BeefFlavor")
    player2 = StupidHuman("Tom Brady")

    game = Game(player1, player2)
    game.start()