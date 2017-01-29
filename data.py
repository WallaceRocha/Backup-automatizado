import time
mes = {'1':'Janeiro', '2': 'Fevereiro', '3':'Março', '4':'Abril','5': 'Maio', '6':'Junho', '7':'Julho', '8':'Agosto','9':'Setembro','10':'Outubro', '11':'Novembro', '12':'Dezembro'}
hora = time.ctime().split(' ')[-2][0:-3]
from datetime import datetime
def data():
    now = datetime.now()

    dia = ("__%s de %s %s" %(now.day,mes[str(now.month)],hora))
    return dia
