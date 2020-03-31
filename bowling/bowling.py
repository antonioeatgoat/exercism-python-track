from bowling_score import BowlingScore


class BowlingGame:
    """The Bowling Game class

    Once initialized, the class setup a new game. It updates its internal status every time a new ball roll is made,
    so basically every method inside the class works considering the current game status.
    """

    _frames_score = {}

    _remaining_frames = 10
    _remaining_rolls = 2
    _remaining_bonus = 0

    _bonus_throws = 0

    def __init__(self):
        self._setup_next_frame()

    def roll(self, pins):
        """Performs a new throw"""
        if self._is_game_finished():
            raise ValueError('The game is finished, you cannot roll anymore.')

        if pins < 0 or pins > 10:
            raise ValueError('The number of pins fallen is not valid. It can be an integer from 0 to 10 (included).')

        if pins > self._remaining_spins:
            raise ValueError('The number of pins fallen is not valid. It cannot be higher than the spins remained.')

        self._handle_single_roll(pins)

        if self._is_strike():
            self._handle_strike()

        if self._is_spare():
            self._handle_spare()

        if self._is_frame_finished() and not self._is_game_finished():
            self._update_frame_count()
            self._setup_next_frame()

    def score(self):
        """Returns the total scores of the game. This method can work only if called at the very end of the game"""
        bowling_score = BowlingScore(self._frames_score)
        return bowling_score.total_score()

    def _handle_single_roll(self, pins):
        """Updates counters related to a generic single ball throw"""
        self._remaining_rolls -= 1
        self._remaining_spins -= pins
        self._frames_score[self._current_frame()].append(pins)
        if self._remaining_frames == 0 and self._remaining_bonus > 0:
            self._remaining_bonus -= 1

    def _handle_strike(self):
        """Updates counters specific of a strike throw"""
        if self._is_second_last_frame():
            self._remaining_bonus = 1
        if self._is_last_frame():
            self._remaining_bonus = 2

    def _handle_spare(self):
        """Updates counters specific of a spare throw"""
        if self._is_last_frame():
            self._remaining_bonus = 1

    def _update_frame_count(self):
        self._remaining_frames -= 1

    def _setup_next_frame(self):
        self._frames_score[self._current_frame()] = []
        self._remaining_rolls = 2
        self._remaining_spins = 10

    def _is_strike(self):
        return self._remaining_rolls == 1 and self._remaining_spins == 0

    def _is_spare(self):
        return self._remaining_rolls == 0 and self._remaining_spins == 0

    def _is_frame_finished(self):
        return self._remaining_rolls == 0 or self._is_strike()

    def _is_game_finished(self):
        return self._remaining_frames == 0 and self._remaining_bonus == 0

    def _current_frame(self):
        return 10 - self._remaining_frames

    def _is_last_frame(self):
        return self._remaining_frames == 1

    def _is_second_last_frame(self):
        return self._remaining_frames == 2
