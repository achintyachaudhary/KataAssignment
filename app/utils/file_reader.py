def read_json(file_path):
    import json

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
