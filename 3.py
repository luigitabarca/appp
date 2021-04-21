
from requests_html import HTMLSession
session = HTMLSession()
my_url = 'https://coinbit.co.kr/'
r = session.get(my_url)

p=r.html.render()

print(p)