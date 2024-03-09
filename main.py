from bs4 import BeautifulSoup
import requests

character = ''

while True:
    print('Which character?')
    character = input('> ')

    if character == 'quit':
        break
    if len(character.split()) > 1:
        character = character.replace(' ', '-')

    url = 'https://www.prydwen.gg/star-rail/characters/' + character
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    is404 = soup.find('h1').text
    if is404 == '404 - Page Not Found':
        print(f'No character with the name: {character}. Try separating their name with a space or hyphen. \n')
        continue

    sub_stats = soup.find_all('div', class_ = 'sub-stats')
    skill_priority = sub_stats[1].p.text
    print(f'Traces priority: {skill_priority} \n')
