import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from ultralytics import YOLO
import cv2
import numpy as np
import math

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESULT_FOLDER'] = 'results'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Ensure the upload and result folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

# Load the YOLO model
model = YOLO("best.pt")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def calculate_area(bbox, image_shape):
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    pixel_area = width * height
    area_sq_meters = pixel_area * 0.01
    return area_sq_meters

def estimate_solar_potential(area):
    solar_panel_efficiency = 0.20
    average_solar_irradiance = 1000  # W/m^2
    potential_power = area * solar_panel_efficiency * average_solar_irradiance
    return potential_power

def calculate_solar_panels(area):
    typical_panel_area = 1.7
    installation_factor = 0.9
    num_panels = math.floor((area * installation_factor) / typical_panel_area)
    return num_panels

def calculate_annual_savings(solar_potential, electricity_bill):
    monthly_energy_production = solar_potential * 24 * 30  # kWh per month
    annual_energy_production = monthly_energy_production * 12
    annual_bill = electricity_bill * 12
    
    # Assuming the solar energy replaces grid electricity
    annual_savings = min(annual_bill, annual_energy_production * 0.1)  # Assuming $0.1 per kWh
    return annual_savings

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    
    electricity_bill = float(request.form.get('electricity_bill', 0))
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        results = model(filepath)
        
        result_filename = f"result_{filename}"
        result_path = os.path.join(app.config['RESULT_FOLDER'], result_filename)
        
        result = results[0]
        result_image = result.plot()
        cv2.imwrite(result_path, result_image)
        
        image = cv2.imread(filepath)
        total_area = 0
        for box in result.boxes:
            bbox = box.xyxy[0].tolist()
            area = calculate_area(bbox, image.shape)
            total_area += area
        
        solar_potential = estimate_solar_potential(total_area)
        num_panels = calculate_solar_panels(total_area)
        annual_savings = calculate_annual_savings(solar_potential / 1000, electricity_bill)  # Convert W to kW
        
        return render_template('index.html', 
                               result_image=f"/results/{result_filename}", 
                               area=f"{total_area:.2f}",
                               solar_potential=f"{solar_potential:.2f}",
                               num_panels=num_panels,
                               annual_savings=f"{annual_savings:.2f}")
    return 'Invalid file type'

@app.route('/results/<filename>')
def serve_result(filename):
    return send_file(os.path.join(app.config['RESULT_FOLDER'], filename))

if __name__ == '__main__':
    app.run(debug=True)