class BowlingGame:

    _frames_score = {}

    _remaining_frames = 10
    _remaining_rolls = 2
    _remaining_bonus = 0

    _bonus_throws = 0

    def __init__(self):
        self._setup_next_frame()

    def roll(self, pins):
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
        # todo define a ScoreCalculator to extract this logic
        score = 0
        for frame, throw in self._frames_score.items():
            if frame > 9:
                break

            throw_sum = sum(throw)
            score += throw_sum
            if throw_sum == 10:
                score += self._frames_score[frame+1][0]

                if len(throw) == 1:
                    if len(self._frames_score[frame + 1]) == 2:
                        score += self._frames_score[frame + 1][1]
                    else:
                        score += self._frames_score[frame + 2][0]

        return score

    def _handle_single_roll(self, pins):
        self._remaining_rolls -= 1
        self._remaining_spins -= pins
        self._frames_score[self._current_frame()].append(pins)
        if self._remaining_frames == 0 and self._remaining_bonus > 0:
            self._remaining_bonus -= 1

    def _handle_strike(self):
        if self._is_second_last_frame():
            self._remaining_bonus = 1
        if self._is_last_frame():
            self._remaining_bonus = 2

    def _handle_spare(self):
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
