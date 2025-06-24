# from flask import Flask, render_template, request
# import google.generativeai as genai

# app = Flask(__name__)



# # ✅ Replace the key below with your real API key
# GEMINI_API_KEY = "AIzaSyAf12EIeiVxABVA5gdaHO-FhbuNq4swRx8"
# genai.configure(api_key=GEMINI_API_KEY)

# # ✅ Use the model you want
# model = genai.GenerativeModel("gemini-2.0-flash-exp")


# def generate_timetable(user_schedule):
#     prompt = f"""
# You're a smart, helpful assistant. Based on the user's schedule, responsibilities, and preferences, build a daily timetable that's balanced and productive.

# Here is the user's input:
# {user_schedule}

# Return a clear, human-readable schedule with proper time blocks and task names. Add breaks appropriately and maintain a good flow throughout the day.
# """
#     response = model.generate_content(prompt)
#     return response.text

# @app.route("/", methods=["GET", "POST"])
# def index():
#     timetable = ""
#     error = ""
#     if request.method == "POST":
#         user_input = request.form.get("user_input", "")
#         if not user_input.strip():
#             error = "Please enter your schedule first."
#         else:
#             try:
#                 timetable = generate_timetable(user_input)
#             except Exception as e:
#                 error = f"Error: {str(e)}"
#     return render_template("index.html", timetable=timetable, error=error)

# if __name__ == "__main__":
#     app.run(debug=True)






# from flask import Flask, render_template, request
# import google.generativeai as genai

# app = Flask(__name__)

# # ✅ Replace with your actual Gemini API key
# GEMINI_API_KEY = "AIzaSyAf12EIeiVxABVA5gdaHO-FhbuNq4swRx8"
# genai.configure(api_key=GEMINI_API_KEY)

# model = genai.GenerativeModel("gemini-2.0-flash-exp")

# def generate_timetable(user_schedule):
#     prompt = f"""
# You're a smart, helpful assistant. Based on the user's schedule, responsibilities, and preferences, build a daily timetable that's balanced and productive.

# Here is the user's input:
# {user_schedule}

# Return a clear, human-readable schedule with proper time blocks and task names. Add breaks appropriately and maintain a good flow throughout the day.
# """
#     response = model.generate_content(prompt)
#     return response.text

# @app.route("/dashboard", methods=["GET"])
# def dashboard_page():
#     return render_template("dashboard.html")

# @app.route("/", methods=["GET", "POST"])
# def index():
#     timetable = ""
#     error = ""
#     if request.method == "POST":
#         user_input = request.form.get("user_input", "")
#         if not user_input.strip():
#             error = "Please enter your schedule first."
#         else:
#             try:
#                 timetable = generate_timetable(user_input)
#             except Exception as e:
#                 error = f"Error: {str(e)}"
#         return render_template("dashboard.html", timetable=timetable, error=error)

#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, render_template, request
# import google.generativeai as genai

# app = Flask(__name__)

# # Your Gemini API key
# GEMINI_API_KEY = "AIzaSyAf12EIeiVxABVA5gdaHO-FhbuNq4swRx8"
# genai.configure(api_key=GEMINI_API_KEY)

# model = genai.GenerativeModel("gemini-2.0-flash-exp")

# def generate_timetable(user_schedule):
#     prompt = f"""
# You're a smart, helpful assistant. Based on the user's schedule, responsibilities, and preferences, build a daily timetable that's balanced and productive.

# Here is the user's input:
# {user_schedule}

# Return a clear, human-readable schedule with proper time blocks and task names. Add breaks appropriately and maintain a good flow throughout the day.
# """
#     response = model.generate_content(prompt)
#     return response.text

# @app.route("/", methods=["GET", "POST"])
# def index():
#     timetable = ""
#     error = ""
#     if request.method == "POST":
#         user_input = request.form.get("user_input", "")
#         if not user_input.strip():
#             error = "Please enter your schedule first."
#         else:
#             try:
#                 timetable = generate_timetable(user_input)
#             except Exception as e:
#                 error = f"Error: {str(e)}"
#         return render_template("dashboard.html", timetable=timetable, error=error)

#     return render_template("index.html")

# # ✅ NEW: This is the missing route
# @app.route("/dashboard", methods=["GET", "POST"])
# def dashboard_page():
#     timetable = ""
#     error = ""

#     if request.method == "POST":
#         user_input = request.form.get("user_input", "")
#         if not user_input.strip():
#             error = "Please enter your schedule first."
#         else:
#             try:
#                 timetable = generate_timetable(user_input)
#             except Exception as e:
#                 error = f"Error: {str(e)}"

#     return render_template("dashboard.html", timetable=timetable, error=error)


# if __name__ == "__main__":
#     app.run(debug=True)



# from flask import Flask, render_template, request
# import openai

# app = Flask(__name__)

# # ✅ Your OpenAI API key
# openai.api_key = "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"  # Replace with your key

# # ✅ Function to generate timetable using OpenAI GPT-3.5
# def generate_timetable(user_schedule):
#     prompt = f"""
# You are a smart, helpful assistant. Based on the user's schedule, responsibilities, and preferences, build a daily timetable that's balanced and productive.

# Here is the user's input:
# {user_schedule}

# Return a clear, human-readable schedule with proper time blocks and task names. Add breaks appropriately and maintain a good flow throughout the day.
# """
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return response.choices[0].message.content.strip()


from flask import Flask, render_template, request

app = Flask(__name__)

# ✅ Dummy AI response generator
def generate_timetable(user_schedule):
    return f"""📅 AI Timetable based on your input:

{user_schedule}

🕘 9:00 AM – Wake up and freshen up  
🕙 10:00 AM – Study Python  
🕛 12:00 PM – Lunch break  
🕐 1:00 PM – DSA Practice  
🕒 3:00 PM – Project Work  
🕕 6:00 PM – Gym or physical activity  
🕗 8:00 PM – Dinner  
🕘 9:00 PM – Review & plan for next day  
🛏️ 10:30 PM – Sleep
"""

# ✅ Home route (index.html)
@app.route("/", methods=["GET", "POST"])
def index():
    timetable = ""
    error = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        if not user_input.strip():
            error = "Please enter your schedule first."
        else:
            timetable = generate_timetable(user_input)
        return render_template("dashboard.html", timetable=timetable, error=error)

    return render_template("index.html")

# ✅ Dashboard route
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard_page():
    timetable = ""
    error = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        if not user_input.strip():
            error = "Please enter your schedule first."
        else:
            timetable = generate_timetable(user_input)
    return render_template("dashboard.html", timetable=timetable, error=error)

# ✅ Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
