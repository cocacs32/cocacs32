import openai

class AIService:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def get_response(self, prompt):
        response = openai.ChatCompletion.create(
            model="claude",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']

# Usage Example
if __name__ == '__main__':
    api_key = 'your_anthropic_api_key'
    ai_service = AIService(api_key)
    prompt = 'What is the capital of France?'
    response = ai_service.get_response(prompt)
    print(response)