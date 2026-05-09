test_setting = {
    "theme" : "dark",
    "language" : "English",
    "notification" : "on"
}

def add_setting(test_setting, tuple_data):
    key = tuple_data[0].lower()
    value = tuple_data[1].lower()

    if key in test_setting:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name"
    
    test_setting[key] = value
    return f"Setting '{key}' added with '{value}' successfully!"

def update_setting(test_setting, tuple_data):
    key = tuple_data[0].lower()
    value = tuple_data[1].lower()

    if key in test_setting:
        test_setting[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting"
    
def delete_setting(test_setting, key):
    key = key.lower()

    if key in test_setting:
        del test_setting[key]
        return f"Setting '{key}' deleted successfully!"

    else:
        return f"Setting not found!"
    
def view_settings(test_setting):
    if not test_setting:
        return f"No settings available."
    else:
        result = "Current User Settings:"
        for key, value in test_setting.items():
            result += f"\n{key.capitalize()}: {value}"
        return result

print(add_setting(test_setting, ("volume", "high")))
print(update_setting(test_setting, ("theme", "light")))
print(view_settings(test_setting))
print(delete_setting(test_setting, "volume"))
print(view_settings(test_setting))