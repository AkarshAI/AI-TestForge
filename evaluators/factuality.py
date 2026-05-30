def evaluate_factuality(
        response,
        expected
):

    return expected.lower() \
        in response.lower()