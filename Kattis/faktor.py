"""
First and only line of input will contain 2 integers, A (1≤A≤100),\ne number of articles you plan to publish and I (1≤I≤100), the impact factor the owners require.
"""

def faktor(articles, impact):
    return (int(articles)*(int(impact)-1)+1)

a = input('Amount of articles u plan to publish: ')
i = input('Impact factor required: ')

print(f'Min amount of scientists u have to bribe: {faktor(a, i)}')
