from fastchat import TerminalChat


base_prompt: str = """
La empresa "TechNova" vende productos electrónicos. Tiene un promedio de 5.000
ventas mensuales en Latinoamérica. Sus categorías principales son smartphones,
notebooks y accesorios.
"""

response_promt: str = """
Asegurate de responder en lenguaje natural describiendo la informacion que tienes. El objetivo es que el usuario te comprenda y pueda encontrar respuestas a sus interrogantes. Mientras no se te pida lenaguaje tecnico, evita usarlo en tus respuestas.
"""

chat = TerminalChat(
    logger_lv="INFO",
    extra_reponse_system_prompts=[
        base_prompt,
        # response_promt,
    ],
    extra_selection_system_prompts=[
        base_prompt,
    ],
)
chat.open()

"¿Cuántos productos principales vende TechNova?"
"¿Cuál fue el precio promedio de venta en Chile?"

"Creame una tabla de comparacion entre ventas por paises, luego con esa informacion dime que pais tuvo mas existo con la empresa?"
"Muestrame la informacion de las ventas por paises y luego dame un analisis de que pais tuvo mejor rendimiento y por que?"

"Dame la informacion resumida de las ventas, busca el correo de Pedro Alvarez y mandale esta informacion de ventas"
"Dame la informacion resumida de las ventas, mandale esta informacion de ventas a Pedro Alvarez por correo"
"Dame la informacion resumida de las ventas, mandale esta informacion de ventas por correo a los clientes de Estados Unidos"
