import io
import sys

def run_practice(code: str) -> str:
    """Execute user code safely (minimal sandbox)."""
    buf = io.StringIO()
    try:
        stdout = sys.stdout
        sys.stdout = buf
        env = {}
        exec(code, env, env)
        return buf.getvalue() or "Executed without output."
    except Exception as e:
        return f"Error: {e}"
    finally:
        sys.stdout = stdout
