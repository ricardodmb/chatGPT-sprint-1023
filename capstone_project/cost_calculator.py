#!/usr/bin/python3

class CostCalculator:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def cost_calculator_for_GPT_3_5_turbo(response) -> str:

        # These 2 values are valid only for the "gpt-3.5-turbo-1106" model.
        # Check https://openai.com/pricing for up-to-date prices
        cost_of_input_tokens = 0.001
        cost_of_output_tokens = 0.002

        completion_tokens = response['usage']['completion_tokens']
        prompt_tokens = response['usage']['prompt_tokens']

        total_cost = (
            (prompt_tokens * cost_of_input_tokens) + (completion_tokens * cost_of_output_tokens)
        ) / 1000
        print(response['usage'])

        return f"Total cost for API call: ${total_cost} USD"