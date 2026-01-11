import io
import sys
import re
import json

def detect_input_prompts(code: str) -> list:
    """Detect all input() calls and extract their prompts."""
    # Match input() calls with optional prompt argument
    pattern = r'input\s*\(\s*([\'\"].*?[\'\"])?\s*\)'
    matches = re.findall(pattern, code)
    prompts = []
    for i, match in enumerate(matches):
        if match:
            # Remove quotes from prompt
            prompt = match.strip('\'"')
        else:
            prompt = f"Input #{i+1}"
        prompts.append(prompt)
    return prompts

def run_practice(code: str, user_inputs: dict = None) -> str:
    """Execute user code safely with support for input()."""
    # Detect input() calls
    prompts = detect_input_prompts(code)
    
    if prompts and not user_inputs:
        # Return a special marker indicating we need input from user
        return json.dumps({"need_input": True, "prompts": prompts})
    
    buf = io.StringIO()
    input_iter = iter(user_inputs.get('values', [])) if user_inputs else iter([])
    
    def mock_input(prompt=""):
        """Mock input function that uses provided values."""
        try:
            return next(input_iter)
        except StopIteration:
            return ""
    
    try:
        stdout = sys.stdout
        sys.stdout = buf
        env = {'input': mock_input, '__builtins__': __builtins__}
        exec(code, env, env)
        return buf.getvalue() or "Executed without output."
    except Exception as e:
        return f"Error: {e}"
    finally:
        sys.stdout = stdout
