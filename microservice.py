
from flask import Flask, request

app = Flask(__name__)

exercises = [
    {"name": "dip", "muscle_group": ["chest", "triceps", "front delts"], "movement": "push"},
    {"name": "pull-up", "muscle_group": ["back", "biceps"], "movement": "pull"},
    {"name": "squat", "muscle_group": ["quads", "glutes"], "movement": "push"},
    {"name": "bench press", "muscle_group": ["chest", "triceps"], "movement": "push"},
    {"name": "deadlift", "muscle_group": ["back", "glutes", "hamstrings"], "movement": "pull"},
    {"name": "overhead press", "muscle_group": ["shoulders", "triceps"], "movement": "push"},
    {"name": "barbell row", "muscle_group": ["back", "biceps"], "movement": "pull"},
    {"name": "lunges", "muscle_group": ["quads", "glutes", "hamstrings"], "movement": "push"},
    {"name": "push-up", "muscle_group": ["chest", "triceps", "shoulders"], "movement": "push"},
    {"name": "lat pulldown", "muscle_group": ["back", "biceps"], "movement": "pull"},
    {"name": "romanian deadlift", "muscle_group": ["hamstrings", "glutes"], "movement": "pull"},
    {"name": "incline bench press", "muscle_group": ["chest", "triceps", "shoulders"], "movement": "push"},
    {"name": "calf raise", "muscle_group": ["calves"], "movement": "push"},
    {"name": "face pull", "muscle_group": ["rear delts", "traps"], "movement": "pull"},
    {"name": "plank", "muscle_group": ["core"], "movement": "static"},
    {"name": "sit-up", "muscle_group": ["core"], "movement": "push"},
    {"name": "bicep curl", "muscle_group": ["biceps"], "movement": "pull"},
    {"name": "tricep extension", "muscle_group": ["triceps"], "movement": "push"},
    {"name": "side lateral raise", "muscle_group": ["shoulders"], "movement": "push"},
    {"name": "leg press", "muscle_group": ["quads", "glutes", "hamstrings"], "movement": "push"},
    {"name": "glute bridge", "muscle_group": ["glutes", "hamstrings"], "movement": "push"},
    {"name": "chin-up", "muscle_group": ["back", "biceps"], "movement": "pull"},
    {"name": "step-up", "muscle_group": ["quads", "glutes"], "movement": "push"},
    {"name": "hip thrust", "muscle_group": ["glutes", "hamstrings"], "movement": "push"},
    {"name": "shrug", "muscle_group": ["traps"], "movement": "pull"},
    {"name": "reverse fly", "muscle_group": ["rear delts", "traps"], "movement": "pull"},
    {"name": "hammer curl", "muscle_group": ["biceps", "forearms"], "movement": "pull"},
    {"name": "front raise", "muscle_group": ["front delts"], "movement": "push"},
    {"name": "cable row", "muscle_group": ["back", "biceps"], "movement": "pull"},
    {"name": "mountain climbers", "muscle_group": ["core", "hip flexors"], "movement": "dynamic"},
    {"name": "burpee", "muscle_group": ["full body"], "movement": "dynamic"},
    {"name": "box jump", "muscle_group": ["quads", "glutes", "calves"], "movement": "push"},
    {"name": "wall sit", "muscle_group": ["quads"], "movement": "static"},
    {"name": "bicycle crunch", "muscle_group": ["core", "obliques"], "movement": "dynamic"},
    {"name": "clamshell", "muscle_group": ["glutes", "hip abductors"], "movement": "push"},
    {"name": "farmer’s carry", "muscle_group": ["forearms", "traps", "core"], "movement": "static"},
    {"name": "turkish get-up", "muscle_group": ["core", "shoulders"], "movement": "dynamic"},
    {"name": "good morning", "muscle_group": ["hamstrings", "glutes", "lower back"], "movement": "pull"},
    {"name": "sled push", "muscle_group": ["quads", "glutes", "hamstrings"], "movement": "push"},
    {"name": "kettlebell swing", "muscle_group": ["glutes", "hamstrings", "core"], "movement": "dynamic"},
    {"name": "medicine ball slam", "muscle_group": ["core", "shoulders"], "movement": "dynamic"},
    {"name": "high pull", "muscle_group": ["traps", "shoulders", "biceps"], "movement": "pull"},
    {"name": "snatch", "muscle_group": ["full body"], "movement": "dynamic"},
    {"name": "clean and jerk", "muscle_group": ["full body"], "movement": "dynamic"},
    {"name": "thruster", "muscle_group": ["quads", "shoulders", "glutes"], "movement": "push"},
    {"name": "pistol squat", "muscle_group": ["quads", "glutes", "core"], "movement": "push"},
    {"name": "z-press", "muscle_group": ["shoulders", "core"], "movement": "push"},
    {"name": "copenhagen plank", "muscle_group": ["adductors", "core"], "movement": "static"},
    {"name": "ab rollout", "muscle_group": ["core", "lats"], "movement": "pull"},
    {"name": "scapular pull-up", "muscle_group": ["traps", "lats"], "movement": "pull"}
]


def search_and_sort_exercises(query='', sort=''):
    query = query.lower()
    filtered = [ex for ex in exercises if query in ex['name'].lower()]

    if sort == 'asc':
        filtered.sort(key=lambda x: x['name'])
    elif sort == 'desc':
        filtered.sort(key=lambda x: x['name'], reverse=True)

    return filtered

@app.route('/exercises', methods=['GET'])
def get_exercises():
    search = request.args.get('search', '')
    sort = request.args.get('sort', '')
    results = search_and_sort_exercises(search, sort)

   
    if not results:
        return "No exercises found.\n", 200

    lines = []
    for ex in results:
        line = f"Name: {ex['name']} Muscle Group: {', '.join(ex['muscle_group'])} Movement: {ex['movement']}"
        lines.append(line)

    return "\n".join(lines) + "\n", 200

if __name__ == '__main__':
    print("Running tested.py microservice on http://localhost:5001")
    app.run(port=5001)


