import cv2
import easyocr
import os
import replicate

def read_image(image_path):
    img = cv2.imread(image_path)
    return img

def detect_text(img):
    reader = easyocr.Reader(['en'], gpu=False)
    img_text = reader.readtext(img)
    return img_text

def create_queries(img_text, pseudo_code_query, python_code_query):
    for text in img_text:
        _, text, _ = text
        pseudo_code_query = '"# ' + pseudo_code_query + text + "\n"
        python_code_query = '"# ' + python_code_query + text + "\n"
    pseudo_code_query = pseudo_code_query + '\ndef"'
    python_code_query = python_code_query + '\ndef"'
    return pseudo_code_query, python_code_query

def generate_code(pseudo_code_query, python_code_query):
    os.environ["REPLICATE_API_TOKEN"] = "r8_HYSfYgUMu2HkpP8hxGee8XDCzds5TwU1JwN81"
    api = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])
    pseudo_code_output = api.run(
        "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
        input={"prompt": pseudo_code_query}
    )
    python_code_output = api.run(
        "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
        input={"prompt": python_code_query}
    )
    return pseudo_code_output, python_code_output

def display_python_code(python_code_output):
    python_code = ""
    for item in python_code_output:
        python_code = python_code + item
    return python_code
    
def main():
    pass

if __name__ == "__main__":
    main()
