from flask import Flask, render_template
import json
import utils

app = Flask(__name__)
candidates = utils.load_candidates()

@app.route("/")
def load_candidates_from_json():
    str_candidates = [candidate for candidate in candidates.values()]
    return render_template('list.html', str_candidates=str_candidates)

@app.route("/candidate/<int:candidate_id>")
def get_candidate(candidate_id):
    for candidate in candidates.values():
        if candidate['id'] == candidate_id:
            return  render_template('single.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def get_candidates_by_name(candidate_name):
    str_candidates = [candidate for candidate in candidates.values() if candidate_name in candidate['name'].lower()]
    return  render_template('search.html', str_candidates=str_candidates, l=len(str_candidates))


@app.route("/skill/<skill_name>")
def get_candidates_by_skill(skill_name):
    str_candidates = []
    for candidate in candidates.values():
        candidate['skills'] = [i.lower() for i in candidate['skills'].split(', ')]
        if skill_name in candidate['skills']:
            str_candidates.append(candidate)
    return  render_template('skill.html', str_candidates=str_candidates, l=len(str_candidates), skill=skill_name)

app.run()
