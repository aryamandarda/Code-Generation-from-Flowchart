# Code Generation from Flowcharts

This project aims to help students with limited coding experience by converting flowchart images into executable Python code using Optical Character Recognition (OCR) and a Large Language Model (LLM). This tool simplifies the process of translating flowchart logic into code, making it easier for beginners to learn programming without getting bogged down by syntax.

## Abstract

Students often find it challenging to learn programming due to the complexity of syntax in various programming languages. Flowcharts help visualize algorithms but converting them into code can still be a hurdle. This project introduces a tool that takes flowchart images as input and generates corresponding Python code, including explanations. The tool uses deep learning models like ResNet and VGG for feature extraction, Long Short-Term Memory networks for sequence labeling, and Connectionist Temporal Classification algorithms for decoding. The extracted text is then processed by Llama-2-Chat, a large language model, to generate Python code. The application was tested with several flowchart images, achieving a 75% success rate in generating error-free code.

## Features

- Converts flowchart images to Python code
- Provides explanations of the generated code
- User-friendly interface built with Gradio
- Utilizes deep learning models for text extraction
- Employs Llama-2-Chat for code generation

## Installation

1. Clone the repository:
    ```bash git clone https://github.com/aryamandarda/Code-Generation-from-Flowchart.git```
3. Change to the project directory:
    ```bash cd Code-Generation-from-Flowchart```
4. Install the required dependencies:
    ```bash pip install -r requirements.txt```
   
## Usage

1. Run the application:
    ```bash python app.py```
2. Upload a flowchart image through the provided UI.
3. The application will display the generated Python code and its explanation.
4. Copy the code to your IDE and run it.

## Evaluation

The tool was evaluated with multiple flowchart images, and 75% of the generated Python codes were executed without errors, demonstrating its effectiveness in aiding students with programming tasks.

## Paper

For more detailed information, please refer to the paper [Code Generation from Flowchart using Optical Character Recognition & Large Language Model](https://www.techrxiv.org/users/766999/articles/853241-code-generation-from-flowchart-using-optical-character-recognition-large-language-model).
