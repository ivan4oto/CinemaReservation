from reservations.reservations_getaway import ReservationGetaway


class ReservationController:
    def __init__(self):
        self.reservation_gateway = ReservationGetaway()

    def get_reservation_by_id(self, reservation_id):
        reservation = self.reservation_gateway.get_by_id(reservation_id=reservation_id)
        return reservation

    def get_all(self):
        reservations = self.reservation_gateway.get_all()
        return reservations

    def delete(self, reservation_id):
        self.reservation_gateway.delete_reservation(reservation_id=reservation_id)
        return True

    def check_is_seats_are_free(self, col, row, user_id, projection_id):
        if not self.reservation_gateway.check_seat_is_free(row=row, col=col, projection_id=projection_id):
            return True
        return False

    def make_reservation(self, list_of_reservations):
        self.reservation_gateway.make_reservation(list_of_reservations=list_of_reservations)
        return True

    def take_all_free_seats_for_pr(self, projection_id):
        return self.reservation_gateway.get_free_seats_for_projection(projection_id=projection_id)

    def get_all_seats_for_projection(self, *, projection_id):
        return self.reservation_gateway.get_all_seats_for_projection(projection_id=projection_id)
