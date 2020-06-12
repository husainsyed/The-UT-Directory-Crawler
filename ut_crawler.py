from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

text_file = open("names.txt", "r")
names_list = text_file.read().split('\n')
text_file.close()



for i in names_list:

	first_name, last_name = i.split(' ', 1)
	my_url = 'https://directory.utexas.edu/advanced.php?aq%5BName%5D=' + first_name + '+' + last_name + '&aq%5BCollege%2FDepartment%5D=&aq%5BTitle%5D=&aq%5BEmail%5D=&aq%5BHome+Phone%5D=&aq%5BOffice+Phone%5D=&scope=student'
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()

	#Parsing HTML
	page_soup = soup(page_html, "html.parser")

	#Now grabbing the class
	containers = page_soup.findAll("div", {"class" : "UT-page"})

	if 'Directory' in containers[1].h2.text:
		with open('names_email.csv', 'a') as f:
			right_div = containers[1]
			right_div.div.div.div.section.div.div.table.findAll("td", {"head"})
			correct_one =  right_div.div.div.div.section.div.div.table.findAll("td")
			email_element = correct_one[3]
			email_element = email_element.text.strip()

			enrolled_college = correct_one[5].text.strip()
			major = correct_one[7].text.strip()
			classification = correct_one[9].text.strip()
			f.write(first_name + " " + last_name + ", " + email_element + ", " + enrolled_college + ", " + major.replace("," , "") + ", " + classification + "\n")
			f.close()