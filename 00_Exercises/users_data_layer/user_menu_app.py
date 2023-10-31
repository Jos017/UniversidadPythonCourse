from logger_base import log
from User_dao import User_dao
from User import User

option = None
while option != 5:
    print('Options:')
    print('1. List Users')
    print('2. Add User')
    print('3. Modify User')
    print('4. Delete User')
    print('5. Exit')
    option = int(input('Choose an option (1-5): '))

    match option:
        case 1:
            print('List Users'.center(50, '-'))
            users = User_dao.select()
            for user in users:
                log.info(
                    f'User: [{user.user_id} {user.username} {user.password}]'
                )
        case 2:
            print('Add User'.center(50, '-'))
            username = input('Username: ')
            password = input('Password: ')
            user = User(username=username, password=password)
            inserted_users = User_dao.insert(user)
            log.info(f'Inserted Users: {inserted_users}')
        case 3:
            print('Modify User'.center(50, '-'))
            user_id = int(input('User to modify (id): '))
            username = input('New username: ')
            password = input('New password: ')
            user = User(user_id, username, password)
            updated_users = User_dao.update(user)
            log.info(f'Updated Users: {updated_users}')
        case 4:
            print('Delete User'.center(50, '-'))
            user_id = int(input('User to remove (id): '))
            user = User(user_id)
            deleted_users = User_dao.delete(user)
            log.info(f'Deleted Users: {deleted_users}')
        case 5:
            log.info('Exit App')
        case _:
            log.error('Invalid option value, try again')
