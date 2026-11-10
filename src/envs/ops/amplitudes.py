

from src.envs.generators import (
    AmplitudeGenerator,
)
from src.envs.tokenizers import IntegerTokenizer, ByteTokenizer


def build_amplitude(params):
    return {
        "problem_tokenizer": ByteTokenizer(['a','b','c','d','e','f']),
        "answer_tokenizer": IntegerTokenizer(params.base),
        "generator": AmplitudeGenerator(params),
    }




def register_amplitude_args(parser):
    parser.add_argument("--base", type=int, default=1000)




OPERATIONS = {
    "amplitude": {"build": build_amplitude, "register_args": register_amplitude_args},
}
