class SnakeClass(object):

    def __init__(self):
        self.name = ''
        self.position = []
        self.body = []
        self.direction = ''
        self.direction_change_to = ''
        self.enemy_body = []
        self.artifact_position = []
        self.fruit_position = []
        self.safe_zone_min_x = 0
        self.safe_zone_max_x = 0
        self.safe_zone_min_y = 0
        self.safe_zone_max_y = 0
        self.score = 0
        self.enemy_score = 0

    # snake's name
    def set_name(self, input_name: str):
        self.name = input_name

    def get_name(self) -> str:
        return self.name

    # snake's position
    def set_position(self, pos: list):
        self.position = pos

    def get_position(self) -> list:
        return self.position

    # snake's body
    def set_body(self, input_body: list):
        self.body = input_body

    def insert_body(self, pos: list):
        self.body.insert(0, pos)

    def get_body(self) -> list:
        return self.body

    def body_pop(self):
        self.body.pop()

    # intelligence information report
    def set_safe_zone(self, input_boundary: list):
        self.safe_zone_min_x = input_boundary[0]
        self.safe_zone_max_x = input_boundary[1]
        self.safe_zone_min_y = input_boundary[2]
        self.safe_zone_max_y = input_boundary[3]

    def update_enemy_body(self, pos: list):
        self.enemy_body = pos

    def get_enemy_body(self) -> list:
        return self.enemy_body

    def update_artifact_position(self, pos: list):
        self.artifact_position = pos

    def get_artifact_position(self) -> list:
        return self.artifact_position

    def update_fruit_position(self, pos: list):
        self.fruit_position = pos

    def get_fruit_position(self) -> list:
        return self.fruit_position

    def update_score(self, score: int):
        self.score = score

    def get_score(self) -> int:
        return self.score

    def update_enemy_score(self, score: int):
        self.enemy_score = score

    def get_enemy_score(self) -> int:
        return self.enemy_score

    # snake move function
    def up(self):
        self.position[0] = self.position[0]
        self.position[1] -= 10  # 10 unit per step
        self.insert_body([self.position[0], self.position[1]])

    def down(self):
        self.position[0] = self.position[0]
        self.position[1] += 10  # 10 unit per step
        self.insert_body([self.position[0], self.position[1]])

    def left(self):
        self.position[0] -= 10  # 10 unit per step
        self.position[1] = self.position[1]
        self.insert_body([self.position[0], self.position[1]])

    def right(self):
        self.position[0] += 10  # 10 unit per step
        self.position[1] = self.position[1]
        self.insert_body([self.position[0], self.position[1]])

    def snake_control(self):
        # modify this method
        pass
