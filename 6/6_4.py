lst = [1, 2.34, 'ddf', 23, 'df', ['q', 'w'], 'df']
print(list(filter(lambda x: isinstance(x, str), lst)))
