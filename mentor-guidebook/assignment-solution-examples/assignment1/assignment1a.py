# Write your code here.
def hello():
    return "Hello!"

print(hello())

def greet(name):
    return f'Hello, {name}!'

print(greet("Tom"))

def calc(value1, value2, operation='multiply'):
    try:
        if (operation == 'add'):
            return value1 + value2
        elif (operation == 'subtract'):
            return value1 - value2
        elif (operation == 'multiply'):
            return value1 * value2
        elif (operation == 'divide'):
            try:
                return value1 / value2
            except ZeroDivisionError:
                return ("You can't divide by 0!")
        elif (operation == 'modulo'):
            return value1 % value2
        elif (operation == 'int_divide'):
            try:
                return value1 // value2
            except ZeroDivisionError:
                return ("You can't divide by 0!")
        elif (operation == 'power'):
            return value1 ** value2
        else:
            print(f'Illegal operation type {operation}')
    except TypeError:
        return(f"You can't {operation} those values!")
    
def data_type_conversion(value, datatype):
    try:
        if (datatype == 'float'):
            return float(value)
        elif(datatype == 'str'):
            return str(value)
        elif(datatype == 'int'):
            return int(value)
        else:
            return f"You can't convert {value} into a {datatype}."
    except ValueError:
        return f"You can't convert {value} into a {datatype}."

def grade(*args):
    try:
        avg = sum(args) / len(args)
        if (avg >= 90):
            return 'A'
        elif (avg >= 80):
            return 'B'
        elif (avg >= 70):
            return 'C'
        elif (avg >= 60):
            return 'D'
        else:
            return 'F'
    except TypeError:
        return "Invalid data was provided."

def repeat(string, count):
    try:
        result = ''
        for i in range(count):
            result += string
        return result
    except TypeError:
        return "Invalid data was provided."

def student_scores(query, **kwargs):
    try:
        if (query == 'best'):
            best = 0
            best_name = ''
            for name, score in kwargs.items():
                if score > best:
                    best = score
                    best_name = name
            return best_name
        elif (query == 'mean'):
            return sum(kwargs.values()) / len(kwargs)
        else:
            return f'bad query type: {query}'
    except TypeError:
        return "Invalid data was provided."
    
def titleize(string):
    small_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()
    words[0] = words[0].capitalize()
    words[-1] = words[-1].capitalize()
    result = []
    for word in words:
        if word not in small_words:
            result.append(word.capitalize())
        else:
            result.append(word)
    return ' '.join(result)

def hangman(secret, guess):
    exploded_secret = list(secret)
    exploded_result = []
    for char in exploded_secret:
        if char in guess:
            exploded_result.append(char)
        else:
            exploded_result.append('_')
    return ''.join(exploded_result)

def pig_latin(sentence):
    vowels = 'aeiou'
    suffix = 'ay'
    words = sentence.split()
    pig_words = []
    for word in words:
        # start with a vowel, add ay to the end
        if word[0] in vowels:
            pig_words.append(word + suffix)
        #starts with a consonant or the special case of qu
        else:
            prefix = ''
            suffix = ''
            for i in range(len(word)):
                if word[i] in vowels:
                    prefix = word[i:]
                    suffix += 'ay'
                    break
                else:
                    if word[i:].startswith('qu'):
                        suffix = suffix + 'qu' + 'ay'
                        prefix = word[(i+2):]
                        break
                    suffix += word[i]
            pig_words.append(prefix + suffix)
    return ' '.join(pig_words) 


    
    




    

