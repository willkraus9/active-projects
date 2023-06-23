#higher order functions - accepts function as argument OR returns function

#functions accept argument:
def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
#calling hello function, naming loud as func (variable replaceable)
    #choose function, then execute

#return function
def divisor(x):
    def dividend(y):
        return y/x
    return dividend
#if want to call dividend, hasve to call divisor first
divide = divisor(10)
print(divide(2))
#order matters! first call divisor function: go to most nested variable (y)
    #when call function again, fill in x (next closest to full nest)

