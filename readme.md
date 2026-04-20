Separation of Concerns (Very Important)
Each folder has a specific responsibility:

routes/ → handles URLs and logic (auth, tasks)
templates/ → HTML files (UI)
static/ → CSS, JS, images
models.py → database structure

👉 This keeps code clean instead of mixing everything in one file.


routes/ = rooms (different functions)
templates/ = decoration (UI)
static/ = furniture (CSS/JS)
models.py = foundation (data)

Blueprint Support (Modular Design)
Your routes/auth.py and routes/tasks.py likely use Blueprints.

👉 This allows:
Splitting app into modules
Reusing parts of code
Team collaboration

What __init__.py Does

👉 It creates and connects all parts of your app:
Flask app
Database
Blueprints (routes)
Config

run.py
   ↓
create_app()  (__init__.py)
   ↓
Create Flask app
   ↓
Attach database
   ↓
Import routes (auth, tasks)
   ↓
Register blueprints
   ↓
Return app
   ↓
App runs

💡 Simple Analogy

__init__.py = Manager

Creates company (Flask app)
Hires employees (routes)
Sets tools (database)
Starts work 🚀
✅ Final Summary

__init__.py:

Builds the app
Connects database
Links all routes
Returns a ready-to-run app


🔹 What is __init__.py?
__init__.py is a special file that makes a folder behave like a Python package.
👉 Without it → folder is just a folder
👉 With it → folder becomes a module/package you can import from

routes.py  ─┐
models.py  ─┼──> __init__.py ───> main app
utils.py   ─┘