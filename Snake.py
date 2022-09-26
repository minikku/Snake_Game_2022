class SnakeClass(object):

    def __init__(self):
        self.__name = ''
        self.__position = []
        self.__body = []
        self.__enemy_body = []
        self.__artifact_position = []
        self.__fruit_position = []
        self.__safe_zone_min_x = 0
        self.__safe_zone_max_x = 0
        self.__safe_zone_min_y = 0
        self.__safe_zone_max_y = 0
        self.__score = 0
        self.__enemy_score = 0
        self.__move_locked_status = False

    # snake's name
    def set_name(self, input_name: str):
        self.__name = input_name

    def get_name(self) -> str:
        return self.__name

    # snake's position
    def set_position(self, pos: list):
        self.__position = pos

    def get_position(self) -> list:
        return self.__position

    # snake's body
    def set_body(self, input_body: list):
        self.__body = input_body

    def insert_body(self, pos: list):
        self.__body.insert(0, pos)

    def get_body(self) -> list:
        return self.__body

    def body_pop(self):
        self.__body.pop()

    # intelligence information report
    def set_safe_zone(self, input_boundary: list):
        self.__safe_zone_min_x = input_boundary[0]
        self.__safe_zone_max_x = input_boundary[1]
        self.__safe_zone_min_y = input_boundary[2]
        self.__safe_zone_max_y = input_boundary[3]

    # enemy's body
    def update_enemy_body(self, pos: list):
        self.__enemy_body = pos

    def get_enemy_body(self) -> list:
        return self.__enemy_body

    # artifact
    def update_artifact_position(self, pos: list):
        self.__artifact_position = pos

    def get_artifact_position(self) -> list:
        return self.__artifact_position

    # fruit
    def update_fruit_position(self, pos: list):
        self.__fruit_position = pos

    def get_fruit_position(self) -> list:
        return self.__fruit_position

    # score
    def update_score(self, score: int):
        self.__score = score

    def get_score(self) -> int:
        return self.__score

    def update_enemy_score(self, score: int):
        self.__enemy_score = score

    def get_enemy_score(self) -> int:
        return self.__enemy_score

    # move lock
    def move_lock(self):
        # FOR SNAKE CLASS ONLY
        self.__move_locked_status = True

    def move_unlock_FOR_MAIN_ONLY(self):
        # FOR MAIN ONLY
        self.__move_locked_status = False

    # snake move function
    def up(self):
        if self.__move_locked_status == 0:
            self.__position[0] = self.__position[0]
            self.__position[1] -= 10  # 10 unit per step
            self.insert_body([self.__position[0], self.__position[1]])
            self.move_lock()

    def down(self):
        if self.__move_locked_status == 0:
            self.__position[0] = self.__position[0]
            self.__position[1] += 10  # 10 unit per step
            self.insert_body([self.__position[0], self.__position[1]])
            self.move_lock()

    def left(self):
        if self.__move_locked_status == 0:
            self.__position[0] -= 10  # 10 unit per step
            self.__position[1] = self.__position[1]
            self.insert_body([self.__position[0], self.__position[1]])
            self.move_lock()

    def right(self):
        if self.__move_locked_status == 0:
            self.__position[0] += 10  # 10 unit per step
            self.__position[1] = self.__position[1]
            self.insert_body([self.__position[0], self.__position[1]])
            self.move_lock()

    def snake_control(self):
        # override this method
        pass
