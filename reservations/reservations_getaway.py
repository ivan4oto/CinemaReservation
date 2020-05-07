from db import Database
from db_schema.reservations import CREATE_RESERVATION, GET_BY_ID, GET_ALL, CHECK_ALL_FREE_SEATS, CHECK_IS_SEAT_IS_FREE, \
    MAKE_RESERVATION, DELETE_RESERVATION, GET_ALL_RESERVATION_FOR_PROJECTION
from reservations.models import ReservationModel


class ReservationGetaway:
    def __init__(self):
        self.model = ReservationModel
        self.START_COL = 1
        self.END_COL = 5
        self.START_ROW = 1
        self.END_ROW = 4
        self.db = Database()

    def create_initial(self, projection_id):
        with self.db.connection:
            for i in range(self.START_COL, self.END_COL):
                for j in range(self.START_ROW, self.END_ROW):
                    self.db.cursor.execute(CREATE_RESERVATION, (i, j, 0, projection_id))

    def get_by_id(self, *, reservation_id):
        with self.db.connection:
            self.db.cursor.execute(GET_BY_ID, (reservation_id))

            reservation_db = self.db.cursor.fetchall()
            reservation = self.model.convert(reservation_db[0])

        return reservation

    def get_all(self):
        with self.db.connection:
            self.db.cursor.execute(GET_ALL)

            reservation_db = self.db.cursor.fetchall()
            result = []

            for db_reservation in reservation_db:
                reservation = self.model.convert(db_reservation)
                result.append(reservation)

        return result

    def delete_projection(self, reservation_id):
        with self.db.connection:
            self.db.cursor.execute(DELETE_RESERVATION, (reservation_id))

    def get_free_seats_for_projection(self, *, projection_id):
        with self.db.connection:
            self.db.cursor.execute(CHECK_ALL_FREE_SEATS, (projection_id))

            number_of_free_seats = self.db.cursor.fetchone()

        return number_of_free_seats[0]

    def get_all_seats_for_projection(self, *, projection_id):
        with self.db.connection:
            self.db.cursor.execute(GET_ALL_RESERVATION_FOR_PROJECTION, (projection_id))

            reservations = []
            reservations_db = self.db.cursor.fetchall()
            for db_reservation in reservations_db:
                reservation = self.model.convert(db_reservation)
                reservations.append(reservation)
                
        return self.convert_reservation_to_seats(reservations)

    def convert_reservation_to_seats(self, reservations):

        matrix = [[0 for x in range(self.END_COL)] for y in range(self.END_ROW)]

        for reservation in reservations:
            row = reservation.row - 1
            col = reservation.col - 1

            if reservation.user_id == 0:
                matrix[row][col] = "."
            else:
                matrix[row][col] = "X"

        return matrix

    def check_seat_is_free(self, *, row, col, projection_id):
        with self.db.connection:
            self.db.cursor.execute(CHECK_IS_SEAT_IS_FREE, (projection_id, col, row))
            reservation_db = self.db.cursor.fetchall()
            reservation = self.model.convert(reservation_db[0])

        if reservation.user_id == 0:
            return True

        return False

    def make_reservation(self, *, list_of_reservations):
        with self.db.connection:
            for seats in list_of_reservations:
                # UPDATE reservations SET user_id = ? WHERE projection_id = ? and col = ? and row = ?;
                self.db.cursor.execute(MAKE_RESERVATION, (seats[2], seats[3], seats[1], seats[0]))