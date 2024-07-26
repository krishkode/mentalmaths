from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Define the topics and their corresponding functions
def times_tables():
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    question = f"{num1} x {num2} = ?"
    answer = num1 * num2
    return question, answer

def multiply_by_11():
    num = random.randint(1, 99)
    question = f"{num} x 11 = ?"
    answer = num * 11
    return question, answer

def square_ending_in_5():
    num = random.randint(1, 9) * 10 + 5
    question = f"{num}^2 = ?"
    answer = num * num
    return question, answer

def multiply_same_first_digit_last_add_10():
    digit = random.randint(1, 9)
    last_digit1 = random.randint(1, 9)
    last_digit2 = 10 - last_digit1
    num1 = digit * 10 + last_digit1
    num2 = digit * 10 + last_digit2
    question = f"{num1} x {num2} = ?"
    answer = num1 * num2
    return question, answer

def multiply_10_to_20():
    num1 = random.randint(10, 20)
    num2 = random.randint(10, 20)
    question = f"{num1} x {num2} = ?"
    answer = num1 * num2
    return question, answer

def square_two_digit_numbers():
    num = random.randint(10, 99)
    question = f"{num}^2 = ?"
    answer = num * num
    return question, answer

topics = {
    "times_tables": times_tables,
    "multiply_by_11": multiply_by_11,
    "square_ending_in_5": square_ending_in_5,
    "multiply_same_first_digit_last_add_10": multiply_same_first_digit_last_add_10,
    "multiply_10_to_20": multiply_10_to_20,
    "square_two_digit_numbers": square_two_digit_numbers,
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_question', methods=['POST'])
def get_question():
    data = request.get_json()
    topic = data['topic']
    question, answer = topics[topic]()
    return jsonify({'question': question, 'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
