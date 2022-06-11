# print a string using plus signs

animal = 'chicken'

print('the ' + animal + " crossed the road")

# print using f string - i could understand its a little bit more scalable
print(f'the {animal} crossed the road')

# this seems to be different pattern - start executing here vs. start from the top
def myfunction():
    print('this executes a function instead of starting at main')


if __name__ == '__main__':
    print('hello world')

    myfunction()

