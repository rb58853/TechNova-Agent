import dotenv

dotenv.load_dotenv()

from fastchat import FastApp
from ..prompts import get_system_prompt

base_prompt: str = get_system_prompt("base_prompt")

fastapp = FastApp(
    extra_reponse_system_prompts=[base_prompt],
    extra_selection_system_prompts=[base_prompt],
    len_context=20,
)

app = fastapp.app
