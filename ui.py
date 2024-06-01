
from utils import ResponseData, BadRequest
import service
from typing import Union

from colorama import Fore

from dto import UserRegisterDTO
from sessions import Session

session = Session()


def print_response(response: Union[ResponseData, BadRequest]):
    color = Fore.GREEN if response.status_code == 200 else Fore.RED
    print(color + response.data + Fore.RESET)


def login():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    response = service.login(username, password)
    print_response(response)
    if response.status_code == 200:
        crud_menu()


def register():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    dto: UserRegisterDTO = UserRegisterDTO(username, password)
    response = service.register(dto)
    print_response(response)


def logout():
    response = service.logout()
    print_response(response)


def todo_add():
    title = input('Enter title: ')
    response = service.todo_add(title)
    print_response(response)


def delete_todo():
    todo_id = int(input('Enter todo ID to delete: '))
    response = service.delete_todo(todo_id)
    print_response(response)


def update_todo():
    todo_id = int(input('Enter todo ID to update: '))
    new_title = input('Enter new title: ')
    response = service.update_todo(todo_id, new_title)
    print_response(response)


def read_todo():
    response = service.read_todo()
    print_response(response)


def block_user():
    choice = input('Block by (1) ID or (2) Username: ')
    if choice == '1':
        user_id = int(input('Enter user ID to block: '))
        response = service.block_user(user_id=user_id)
    elif choice == '2':
        username = input('Enter username to block: ')
        response = service.block_user(username=username)
    else:
        print(Fore.RED + 'Invalid choice' + Fore.RESET)
        return
    print_response(response)


def main_menu():
    while True:
        choice = unauthenticated_menu()
        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            break
        else:
            print(Fore.RED + 'Invalid choice' + Fore.RESET)


def unauthenticated_menu():
    print('1. Login')
    print('2. Register')
    print('3. Exit')
    return input('Enter your choice: ')


def crud_menu():
    while True:
        choice = authenticated_menu()
        if choice == '1':
            todo_add()
        elif choice == '2':
            delete_todo()
        elif choice == '3':
            update_todo()
        elif choice == '4':
            read_todo()
        elif choice == '5':
            block_user()
        elif choice == '6':
            logout()
            break
        elif choice == '7':
            break
        else:
            print(Fore.RED + 'Invalid choice' + Fore.RESET)


def authenticated_menu():
    print('1. Add Todo')
    print('2. Delete Todo')
    print('3. Update Todo')
    print('4. Read Todos')
    print('5. Block User')
    print('6. Logout')
    print('7. Exit')
    return input('Enter your choice: ')


