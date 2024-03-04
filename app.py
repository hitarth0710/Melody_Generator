# from flask import Flask, request, jsonify, render_template
# from melodygenerator import MelodyGenerator
# from preprocess import SEQUENCE_LENGTH
# import music21 as m21
# import os
# import random

# app = Flask(__name__)
# mg = MelodyGenerator()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/generate-melody', methods=['GET'])
# def generate_melody():
#     seed = request.args.get('seed')
#     format = request.args.get('format', 'midi')

#     # Generate melody using your MelodyGenerator class
#     melody = mg.generate_melody(seed, 500, SEQUENCE_LENGTH, 0.3)

#     # Save the melody
#     file_name=f"{generate_random_filename()}.{format}"
#     mg.save_melody(melody, file_name=file_name)

#     path='generated_melodies'
#     file = file_name

#     song = m21.converter.parse(os.path.join(path, file))
#     song.show()

#     return jsonify({'melodyLink': file_name})

# def generate_random_filename(prefix="melody", number_length=5):
#     random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(number_length))
#     return f"{prefix}{random_numbers}"


# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify, render_template
from preprocess import SEQUENCE_LENGTH
import music21 as m21
from melodygenerator import MelodyGenerator
import os
import random


app = Flask(__name__)
SELECTED_DATA=""
@app.route("/get-melody" , methods=["GET"])
def getMelody():
    SELECTED_DATA = request.args.get("data")
    if SELECTED_DATA == "midi":
        print("SELECTED GERMANY")
        from melodygenerator import MelodyGenerator
    elif SELECTED_DATA == "Romania":
        print("SELECTED ROMANAIN")
        from melodygenerator_romania import MelodyGenerator
    elif SELECTED_DATA == "England": 
        print("SELECTED ENGLAND")
        from melodygenerator_england import MelodyGenerator
    elif SELECTED_DATA == "India": 
        print("SELECTED INDIAN")
        from melodygenerator_india import MelodyGenerator
    else: 
        from melodygenerator import MelodyGenerator    
    return jsonify({SELECTED_DATA:SELECTED_DATA})
 

mg = MelodyGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-melody', methods=['GET'])
def generate_melody():
    seed = request.args.get('seed')
    format = request.args.get('format', 'midi')

    print(f"MMMMMM {format}")

    # Generate melody using your MelodyGenerator class
    melody = mg.generate_melody(seed, 500, SEQUENCE_LENGTH, 0.3)

    # Save the melody
    file_name=f"{generate_random_filename()}.midi"
    mg.save_melody(melody, file_name=file_name)

    path='generated_melodies'
    file = file_name

    song = m21.converter.parse(os.path.join(path, file))
    song.show()

    return jsonify({'melodyLink': file_name})

def generate_random_filename(prefix="melody", number_length=5):
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(number_length))
    return f"{prefix}{random_numbers}"


if __name__ == '__main__':
    app.run(debug=True)
