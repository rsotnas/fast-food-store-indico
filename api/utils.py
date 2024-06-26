def check_keys(data, mode="all"):
    KEYS = ['establishedyear', 'location', 'owner', 'storeid', 'numberofemployees']
    if mode == "all":
        return [key for key in KEYS if key not in data]
    else:
        return [key for key in KEYS if key not in data and key != 'storeid']
    # missing_keys = [key for key in KEYS if key not in data]
    # if missing_keys:
    #     return f"Missing keys: {', '.join(missing_keys)}"