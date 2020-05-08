class UserModel:
    def __init__(self, *, username, id, usertype = ''):
        self.username = username
        self.id = id
        self.type = usertype

    def __str__(self):
        return f'username: {self.username}  account_type: {self.type}   id: {self.id}'


    @staticmethod
    def validate(email, password):
        if len(password) < 8:
            raise ValueError('Password is too short !')
        if not any([x.isupper() for x in password]):
            raise ValueError('Password must include one uppercase letter !')
        n = False
        for i in "[@_!#$%^&*()<>?/\|}{~:]":
            if i in password:
                n = True
        if not n:
            raise ValueError('Password must contain atleast one special character !')

        