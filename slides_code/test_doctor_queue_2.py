from doctor_queue.determine import determine_queue_position, Patient, Queue


def test_pregnancy_means_accessing_doctor_without_having_to_wait():
    queue = Queue()
    patient = Patient(is_pregnant=True, is_regular_blood_donor=False)

    queue_position = determine_queue_position(patient, queue)

    assert queue_position == 0
