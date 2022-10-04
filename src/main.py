from clases.user import User

def main():
    user = User('John')
    print(user.name)
    user0 = User()
    print(user0.name)


if __name__ == '__main__':
    main()