import re

def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result


if __name__ == "main":
    # print(extract_session_id("projects/mira-chatbot-tbls/agent/sessions/f8aa73c6-9939-3873-6242-3eb21c0100f8/contexts/ongoing-order"))
    pass