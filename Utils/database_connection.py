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

    def table_selector(self, data:userInfo|userLog) -> str|None:
        try:
            if isinstance(data, userInfo):
                table = self.__info_table
            else: 
                table = self.__log_table
            
            return table

        except Exception as e:
            print(f"Error: databaseConnection.table_selector() -> {e}")
            return None

    def insert_record(self, data:userInfo|userLog):
        try:
            table = self.table_selector(data)
            if table:
                response = self.__client.table(table).insert(data).execute()
                return response
            return None

        except Exception as e:
            print(f"Error: databaseConnection.insert_new() -> {e}")

    def upsert_record(self):
        try:
            pass

        except Exception as e:
            print(f"Error: databaseConnection.upsert_record() -> {e}")

    def delete_record(self):
        pass

    def fetch_record(self):
        pass