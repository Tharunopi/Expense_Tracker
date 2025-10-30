from dotenv import load_dotenv
from supabase import create_client, Client
from Utils.data_class_custom import userInfo, userLog
import os

load_dotenv()

class databaseConnection:
    def __init__(self):
        try:
            self.__info_table = "expense_tracker_user_info"
            self.__log_table = "expense_tracker_user_logs"
            self.__client: Client = create_client(supabase_url=os.getenv("supabase_url"), supabase_key=os.getenv("supabase_apikey"))
        
        except Exception as e:
            print(f"Error: databaseConnection() -> {e}")

    def insert_new(self, data:userInfo|userLog):
        try:
            self.__client

        except Exception as e:
            print(f"Error: databaseConnection.insert_new() -> {e}")