import os

from dotenv import load_dotenv, find_dotenv


dotenv_path = find_dotenv()

load_dotenv(dotenv_path)


DB_URL: str = os.environ.get('DB_URL') if os.environ.get('DB_URL') else 'sqlite:///database/data.db' # type: ignore
