from ui import main_menu
from db import create_table, migrate

def initialize():
    create_table()
    migrate()

# avval quyidagi main menu chiqadi:
# user muvaffaqiyatli login bolgandan keyin CRUD_TODO menu chiqadi:

if __name__ == '__main__':
    initialize()
    main_menu()