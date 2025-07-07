from flask import Flask, render_template, send_file
import subprocess
import os
from geofencing import Geofencing
from geopy.distance import great_circle
import define_constants as const

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/take-attendance')
def take_attendance():

    campus_center = (17.438188, 78.716631)  # Actual coordinates
    radius = 500  
    geofence = Geofencing(campus_center, radius)

    #current_location = (17.438200, 78.716635) #  college location
    current_location = (17.368211, 78.579437) #other location

    if not geofence.is_within_geofence(current_location):
        return "Attendance cannot be marked as you are outside the geofence."

    try:
        # Running backend scripts
        #subprocess.run(['python', 'encode_faces.py'], check=True)
        subprocess.run(['python', 'attendence_project.py'], check=True)

        #if not geofence.is_within_geofence(current_location):
        #    return "Attendance cannot be marked as you are outside the geofence."
        
        return "Attendance recorded successfully!"
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"

@app.route('/results/attendence.csv')
def view_attendance_sheet():
    # Adjust path to the attendance.csv file in the results folder
    attendance_path = os.path.join('results', 'attendence.csv')
    return send_file(attendance_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
