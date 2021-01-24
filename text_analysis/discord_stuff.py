from bs4 import BeautifulSoup

txt = open("text_analysis/Direct Messages - Private - weir [742737468092317697].html").read(9930)
print(txt[-300:])
#soup = BeautifulSoup(txt, 'html.parser')
#print(soup.findAll({"class": "preserve-whitespace"})