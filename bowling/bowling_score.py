class BowlingScore:
    """Given a sequence of frames containing the spins fallen in each throws, this class can calculate the total
    score of the game"""

    def __init__(self, frames_scores: {}):
        self._frames_scores = frames_scores

    def total_score(self) -> int:
        """Calculates the total score of the game"""

        score = 0
        for current_frame, frame_throws in self._frames_scores.items():
            if current_frame > 9:
                break

            throw_sum = sum(frame_throws)
            score += throw_sum

            if self._is_strike(current_frame):
                score += self._get_strike_additional_score(current_frame)
            elif self._is_spare(current_frame):
                score += self._get_spare_additional_score(current_frame)

        return score

    def _is_spare(self, frame_index: int) -> bool:
        """Checks if the given frame was a spare or not"""

        return sum(self._frames_scores[frame_index]) == 10 and not self._is_strike(frame_index)

    def _is_strike(self, frame_index: int) -> bool:
        """Checks if the given frame was a strike or not"""

        return len(self._frames_scores[frame_index]) == 1

    def _get_spare_additional_score(self, frame_index: int) -> int:
        """Gets the additional spare points of a given frame"""

        return self._frames_scores[frame_index + 1][0]

    def _get_strike_additional_score(self, frame_index: int) -> int:
        """Gets the additional strike points of a given frame"""

        next_score = self._frames_scores[frame_index + 1][0]
        if not self._is_strike(frame_index + 1):
            next_2_score = self._frames_scores[frame_index + 1][1]
        else:
            next_2_score = self._frames_scores[frame_index + 2][0]

        return next_score + next_2_score
