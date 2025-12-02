from fastchat import TerminalChat
from prompts import get_system_prompt

base_prompt: str = get_system_prompt("base_prompt")

chat = TerminalChat(
    logger_lv="INFO",
    extra_reponse_system_prompts=[base_prompt],
    extra_selection_system_prompts=[base_prompt],
)
chat.open()
