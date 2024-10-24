#programa estoque com frete
# variaveis de memoria
vcont = 's'
vproduto = ''
vquantidade = 0
vvalor = 0.0
vpeso = 0.0
# criando
Lproduto = []
Lvalor= []
Lquantidade=[]
Lpeso = []
print("sistema vendas")
while vcont=='s':
    Vproduto=input('digite o produto : ')
    Valor=float(input('valor:'))
    vquantidade=input(input("quit"))
    Lproduto.append (Vproduto)
    Lquantidade.append(vquantidade)
    Lpeso.append(vpeso)
    vcont  = input('deseja continuar <s/n>:')
    print('-----------------------------------------------')
    print('----------calculando peso -----')