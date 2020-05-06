class ReservationModel:

    def __init__(self, *, row, col, user_id, projection_id, res_id=None):
        self.res_id = res_id
        self.row = row
        self.col = col
        self.user_id = user_id
        self.projection_id = projection_id

    def __str__(self):
        return f'''Reservation : \n'
                Row : {self.row}, Col : {self.col},
                User_id : {self.user_id}, Projection_id : {self.projection_id}'''

    @staticmethod
    def validate(row, col, user_id, projection_id):
        check = [row, col, user_id, projection_id]

        for i in check:
            if i < 0 or i is not int:
                raise ValueError(f"{i} should be bigger than 0 and should be integer.")

    @staticmethod
    def convert(reservation_db):
        return ReservationModel(row=reservation_db[1], col=reservation_db[2], user_id=reservation_db[3],
                                projection_id=reservation_db[4], res_id=reservation_db[0])
