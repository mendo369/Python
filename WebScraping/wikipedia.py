import requests
from lxml import html

encabezado = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
}

url = "https://es.wikipedia.org/wiki/Wikipedia:Portada"

respuesta = requests.get(url, headers=encabezado)

# print(respuesta.text)
parser = html.fromstring(respuesta.text)

destacado = parser.get_element_by_id("Artículo_destacado")
destacadoClass = parser.find_class("main-header")
xpath = parser.xpath("//div[@id='Artículo_destacado']/text()")

print(destacado.text_content())
print(xpath)
for element in destacadoClass:
    print(element.text_content())
    print("***********************************")
