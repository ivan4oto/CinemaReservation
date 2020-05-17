from sqlalchemy.orm import sessionmaker
from sqlalchemy import null

from db import Database
from projections.projections_getaway import ProjectionGetaway
from reservations.models import Reservation
from users.models import Users
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
        session = self.db.session()
        # projection = self.projectionGetaway.get_by_id(projection_id=projection_id)

        for i in range(self.START_COL, self.END_COL):
            for j in range(self.START_ROW, self.END_ROW):
                r = Reservation(row=i, col=j, user_id=0, projection_id=projection_id)
                session.add(r)
        session.commit()

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
        session = self.db.session()
        reservations = session.query(Reservation).filter(Reservation.projection_id == projection_id).all()
        result = 0
        for r in reservations:
            if r.user_id == 0:
                result += 1
        session.commit()

        return result

    def get_all_seats_for_projection(self, *, projection_id):
        projection = self.projectionGetaway.get_by_id(projection_id=projection_id)

        return self.convert_reservation_to_seats(projection.reservations)

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

    def check_seat_is_free(self, *, row, col, projection_id, username):
        session = self.db.session()
        # userid = session.query(Users).filter(Users.username == username).one()
        if int(row) > self.END_ROW - 1 or int(col) > self.END_ROW - 1 or int(row) < self.START_ROW or int(
                col) < self.START_COL:
            raise ValueError("Ain't got that much seets !")

        reservations = session.query(Reservation).filter(Reservation.projection_id == projection_id). \
            filter(Reservation.row == row).filter(Reservation.col == col).all()
        for r in reservations:
            if r.user_id == 0:
                return True
            else:
                return False

    def make_reservation(self, *, list_of_reservations):
        session = self.db.session()
        print(list_of_reservations, '<-----------')

        for seats in list_of_reservations:
            col, row, username, projection_id = seats[0], seats[1], seats[2], seats[3]
            userid = self.userGateway.select_user_id(username=username)

            reservation = session.query(Reservation).filter(Reservation.projection_id == projection_id). \
                filter(Reservation.col == col).filter(Reservation.row == row). \
                one()
            reservation.user_id = userid

            session.add(reservation)

        session.commit()
