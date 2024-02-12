# **Criador de Etiqueta de Código de Barras // Barcode Tag Creator**

Arquivo "run_raw.py"

Este é um aplicativo Flask que gera etiquetas de código de barras no formato Code128 para produtos. // This is a Flask application that generates barcode labels in Code128 format for products.

## **Descrição // Description**

Este aplicativo fornece um endpoint de API `/create_tag` onde você pode enviar uma solicitação POST com um payload JSON contendo o código do produto. O servidor gera então uma imagem.png de etiqueta de código de barras com base no código do produto fornecido usando o formato de código de barras Code128 e retorna o caminho para o arquivo de imagem gerado. // This application provides a `/create_tag` API endpoint where you can send a POST request with a JSON payload containing the product code. The server then generates a barcode label image.png based on the product code provided using the Code128 barcode format and returns the path to the generated image file.

## **Pré-requisitos // Prerequisites**
- Python 3.x
- Flask
- python-barcode
- Postman

## **Uso // Usage
1. Execute a aplicação Flask // Execute the Flask aplication
  
2. Envie uma solicitação POST para http://localhost:xxxx/create_tag utilizando o Postman, com um payload JSON contendo o código do produto.
O servidor irá gerar uma imagem de etiqueta de código de barras com base no código do produto fornecido e retornará o caminho para o arquivo de imagem gerado na resposta. // Send a POST request to http://localhost:xxxx/create_tag with a JSON payload containing the product code. The server will generate a barcode label image based on the product code provided and return the path to the image file generated in the response.

## **Exemplo / Example**
'{"product_code": "123456789"}' http://localhost:xxxx/create_tag
