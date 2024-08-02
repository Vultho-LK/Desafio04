# mostre os tipo primitivo e (quase) todas as informacoes possiveis
n = input('digite algo: ')
print('''o tipo é {} 
é alfabetico {}
é numerico {} 
é alfanumerico {}
é um espaço {}
esta em minisculo {}
esta em maiusculo {}
começa com letra maiuscola {}
'''.format(type(n), n.isalpha(), n.isnumeric(), n.isalnum(), n.isspace(), n.islower(), n.isupper(), n.istitle()))
