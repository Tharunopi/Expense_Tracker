from abc import abstractmethod, ABC
from dotenv import load_dotenv
from supabase import create_client, Client
import os

load_dotenv()

class databaseConnection(ABC):
    def __init__(self):
        self.__client: Client = create_client(supabase_url=os.getenv("supabase_url"), supabase_key=os.getenv("supabase_apikey"))

    @abstractmethod
    def 