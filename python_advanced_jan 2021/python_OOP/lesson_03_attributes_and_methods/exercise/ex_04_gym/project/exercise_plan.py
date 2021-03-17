class ExercisePlan:
    id = 0

    def __init__(self, trainer_id, equipment_id, duration):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.get_next_id()

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"

    @staticmethod
    def get_next_id():
        ExercisePlan.id += 1
        return ExercisePlan.id

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        return cls(trainer_id=trainer_id, equipment_id=equipment_id, duration=hours*60)
