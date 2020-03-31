"""Practice to understand crash course and args and kwargs"""

#1: test out zip

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

# zip is lazy, so you have to do something like the following
[pair for pair in zip(list1, list2)]    # is [('a', 1), ('b', 2), ('c', 3)]


assert [pair for pair in zip(list1, list2)] == [('a', 1), ('b', 2), ('c', 3)]

#2: test out unzipping
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

letters, numbers = zip(('a', 1), ('b', 2), ('c', 3))
print("letters: ", letters, "numbers: ", numbers)


#3: try a function, *[] unzips a list such that the elements are directly inputted
def add(a, b): return a + b

add(1, 2)      # returns 3
try:
    add([1, 2])
except TypeError:
    print("add expects two inputs")
add(*[1, 2])   # returns 3


def doubler(f):
    # Here we define a new function that keeps a reference to f
    def g(x):
        return 2 * f(x)

    # And return that new function.
    return g

def f1(x):
    return x + 1

g = doubler(f1)
assert g(3) == 8,  "(3 + 1) * 2 should equal 8"
assert g(-1) == 0, "(-1 + 1) * 2 should equal 0"

def f2(x, y):
    return x + y

g = doubler(f2)
try:
    g(1, 2)
except TypeError:
    print("as defined, g only takes one argument")

def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)

magic(1, 2, key="word", key2="word2")

# prints
#  unnamed args: (1, 2)
#  keyword args: {'key': 'word', 'key2': 'word2'}

def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = {"z": 3}
assert other_way_magic(*x_y_list, **z_dict) == 6, "1 + 2 + 3 should be 6"

def doubler_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
print(g(1,2))
assert g(1, 2) == 6, "doubler should work now"


"""my practice, 3-30-2020"""

#take list and unzip
def my_practice(args):
    for i in range(*args):
        print(i)

my_practice([3,6]) # helpful for taking list and unpacking as inputs for function

#take loose inputs and create tuple
def create_tuple(*args):
    print(type(args))
    return(args)

print(create_tuple(1, 2, 4, 5))
print(create_tuple(6, 7))

def create_sentence(name:str, age:int, job:str):
    sentence = f"My name is {name} and I am {str(age)} years old and I work as a {job}"
    return sentence

my_sent = create_sentence("anna", 23, "student")
print(my_sent)
 
facts_dict = {"age": 61, "name": "Jeff", "job": "Dad"}
my_sent2 = create_sentence(**facts_dict)
print(my_sent2)

#test out generator for tuple 
my_generator = (i for i in range(3,6))
print(my_generator) #creates generator object
