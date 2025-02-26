from nltk.sem import Expression

read_expr = Expression.fromstring
expr = read_expr("forall x.(man(x) -> mortal(x))")
print(expr)
