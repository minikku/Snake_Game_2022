from Snake import SnakeClass
import random


class Snake1(SnakeClass):

    def __init__(self):
        super().__init__()
        self.set_name('TEAM 1')  # <--- define team's name here
        self.visited_path = []

    def get_visited_path(self) -> list:
        return self.visited_path

    def add_visited_path(self, step: list):
        self.visited_path.insert(0, step)

    # override control method here
    def snake_control(self):
        # movement: up, down, left, right

        ml = 'ok'
        mr = 'ok'
        mu = 'ok'
        md = 'ok'

        # avoid danger zone
        if self.get_position()[0] - 10 < self.safe_zone_min_x:
            ml = 'no'

        if self.get_position()[0] + 10 > self.safe_zone_max_x - 10:
            mr = 'no'

        if self.get_position()[1] - 10 < self.safe_zone_min_y:
            mu = 'no'

        if self.get_position()[1] + 10 > self.safe_zone_max_y - 10:
            md = 'no'

        # avoid artifact
        if self.get_position()[0] - 10 == self.get_artifact_position()[0] and self.get_position()[1] == \
                self.get_artifact_position()[1]:
            ml = 'no'

        if self.get_position()[0] + 10 == self.get_artifact_position()[0] and self.get_position()[1] == \
                self.get_artifact_position()[1]:
            mr = 'no'

        if self.get_position()[0] == self.get_artifact_position()[0] and self.get_position()[1] - 10 == \
                self.get_artifact_position()[1]:
            mu = 'no'

        if self.get_position()[0] == self.get_artifact_position()[0] and self.get_position()[1] + 10 == \
                self.get_artifact_position()[1]:
            md = 'no'

        # avoid visited path
        for block in self.get_visited_path():
            if self.get_position()[0] - 50 == block[0] and self.get_position()[1] == block[1]:
                ml = 'no'

            if self.get_position()[0] + 50 == block[0] and self.get_position()[1] == block[1]:
                mr = 'no'

            if self.get_position()[0] == block[0] and self.get_position()[1] - 50 == block[1]:
                mu = 'no'

            if self.get_position()[0] == block[0] and self.get_position()[1] + 50 == block[1]:
                md = 'no'

        # avoid self touching
        for block in self.get_body()[1:]:
            if self.get_position()[0] - 10 == block[0] and self.get_position()[1] == block[1]:
                ml = 'no'

            if self.get_position()[0] + 10 == block[0] and self.get_position()[1] == block[1]:
                mr = 'no'

            if self.get_position()[0] == block[0] and self.get_position()[1] - 10 == block[1]:
                mu = 'no'

            if self.get_position()[0] == block[0] and self.get_position()[1] + 10 == block[1]:
                md = 'no'

        # avoid enemy touching
        for block in self.get_enemy_body():
            if self.get_position()[0] - 10 == block[0] and self.get_position()[1] == block[1]:
                ml = 'no'

            if self.get_position()[0] + 10 == block[0] and self.get_position()[1] == block[1]:
                mr = 'no'

            if self.get_position()[0] == block[0] and self.get_position()[1] - 10 == block[1]:
                mu = 'no'

            if self.get_position()[0] == block[0] and self.get_position()[1] + 10 == block[1]:
                md = 'no'

        # ready to move
        ready_move = []

        if ml == 'ok':
            ready_move.append('ml')
        if mr == 'ok':
            ready_move.append('mr')
        if mu == 'ok':
            ready_move.append('mu')
        if md == 'ok':
            ready_move.append('md')

        ready_move_len = len(ready_move)
        rand_idx = 0
        if ready_move_len > 1:
            rand_idx = random.randint(0, ready_move_len - 1)

        if ready_move_len > 0:
            if ready_move[rand_idx] == 'ml' and ml == 'ok':
                self.left()
                self.add_visited_path(self.get_position())
            if ready_move[rand_idx] == 'mr' and mr == 'ok':
                self.right()
                self.add_visited_path(self.get_position())
            if ready_move[rand_idx] == 'mu' and mu == 'ok':
                self.up()
                self.add_visited_path(self.get_position())
            if ready_move[rand_idx] == 'md' and md == 'ok':
                self.down()
                self.add_visited_path(self.get_position())
