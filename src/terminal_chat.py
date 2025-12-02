from fastchat import TerminalChat


base_prompt: str = """
La empresa "TechNova" vende productos electrónicos. Tiene un promedio de 5.000
ventas mensuales en Latinoamérica. Sus categorías principales son smartphones,
notebooks y accesorios.
"""

chat = TerminalChat(
    logger_lv="INFO",
    extra_reponse_system_prompts=[base_prompt],
    extra_selection_system_prompts=[base_prompt],
)
chat.open()

"¿Cuántos productos principales vende TechNova?"
"¿Cuál fue el precio promedio de venta en Chile?"
"Dame la informacion resumida de las ventas, mandale esta informacion de ventas a Pedro Alvarez por correo"
"Dame la informacion resumida de las ventas, mandale esta informacion de ventas por correo a los clientes de Estados Unidos"
