def test (name:str, age:int, isSleeping: bool):
    if isSleeping:
        sleep = 'is sleeping'
    else:
        sleep = 'is not sleeping'
    print(f'{name} (age: {age}), {sleep}.')

test(18, 'Joey', False)