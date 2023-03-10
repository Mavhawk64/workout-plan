import json

workouts = [{"Day": "Sunday","Workout":None},
            {"Day": "Monday", "Category": "Chest / Back / Biceps", "Workout": ["Incline DB Press (W1: 4x10-12 / W2: 4x8-10 / W3: 4x6-8)", "Barbell Row (W1: 4x10-12 / W2: 4x8-10 / W3: 4x6-8)", "Flat DB Press (SUPERSET) Lat Pulldown (12-15, 10-12, 8-10, DROPSET)", "Seated Row (SUPERSET) Cable Fly (12-15, 10-12, 8-10, DROPSET)", "Barbell Curl (W1: 4x12-15 / W2: 4x10-12 / W3: 4x8-10)"]},
            {"Day": "Tuesday", "Category": "Legs / Triceps", "Workout": ["Squat (W1: 4x10-12 / W2: 4x8-10 / W3: 4x6-8)", "Leg Press (15-20,12-15,10-12, DROPSET)",
                                                                                 "Leg Extension (SUPERSET) Hamstring Curl (4x15-20)", "Tricep Pushdown (12-15, 10-12, 8-10, DROPSET)", "French Press (SUPERSET) Calf Raise (3x10-12 & 3x15-20)"]},
            {"Day": "Wednesday", "Category": "Shoulders / Biceps", "Workout": ["LIGHT Seated Behind Neck Press (W1: 4x10-12 / W2: 4x8-10 / W3: 4x6-8)", "Machine Lateral Raises (4x12-15, DROPSET)",
                                                                               "CABLE LATERALS (SUPERSET) CABLE REVERSE FLY (SUPERSET) CABLE UPRIGHT ROW (3x12-15)", "Spider Curl or Bicep Machine (3x12-15)", "Free Bicep Exercise (3x?)"]},
            {"Day": "Thursday", "Category": "Chest / Back", "Workout": ["Bench Press (W1: 4x10-12 / W2: 4x8-10 / W3: 4x6-8)", "Neutral Grip Pulldown (W1: 4x10-12 / W2: 4x8-10 / W3: 4x6-8)",
                                                                                      "Incline Pause Bench Press (12-15, 10-12, 8-10)", "Chest Supported Row (12-15, 10-12, 8-10)", "Cable Row (SUPERSET) Pec Dec Fly (3x12-15)"]},
            {"Day": "Friday", "Category": "Shoulders / Legs / Triceps", "Workout": ["Standing Press (W1: 3x6 / W2: 4x6 / W3: 5x6)", "Smith Machine Squat (15-20, 12-15, 10-12, 8-10)", "Smith Machine Shoulder Press (4x12-15)", "DB Bulgarian Split Squat (10-12, 8-10, 6-8)", "Lateral Raise (SUPERSET) Romanian Deadlift (12-15, 10-12, 8-10, 8-10)", "DB Skull Crusher (3x10-12)"]},
            {"Day": "Saturday","Workout":None}]
my_json = {}
for workout in workouts:
    if workout["Workout"] == None:
        my_json[workout["Day"]] = None
        continue
    my_json[workout["Day"]] = {
        "Category": workout["Category"], "Exercises": []}
    x = workout["Workout"]

    for j, i in enumerate(x):
        i = i.replace("(SUPERSET)", "&")
        i = i[:-1].split('(')
        i = [x.strip() for x in i]
        exercise = i[0].replace("&", "(SUPERSET)")
        sets = i[1]
        my_exercise = {"Name": exercise,
                       "Type": "SUPERSET" if "(SUPERSET)" in exercise else "SINGLE"}

        for a, k in enumerate(exercise.split("(SUPERSET)")):
            k = k.strip()
            my_exercise[k.strip()] = {"Routine": []}
            if "W" in sets:
                for l in sets.split("/"):
                    my_exercise[k]["Routine"].append({})
                    l = l.replace("W1: ", "").replace("W2: ", "").replace(
                        "W3: ", "")
                    my_exercise[k]["Routine"][-1]["Sets"] = int(l.split("x")[0])*[{"Type": "Count", "Reps": l.split(
                        "x")[1].strip(), "Weight":None, "Previous Weight":None}]
            elif "x" in sets and "," not in sets:
                my_exercise[k]["Routine"].append({})
                b = sets.split("&")[a] if "&" in sets else sets
                my_exercise[k]["Routine"][-1]["Sets"] = int(b.split("x")[0])*[{"Type": "Count", "Reps": b.split(
                    "x")[1].strip(), "Weight":None, "Previous Weight":None}]
            elif "x" not in sets:
                my_exercise[k]["Routine"].append({"Sets": []})
                for l in sets.split(","):
                    if l.strip() != "DROPSET":
                        my_exercise[k]["Routine"][0]["Sets"].append(
                            {"Type": "Count", "Reps": l.strip(), "Weight": None, "Previous Weight": None})
                    else:
                        my_exercise[k]["Routine"][0]["Sets"].append({"Type": "DROPSET", "Reps": {"1": "6-8", "2": "6-8", "3": "6-8"}, "Weight": {
                            "1": None, "2": None, "3": None}, "Previous Weight": {"1": None, "2": None, "3": None}})
            else:
                my_exercise[k]["Routine"].append({})
                for l in sets.split(","):
                    if l.strip() != "DROPSET":
                        my_exercise[k]["Routine"][-1]["Sets"] = int(l.split("x")[0])*[{"Type": "Count", "Reps": l.split(
                            "x")[1].strip(), "Weight": None, "Previous Weight": None}]
                    else:
                        my_exercise[k]["Routine"][-1]["Sets"].append({"Type": "DROPSET", "Reps": {"1": "6-8", "2": "6-8", "3": "6-8"}, "Weight": {
                            "1": None, "2": None, "3": None}, "Previous Weight": {"1": None, "2": None, "3": None}})

        my_json[workout["Day"]]["Exercises"].append(my_exercise)

# print my_json with indent 4
print(json.dumps(my_json, indent=4))

# output to json file: output.json
with open('sample.json', 'w') as outfile:
    json.dump(my_json, outfile, indent=4)
