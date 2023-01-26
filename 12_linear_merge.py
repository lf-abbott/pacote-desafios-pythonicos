"""
12. linear_merge

Dada duas listas ordenadas em ordem crescente, crie e retorne uma lista
com a combinação das duas listas, também em ordem crescente. Você pode
modificar as listas recebidas.

A sua solução deve rodar em tempo linear, ou seja, deve fazer uma
única passagem em cada uma das listas.
"""

def linear_merge(list1, list2):
    tam1 = len(list1)
    tam2 = len(list2)
    
    cont = 0
    listao = []
    
    if tam1>tam2:
        while cont < tam2:
            listao.append(list1[cont])
            listao.append(list2[cont])
            cont = cont +1
        dif = tam1 - tam2
        while dif > 0:
            listao.append(list1[tam1-dif])
            dif = dif -1
    else:
        while cont < tam1:
            listao.append(list1[cont])
            listao.append(list2[cont])
            cont = cont +1
        dif = tam2 - tam1
        while dif > 0:
            listao.append(list2[tam2-dif])
            dif = dif -1
        
    listao.sort()    

    return (listao)

"""
# outra solução que fuciona com as duas expresoes l1 ou l2:

def linear_merge(list1, list2):
    [list2.append(i) for i in list1]
    list2.sort()
    
    return (list2)
 
"""
"""
#outra solução mais evoluida:

from heapq import merge

def linear_merge(list1, list2):
    
    return list(merge(list1, list2))
    
"""

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(linear_merge, (['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])
