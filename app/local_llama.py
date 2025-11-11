import os
try:
    from langchain_community.llms import LlamaCpp
except ImportError:
    LlamaCpp = None


def get_local_llama(model_path=None, **kwargs):
    model_path = model_path or os.getenv("LLAMA_MODEL_PATH")
    if not model_path:
        raise RuntimeError("LLAMA_MODEL_PATH not set")
    if LlamaCpp is None:
        raise RuntimeError("Install llama-cpp-python to use local LLaMA")
    return LlamaCpp(model_path=model_path, **kwargs)