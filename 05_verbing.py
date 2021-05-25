"""
05. verbing

Dada uma string, se seu tamanho for pelo menos 3,
adicione 'ing' no seu fim, a menos que a string
já termine com 'ing', nesse caso adicione 'ly'.

Se o tamanho da string for menor que 3, não altere nada.

Retorne o resultado da string.
"""


def verbing(s):
    return solution_2(s)


def solution_1(s):
    v_ing = 'ing'
    v_ly = 'ly'
    if s[-3:] == v_ing and len(s) > 3:
        result = s[:] + v_ly
    elif s[-3:] != v_ing and len(s) > 3:
        result = s[:] + v_ing
    else:
        result = s[:]
    return result


def solution_2(s):
    if len(s) > 3:
        result = f'{s + "ing" if not "ing" in s else s + "ly"}'
    else:
        result = s[:]
    return result

    # --- Daqui para baixo são apenas códigos auxiliáries de teste. ---


def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(verbing, 'hail', 'hailing')
    test(verbing, 'swiming', 'swimingly')
    test(verbing, 'do', 'do')
