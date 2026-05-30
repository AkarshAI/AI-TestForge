class LLMClient:

    def ask(self, question):

        responses = {

            "Capital of India":
                "New Delhi",

            "Capital of France":
                "Paris",

            "Capital of Japan":
                "Tokyo"
        }

        return responses.get(
            question,
            "Unknown"
        )