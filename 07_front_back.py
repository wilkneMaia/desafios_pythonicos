"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""


def front_back(a, b):
    a_front = ''
    a_back = ''
    b_front = ''
    b_back = ''
    a_b = a + b

    if (len(a) % 2) == 0:
        a_front = a[:len(a)//2]
        a_back = a[len(a)//2:]
    else:
        a_front = a[:len(a)//2 + 1]
        a_back = a[len(a)//2 + 1:]

    if (len(b) % 2) == 0:
        b_front = b[:len(b)//2]
        b_back = b[len(b)//2:]
    else:
        b_front = b[:len(b)//2 + 1]
        b_back = b[len(b)//2 + 1:]

    return a_front + b_front + a_back + b_back


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
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
