from server import booking_confirmation_message


def test_message_confirmation_plusieurs_places():
    message = booking_confirmation_message(3)
    assert message == "Great-booking complete! You have booked 3 places."


def test_message_confirmation_une_place():
    message = booking_confirmation_message(1)
    assert message == "Great-booking complete! You have booked 1 place."
