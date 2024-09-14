from dotenv import load_dotenv
import os
load_dotenv()

SERVER_URL = os.getenv("SERVER_URL")
PORT = '8900'
ENV = 'dev'

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")