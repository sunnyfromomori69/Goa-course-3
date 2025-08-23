def rps(player1, player2):
    rules = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    if player1 == player2:
        return "Draw!"
    elif rules[player1] == player2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"
    

2.
def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
    
3.  
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
4.
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9