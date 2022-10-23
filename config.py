from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "18641113"))
API_HASH = getenv("API_HASH", "bc5fea81e7bf9f3c0784a0a7d35f9c71")
OWNER_USERNAME = getenv("kassim_darlzzz")
BOT_TOKEN = getenv("BOT_TOKEN","5673232199:AAFDwlz2T7U22NONiyJWKOBNuWgKaC_xnLY")
BOT_USERNAME = getenv("BOT_USERNAME", "Darlzzzmusic_bot")
BOT_NAME = getenv("BOT_NAME","darlzzzmusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "AQCRbpMZRCun02ZdJ6j8wQ4pkOMy8P5mBYxiJEavLlWjgDsQljShUh94PHzCMtNMk7WtfRmqq9UVee8p2c8TNOcYu3No4UAynYEBS1fE2nRfo60-PMVEI6MB_X3CUNOQ4KkkdOje2tx2cdGUNFMiomERDrwSDolOiljbHrfSutRHpSjLacXl3m7HlUOFeCa-uMSuhLJ8-kX5_VVjHBhnsDZSCyT7duS0YZRAfnO2Ikq6KCx0bmHXWZXyEQKRRJRdOWkQU08XJwB6Ny-PfLmHd8K4U8vB2keU9CpPFWT_i7vlVMFlWn1ROROK9kT_P_4Bcs1smaDKK55oCdHJGVVtU0r_AAAAAU7LTEIA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5323266323").split()))
