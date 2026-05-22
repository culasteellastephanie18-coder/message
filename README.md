# Python + JavaScript Starter

Welcome! This workspace includes a simple setup for writing both Python and JavaScript.

## Files

- `main.py` - Python entry point that prints the letter and runs the JavaScript file.
- `script.js` - JavaScript file that prints the shared letter content from `letter.txt`.
- `letter.txt` - The actual birthday letter text shared by the user.
- `package.json` - Node package file with run scripts for JavaScript.
- `.gitignore` - Ignore Python `venv` and `node_modules`.

## Quick start

1. Open the workspace in VS Code.
2. Create a Python virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install any Python dependencies if needed.
4. Run the Python file:

   ```powershell
   python main.py
   ```

5. Run the JavaScript file directly with Node:

   ```powershell
   npm install
   npm run start
   ```

## Notes

- You can edit `main.py` and `script.js` to experiment with Python and JavaScript.
- If you want, I can also add a Flask/Express starter or a web UI next.
