from .lib.inference import EXAMPLE_FILE, Inference_result

def score(file_path):
    return Inference_result(EXAMPLE_FILE)