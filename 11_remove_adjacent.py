"""
11. remove_adjacent

Dada uma lista de números, retorne uma lista onde todos elementos
adjacentes iguais são reduzidos a um único elemento.

Exemplo: [1, 2, 2, 3]
Irá retornar: [1, 2, 3]
"""


def remove_adjacent(nums):
    return solution_1(nums)

# 1˚ solution
def solution_2(nums):
    
def solution_1(nums):
    new_list = []
    nome = None
    for num in nums:
        if num != nome:
            new_list.append(num)
        nome = num
    return new_list
# inspiration: https://github.com/dougfraga/pythonic-challenges/blob/master/11_remove_adjacent.py

# 2˚ solution
def solution_2(nums):
    if not nums:
        return []
    
    l = [nums[0]]
    
    for c, n in zip(nums[:-1], nums[1:]):
        if c != n:
            l.append(n)
    return l

# 3˚ solution
def solution_2(nums):
    if not nums:
        return []
    
    return [nums[0]] + [n for c, n in zip(nums[:-1], nums[1:]) if c != n]
    
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
    test(remove_adjacent, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent, [], [])
    test(remove_adjacent, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
