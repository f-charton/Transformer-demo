

from src.envs.generators.base import Generator
import numpy as np

class AmplitudeGenerator(Generator):

    def __init__(self, params):
        self.base = params.base
        
    def generate(self, rng, is_train):
        return None

    def encode_class_id(self, problem_data, question_data, answer_data):
        return np.sign(answer_data)

    def read_func(self,problem_str, question_str, answer_str):
        try:
            value = int(answer_str)
        except Exception:
            return [], None, []

        base = self.base
        neg = value < 0
        value = -value if neg else value
        answer = []
        while True:
            rem = value % base
            value = value // base
            answer.append(str(rem))
            if value == 0:
                break
        tag = "INT-" if neg else "INT+"
        answer = [tag] + answer[::-1]
        return list(problem_str.strip()), None, answer

    def evaluate(self, problem, question, answer, hyp, metrics):
        if hyp is None:
            return {"is_valid": -1}
        if hyp == answer:
            return {"is_valid": 1, "correct_sign":1, "correct_module": 1}
        same_sign = (hyp * answer > 0)
        same_module = (abs(hyp) == abs(answer))
        res = {"is_valid": 0}
        res["correct_sign"]= 1 if same_sign else 0
        res["correct_module"]= 1 if same_module else 0
        return res
