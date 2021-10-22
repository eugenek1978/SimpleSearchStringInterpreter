INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        self.start_digit_position = -1
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        text = self.text

        if self.pos > len(text) - 1:
            return Token(EOF, None)

        if text[self.pos].isdigit():
            number = 0
            while self.pos < len(text) and text[self.pos].isdigit():
                number = number*10 + int(text[self.pos])
                self.pos += 1

            token = Token(INTEGER, number)
            return token

        if text[self.pos] == '+':
            token = Token(PLUS, text[self.pos])
            self.pos += 1
            return token

        if text[self.pos] == '-':
            token = Token(MINUS, text[self.pos])
            self.pos += 1
            return token

        self.error()

    def eat(self, token):
        self.current_token = self.get_next_token()

    def expr(self):

        self.current_token = self.get_next_token()
        left = self.current_token

        op = self.get_next_token()

        right = self.get_next_token()
        result = 0;
        add = lambda a, b: a + b
        sub = lambda a, b: a - b
        if op.type == PLUS:
            result = add(left.value, right.value)
        elif op.type == MINUS:
            result = sub(left.value, right.value)

        return result


def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()