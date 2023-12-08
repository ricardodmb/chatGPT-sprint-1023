#!/usr/bin/python3
from brain_module import ChatGPT
from cost_calculator import CostCalculator

class AnalyseFiles:
    bot = ChatGPT()
    cost_calc = CostCalculator()
    def __init__(self):
        pass

    @staticmethod
    def analyze_source_file(code_str:str):
        message = f"""
        I will give you a python dict with {{"name_of_file": "source_code"}}
        take source_code then transform the syntax to the other programming language (python from GO lang or viceversa)
        and give me a list of all the dependencies from the original code:
        {code_str}
        Include the response on the folowing json structure:
                {{
                "original_programming_language":
                "converted_programming_language":
                "suggested_script_name":
                "dependencies_list_from_original_code":
                "dependencies_list_from_converted_converted":
                "code":
                }}
                """
        response = AnalyseFiles.bot.request_openai(message ,"user")

        cost = AnalyseFiles.cost_calc.cost_calculator_for_GPT_3_5_turbo(response)
        print(cost)
        return response['choices'][0]['message']['content']