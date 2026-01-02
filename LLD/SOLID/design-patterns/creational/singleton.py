class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print("Creating a new database connection instance.")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance
    
conn1 = DatabaseConnection()
conn2 = DatabaseConnection()