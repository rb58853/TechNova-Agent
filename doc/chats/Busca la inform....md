# Busca la informacion de las ventas, mandale esta informacion de ventas a Pedro Alvarez por correo.
### Task query decomposer
Analyze the user query and available services to separate it into service-specific calls.
- **querys:** ['Busca la información de las ventas en la base de datos de ventas.', 'Busca el correo de Pedro Alvarez en la tabla clientes.', 'Envía la información de ventas a Pedro Alvarez por correo.']
## Busca la información de las ventas en la base de datos de ventas.
### Select prompts
Select the mosts appropriates prompts for the current query and generate the necessary arguments for use with the selected prompts
- **prompts:** None
### Select service
Select the most appropriate service for the current query.
- **service:** sqlite_server_sql_query- **args:** {'query': 'SELECT * FROM ventas;'}
### Response
Ventas encontradas en la base de datos de ventas:
- ID 1: producto iPhone 14 | categoría smartphones | precio 1300 | país Argentina | fecha de venta 2024-05-10
- ID 2: producto MacBook | categoría Airnotebooks | precio 1800 | país Chile | fecha de venta 2024-05-12

Resumen: 2 ventas registradas. Ingreso total: 3100 (moneda no especificada).


```json
[
  {
    "id": 1,
    "producto": "iPhone 14",
    "categoria": "smartphones",
    "precio": 1300,
    "pais": "Argentina",
    "fecha_venta": "2024-05-10"
  },
  {
    "id": 2,
    "producto": "MacBook",
    "categoria": "Airnotebooks",
    "precio": 1800,
    "pais": "Chile",
    "fecha_venta": "2024-05-12"
  }
]
```
## Busca el correo de Pedro Alvarez en la tabla clientes.
### Select prompts
Select the mosts appropriates prompts for the current query and generate the necessary arguments for use with the selected prompts
- **prompts:** None
### Select service
Select the most appropriate service for the current query.
- **service:** sqlite_server_clients_sql_query- **args:** {'query': "SELECT correo FROM clientes WHERE nombre = 'Pedro Alvarez' LIMIT 1;"}
### Response
Correo de Pedro Alvarez: pedro.alvarez@gmail.com.  
Dato obtenido de la tabla clientes.


```json
[
  {
    "correo": "pedro.alvarez@gmail.com"
  }
]
```
## Envía la información de ventas a Pedro Alvarez por correo.
### Select prompts
Select the mosts appropriates prompts for the current query and generate the necessary arguments for use with the selected prompts
- **prompts:** None
### Select service
Select the most appropriate service for the current query.
- **service:** messages_simulation_send_email- **args:** {'emails': ['pedro.alvarez@gmail.com'], 'subject': 'Resumen de ventas', 'body': 'Estimado Pedro Alvarez,\n\nAdjunto el resumen de ventas registrado en la base de datos:\n- Total de ventas: 2\n- Ingreso total: 3100 (moneda no especificada)\n- Detalles:\n  1) iPhone 14 | smartphones | Argentina | 2024-05-10 | 1300\n  2) MacBook | Airnotebooks | Chile | 2024-05-12 | 1800\n\nSaludos,\nEquipo de Ventas'}
### Response
Correo enviado a pedro.alvarez@gmail.com con el asunto "Resumen de ventas".
Datos recuperados: "Emails sent to 1 recipients (pedro.alvarez@gmail.com) with subject 'Resumen de ventas'."


```json
Emails sent to 1 recipients (pedro.alvarez@gmail.com) with subject 'Resumen de ventas'
```
