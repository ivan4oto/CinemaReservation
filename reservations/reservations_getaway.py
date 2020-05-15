from sqlalchemy.orm import sessionmaker

from db import Database
from db_schema.reservations import CREATE_RESERVATION, GET_BY_ID, GET_ALL, CHECK_ALL_FREE_SEATS, CHECK_IS_SEAT_IS_FREE, \
    MAKE_RESERVATION, DELETE_RESERVATION, GET_ALL_RESERVATION_FOR_PROJECTION
from projections.projections_getaway import ProjectionGetaway
from reservations.models import Reservation
from users.users_gateway import UserGateway


class ReservationGetaway:
    def __init__(self):
        self.db = Database()
        self.projectionGetaway = ProjectionGetaway()
        self.userGateway = UserGateway()
        self.session = sessionmaker(bind=self.db.engine)
        self.movie_gateway = ()
        self.START_COL = 1
        self.END_COL = 5
        self.START_ROW = 1
        self.END_ROW = 4

    def create_reservation_table(self):
        self.db.base.metadata.create_all(self.db.engine)

    def create_initial(self, projection_id):

        projection = self.projectionGetaway.get_by_id(projection_id=projection_id)

        for i in range(self.START_COL, self.END_COL):
            for j in range(self.START_ROW, self.END_ROW):
                projection.reservations.append(Reservation(row=i, col=j, user_id=0))

    def get_by_id(self, *, reservation_id):

        session = self.db.session()
        reservation = session.query(Reservation). \
            filter(Reservation.id == reservation_id). \
            one()

        session.commit()
        return reservation

    def get_all(self):

        session = self.db.session()
        reservation = session.query(Reservation).all()
        session.commit()

        return reservation

    def delete_reservation(self, reservation_id):
        session = self.db.session()
        session.query(Reservation).filter(Reservation.id == reservation_id).delete()
        session.commit()

    def get_free_seats_for_projection(self, *, projection_id):

        projection = self.projectionGetaway.get_by_id(projection_id=projection_id)

        result = 0
        for r in projection_id.reservations:
            if r.user_id == 0:
                result = result + 1

        # with self.db.connection:
        #     self.db.cursor.execute(CHECK_ALL_FREE_SEATS, (projection_id))
        #
        #     number_of_free_seats = self.db.cursor.fetchone()
        #
        # return number_of_free_seats[0]

    def get_all_seats_for_projection(self, *, projection_id):
        projection = self.projectionGetaway.get_by_id(projection_id=projection_id)

        return self.convert_reservation_to_seats(projection.reservations)

        # with self.db.connection:
        #     self.db.cursor.execute(GET_ALL_RESERVATION_FOR_PROJECTION, (projection_id))
        #
        #     reservations = []
        #     reservations_db = self.db.cursor.fetchall()
        #
        #     for db_reservation in reservations_db:
        #         reservation = self.model.convert(db_reservation)
        #         reservations.append(reservation)
        #
        # return self.convert_reservation_to_seats(reservations)

    def convert_reservation_to_seats(self, reservations):
        row = self.END_ROW - 1
        col = self.END_COL - 1

        matrix = [[0 for x in range(row)] for y in range(col)]

        for reservation in reservations:
            row = reservation.row - 1
            col = reservation.col - 1

            if reservation.user_id == 0:
                matrix[row][col] = "."
            else:
                matrix[row][col] = "X"
        return matrix

    def check_seat_is_free(self, *, row, col, projection_id):
        if int(row) > self.END_ROW - 1 or int(col) > self.END_ROW - 1 or int(row) < self.START_ROW or int(
                col) < self.START_COL:
            raise ValueError("Ain't got that much seets !")

        projection = self.projectionGetaway.get_by_id(projection_id=projection_id)

        for r in projection.reservations:
            if r.row == row and r.col == col:
                if r.user_id == 0:
                    return True
                else:
                    return False

        # with self.db.connection:
        #     self.db.cursor.execute(CHECK_IS_SEAT_IS_FREE, (projection_id, col, row))
        #     reservation_db = self.db.cursor.fetchall()
        #     reservation = self.model.convert(reservation_db[0])
        #
        # if reservation.user_id == 0:
        #     return True
        #
        # return False

    def make_reservation(self, *, list_of_reservations):
        session = self.db.session()

        for seats in list_of_reservations:
            username = seats[2]
            projection_id = seats[3]
            col = seats[1]
            row = seats[0]
            projection = self.projectionGetaway.get_by_id(projection_id=projection_id)
            user = self.userGateway.select_user_id(username=username)
            for r in projection.reservations:
                if r.row == row and r.col == col:
                    user.reservations.append(r)
            session.commit()

            # UPDATE reservations SET user_id = ? WHERE projection_id = ? and col = ? and row = ?;
            # self.db.cursor.execute(MAKE_RESERVATION, (seats[2], seats[3], seats[1], seats[0]))
