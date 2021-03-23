import requests, bs4

res = requests.get('https://www.i.ua/')
a = res.raise_for_status()
print("1---", a)

res_st = bs4.BeautifulSoup(res.txt)
print('2---', res_st)