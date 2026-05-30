def evaluate_hallucination(
        response,
        expected
):

    if expected.lower() \
        in response.lower():

        return False

    return True