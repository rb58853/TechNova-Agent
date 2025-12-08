import dotenv

dotenv.load_dotenv()

from fastapi import FastAPI
from fastchat import FastApp
from fastchat.config import AuthApiConfig
from ..prompts import get_system_prompt

# ------------------------------------------------
#                  PROMPTS                       #
# ------------------------------------------------
base_prompt: str = get_system_prompt("base_prompt")
md: str = get_system_prompt("md")
no_sql: str = get_system_prompt("no_sql")
filter_response: str = get_system_prompt("filter_response")
# ------------------------------------------------

# ------------------------------------------------
#                Fastapi App                     #
# ------------------------------------------------
fastapp: FastApp = FastApp(
    extra_reponse_system_prompts=[base_prompt, md],
    extra_selection_system_prompts=[base_prompt, no_sql],
)
app: FastAPI = fastapp.app
