import requests
from bs4 import BeautifulSoup

# El header para que seamos un cliente normal y no un robot
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
}

# url del sitio
url = "https://stackoverflow.com/questions"

# petición
request = requests.get(url, headers=header)

# parsear el DOM
soup = BeautifulSoup(request.text)

# Obtener la sección de preguntas
questionsSection = soup.find(id="questions")

# Obtenemos la lista de preguntas
questionList = questionsSection.find_all("div", class_="s-post-summary")

# Iteramos las preguntas
for question in questionList:
    # Obtenemos los titulos de las preguntas
    title = question.find("h3").text
    print(title)
