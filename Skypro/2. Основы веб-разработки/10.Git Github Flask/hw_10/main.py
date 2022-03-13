from flask import Flask
import utils

app = Flask(__name__)

candidates = utils.load_candidates()


@app.route('/')
def page_index():
    candidate_str = '<pre>'
    for candidate in candidates.values():
        candidate_str += f'{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n\n'
    candidate_str += '</pre>'
    return candidate_str


@app.route('/candidate/<int:id>')
def profile(id):
    candidate = candidates[id]
    candidate_str = f'<img src={candidate["picture"]}></img> <br><br>{candidate["name"]}<br>{candidate["position"]}<br>{candidate["skills"]}<br><br>'

    return candidate_str


@app.route('/skill/<skills>')
def skill(skills):
    candidate_str = '<pre>'

    for candidate in candidates.values():
        candidate_skills = candidate['skills'].lower()
        print(candidate_skills)
        if skills in candidate_skills:
            candidate_str += f'{candidate["name"]}<br>{candidate["position"]}<br>{candidate["skills"]}<br><br>'
    candidate_str += '</pre>'

    return candidate_str


app.run()
