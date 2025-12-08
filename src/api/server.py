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
selection_filter: str = get_system_prompt("selection_filter")
# ------------------------------------------------

# ------------------------------------------------
#                Fastapi App                     #
# ------------------------------------------------
fastapp: FastApp = FastApp(
    extra_reponse_system_prompts=[base_prompt, md, filter_response],
    extra_selection_system_prompts=[base_prompt, no_sql, selection_filter],
    len_context=50,
)
app: FastAPI = fastapp.app
