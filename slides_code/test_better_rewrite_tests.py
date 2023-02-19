
def test_generates_files_for_SOME_data_in_db() -> None:
    put_SOME_data_in_db()

    run_one_loop_of_program()

    assert some_files_exist()
