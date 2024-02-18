import gradio as gr
import time
from ctransformers import AutoModelForCausalLM


def load_llm():
    return AutoModelForCausalLM.from_pretrained(
        model_path_or_repo_id = 'codellama-13b.Q4_0.gguf',
        model_type = 'llama',
        max_new_tokens = 1096,
        repetition_penalty = 1.13,
        temperature = 0.1,
    )

def llm_function(message, chat_history):
    llm = load_llm()
    response = llm(message)
    output_text = response
    
    return output_text

title = 'CodeLlama 13B GGUF Demo'

examples = [
    'Write a java program to connect with a SQL database and list down all the tables.',
    'Write a python program to train a linear regression model using scikit-learn',
    'Write a c++ code to implement a binary tree',
    'What are the benefits of C++ for deep learning programming'
]

gr.ChatInterface(
    fn = llm_function,
    title = title,
    examples = examples,
).launch()