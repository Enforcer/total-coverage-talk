class Patient:
    def __init__(self, is_pregnant: bool, is_regular_blood_donor: bool):
        self.is_pregnant = is_pregnant
        self.is_regular_blood_donor = is_regular_blood_donor


class Queue(list):
    pass


def determine_queue_position(patient: Patient, queue: Queue) -> int:
    # initially, we assume that a patient will just join queue
    position = len(queue)

    # there are certain groups of patients that are served without
    # having to wait in a queue
    if patient.is_pregnant or patient.is_regular_blood_donor:
        position = 0

    return position
