from fastchat import TerminalChat
from prompts import get_system_prompt

# ------------------------------------------------
#                  PROMPTS                       #
# ------------------------------------------------
base_prompt: str = get_system_prompt("base_prompt")
md: str = get_system_prompt("md")
no_sql: str = get_system_prompt("no_sql")
filter_response: str = get_system_prompt("filter_response")
# ------------------------------------------------

chat = TerminalChat(
    logger_lv="INFO",
    extra_reponse_system_prompts=[base_prompt, md, filter_response],
    extra_selection_system_prompts=[base_prompt, no_sql],
)
chat.open()
