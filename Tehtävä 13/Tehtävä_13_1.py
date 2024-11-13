from flask import Flask, request

app = Flask(__name__)
@app.route('/prime/<num>')

def prime(num):
    num = int(num)
    if num > 1:
        for n in range(2, (num//2) +1):
            if num % n == 0:
                is_prime = False
                break
        else:
            is_prime = True
    else:
        is_prime = False
    result = {
        "number" : num,
        "is_prime" : is_prime
    }

    return result
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=4000)