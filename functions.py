def get_summ(one, two, delimiter="&"):
    concatenated = f"{one}{delimiter}{two}"
    return concatenated

my_string = get_summ("Learn", "python")
print(my_string.upper())

print('-'*50)
def hello(*args, **kwargs):
    print(args)
    print(kwargs)

hello(17,18)
hello(1,2,55,66,cat='cat',dog='Russia')