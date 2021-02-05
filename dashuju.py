import requests
from bs4 import BeautifulSoup

def get_info(url):
	r = requests.get(url)
	return r.content

def parse_str(content):
	soup = BeautifulSoup(content, 'lxml')
	infos = [v.find('a') for v in soup.find_all('li')]
	r = []
	for v in infos:
		try:
			r.append('\t'.join([v.text, v['href']]))
		except:
			pass
	return '\n'.join(r)

def load_rlt(rlt, filename):
	with open(filename, 'w') as fw:
		fw.write(rlt)

def main():
	url = 'http://hao.bigdata.ren/'
	r = get_info(url)
	rlt = parse_str(r)
	load_rlt(rlt, 'bigdata.csv')

if __name__ == '__main__':
	main()
	print('Finished!')