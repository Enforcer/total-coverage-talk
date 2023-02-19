from doctor_queue.determine import Patient, Queue, determine_queue_position


def test_determine_queue_position():
    patient = Patient(is_pregnant=False, is_regular_blood_donor=False)
    queue = Queue()

    position = determine_queue_position(patient, queue)

    assert position == 0
