class LLMClient:

    def ask(self, question):

        responses = {
            "Capital of India": "New Delhi",
            "Capital of France": "Paris"
        }

        return responses.get(
            question,
            "Unknown"
        )