import gradio as gr
from utils import *

def generate(uploaded_image):
    uploaded_image_path = uploaded_image.name
    img = read_image(uploaded_image_path)
    img_text = detect_text(img)
    python_code_query = "Generate the python code from the below given content : \n"
    pseudo_code_query, python_code_query = create_queries(img_text, pseudo_code_query, python_code_query)
    _, python_code_output = generate_code(pseudo_code_query, python_code_query)
    python_code = display_python_code(python_code_output)
    return img, python_code

def main(): 
    io = gr.Interface(
        fn=generate,
        inputs=gr.File(label="Upload the image of your flowchart", file_types = ["image"]),
        outputs = [gr.Image(label = "Uploaded Image", width = 400, height = 400), 
                   gr.Textbox(label="Python Code For The Uploaded Flowchart", show_copy_button = True, multiline = True)],
        allow_flagging="manual",
        flagging_options=["Save"],
        title="Code Generation from Flowchart using Image Processing and Large Language Model",
        description="Effortlessly Generate Python Codes For Your Flowcharts",
        theme = gr.themes.Soft()
    )
    io.launch(share=True)

if __name__ == "__main__":
    main()