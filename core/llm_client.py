import time


class LLMClient:

    def ask(self, question):

        start = time.time()

        responses = {

            "Capital of India":
            "The capital of India is New Delhi",

            "Capital of France":
            "Paris",

            "Capital of Japan":
            "Tokyo"
        }

        answer = responses.get(
            question,
            "Unknown"
        )

        end = time.time()

        return {

            "answer": answer,

            "latency": end - start
        }