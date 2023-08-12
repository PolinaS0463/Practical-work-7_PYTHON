rows = int(input("Введите кол-во строк: "))
columns = int(input("Введите кол-во колонок: "))


def print_operation_table(operation, rows=rows, columns=columns):
    for row in range(1, rows+1):
        for column in range(1, columns+1):
            print(operation(row,column), end='\t')
        print()

print_operation_table(lambda x, y: x * y)