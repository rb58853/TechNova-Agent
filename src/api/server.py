import dotenv

dotenv.load_dotenv()

from fastchat import FastApp


base_prompt: str = """
La empresa "TechNova" vende productos electrónicos. Tiene un promedio de 5.000
ventas mensuales en Latinoamérica. Sus categorías principales son smartphones,
notebooks y accesorios.
"""

fastapp = FastApp(
    extra_reponse_system_prompts=[base_prompt],
    extra_selection_system_prompts=[base_prompt],
    len_context=20,
)

app = fastapp.app
