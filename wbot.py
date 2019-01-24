from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep
browser = None

def start():
	global browser
	browser = webdriver.Firefox(executable_path='/home/luca/Pojects/wbot/WhatsAppBot/geckodriver') #Pfad zum geckodriver
	browser.get('https://web.whatsapp.com/')
	print('Scan QR')

def send_message_to_contact(message, *contact_name):
	while True:
		try:
			search = browser.find_element_by_css_selector('#side > div._3CPl4 > div > label > input')
		except NoSuchElementException:
			sleep(1)
			continue
		break
	for n in contact_name:
		title = None
		try:
			title = browser.find_element_by_css_selector('#main > header > div._1WBXd > div > div > span').text
		except NoSuchElementException:
			pass
		if title != n:
			search.send_keys(n)
			search.send_keys(Keys.ENTER)
			try:
				not_found = browser.find_element_by_css_selector('#pane-side > div > div > span').text
				if not_found == 'No chats, contacts or messages found' or not_found == 'Es wurden keine Chats, Kontakte oder Nachrichten gefunden':
					return
			except:
				pass
		try:
			input = browser.find_element_by_css_selector('#main > footer > div._3oju3 > div._2bXVy > div > div._2S1VP.copyable-text.selectable-text')
		except NoSuchElementException:
			return
		for c in message:
			if c == '\n':
				input.send_keys(Keys.SHIFT, Keys.ENTER)
			else:
				input.send_keys(c)
		input.send_keys(Keys.ENTER)
		print('Message sent to ' + n + '.')
		sleep(0.5)


def send_messages_to_contact(contact_name, *messages):
	while True:
		try:
			search = browser.find_element_by_css_selector('#side > div._3CPl4 > div > label > input')
		except NoSuchElementException:
			print('exception')
			sleep(1)
			continue
		break
	title = None
	try:
            title = browser.find_element_by_css_selector('#main > header > div._1WBXd > div > div > span').text
	except NoSuchElementException:
		pass
	if title != contact_name:
            search.send_keys(contact_name)
            search.send_keys(Keys.ENTER)
            try:
                    not_found = browser.find_element_by_css_selector('#pane-side > div > div > span').text
                    if not_found == 'No chats, contacts or messages found' or not_found == 'Es wurden keine Chats, Kontakte oder Nachrichten gefunden':
                        return
            except:
                    pass
	try:
		input = browser.find_element_by_css_selector('#main > footer > div._3oju3 > div._2bXVy > div > div._2S1VP.copyable-text.selectable-text')
	except NoSuchElementException:
		return
	for m in messages:
		for c in m:
			if c == '\n':
				input.send_keys(Keys.SHIFT, Keys.ENTER)
			else:
				input.send_keys(c)
		input.send_keys(Keys.ENTER)
		print('Message sent to ' + contact_name + '.')
		sleep(0.5)

def send_message_to_number(number, message):
	print('d')
	message = message.replace(' ', '%20')
	for c in number:
		if c not in '0123456789':
			number = number.replace(c, '')
	browser.get('https://api.whatsapp.com/send?phone=' + number + '&text=' + message)
	try:
		browser.find_element_by_id('action-button').click()
	except NoSuchElementException:
		pass
	while True:
		try:
			browser.find_element_by_css_selector('#main > footer > div._3oju3 > button').click()
		except NoSuchElementException:
			sleep(1)
			continue
		break
	print('Message sent to ' + number + '.')

def retrieve_newest(contact_name, num):
	while True:
		try:
			#search = browser.find_element_by_id('input-chatlist-search')
			search = browser.find_element_by_css_selector('#side > div._3CPl4 > div > label > input')
		except NoSuchElementException:
			sleep(1)
			continue
		break
	title = None
	try:
		title = browser.find_element_by_css_selector('#main > header > div._1WBXd > div > div > span').text
	except NoSuchElementException:
		pass
	if title != contact_name:
		search.send_keys(contact_name)
		search.send_keys(Keys.ENTER)
		try:
			not_found = browser.find_element_by_css_selector('#pane-side > div > div > span').text
			if not_found == 'No chats, contacts or messages found' or not_found == 'Es wurden keine Chats, Kontakte oder Nachrichten gefunden':
				return
		except:
			pass
	messages = browser.find_elements_by_css_selector('div > div > div > div.copyable-text > div > span')
	newest = []
	for i in range(num):
		try:
			newest.append(messages[i].text)
		except IndexError:
			break
		if i == len(messages) - 1:
			browser.find_element_by_tag_name('html').send_keys(Keys.ARROW_UP)
			browser.find_element_by_tag_name('html').send_keys(Keys.ARROW_UP)
			messages = browser.find_elements_by_css_selector('div > div > div > div.copyable-text > div > span')
	return list(reversed(newest))

def set_about(status):
	while True:
		try:
			browser.find_element_by_css_selector('#side > header > div._2umId > div > img').click()
		except NoSuchElementException:
			sleep(1)
			continue
		break
	sleep(1)
	browser.find_element_by_css_selector('#app > div > div > div.MZIyP > div._3q4NP.k1feT > span > div > div > div > div:nth-child(4) > div.ogWqZ._2-h1L > div._1DTd4._1G2k- > div._2YmC2 > span:nth-child(1) > div').click()
	input = browser.find_element_by_css_selector('#app > div > div > div.MZIyP > div._3q4NP.k1feT > span > div > div > div > div:nth-child(4) > div.ogWqZ._2-h1L._31WRs > div._1DTd4 > div._3F6QL.bsmJe > div._2S1VP.copyable-text.selectable-text')
	input.clear()
	input.send_keys(status)
	input.send_keys(Keys.ENTER)
	print('About changed to "' + status + '".')
	browser.find_element_by_css_selector('#app > div > div > div.MZIyP > div._3q4NP.k1feT > span > div > div > header > div > div.SFEHG > button').click()

def close():
	browser.close()
