from django.shortcuts import render, get_object_or_404, redirect
from .models import Data, Prediction
from .forms import DataForm
import pickle
import numpy as np


# Load the model from the pickle file
with open('./heart_pred_4.pk1', 'rb') as file:
    loaded_model = pickle.load(file)
    mean_values = loaded_model['mean']
    print(mean_values)

def heart_data(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            # Process the form data (save to database, perform calculations, etc.)
            instance = form.save(commit=False)

            # Replace missing values with mean values
            if instance.age in [None, '']:
                instance.age = round(mean_values['age'])
            if instance.chest_pain in [None, '']:
                instance.chest_pain = round(mean_values['chest pain type'])
            if instance.resting_bp in [None, '']:
                instance.resting_bp = round(mean_values['resting bp s'])
            if instance.cholesterol in [None, '']:
                instance.cholesterol = round(mean_values['cholesterol'])
            if instance.fasting_blood_suger in [None, '']:
                instance.fasting_blood_suger = round(mean_values['fasting blood sugar'])
            if instance.resting_ecg in [None, '']:
                instance.resting_ecg = round(mean_values['resting ecg'])
            if instance.max_heart_rate in [None, '']:
                instance.max_heart_rate = round(mean_values['max heart rate'])
            if instance.exercise_angina in [None, '']:
                instance.exercise_angina = round(mean_values['exercise angina'])
            if instance.oldpeak in [None, '']:
                instance.oldpeak = round(mean_values['oldpeak'])
            if instance.ST_slope in [None, '']:
                instance.ST_slope = round(mean_values['ST slope'])


            # Make predictions using the loaded model
            input_data = [
                instance.age,
                instance.gender,
                instance.chest_pain,
                instance.resting_bp,
                instance.cholesterol,
                instance.fasting_blood_suger,
                instance.resting_ecg,
                instance.max_heart_rate,
                instance.exercise_angina,
                instance.oldpeak,
                instance.ST_slope,
            ]
            print(input_data)
            input_data_array = np.array(input_data)
            print(input_data_array)
            print("Input Data Shape:", np.array(input_data).shape)
            prediction_value = loaded_model['model'].predict([input_data_array])[0]
            print(prediction_value)
            instance.save()
            # Save the predictions to the database
            Prediction.objects.create(data=instance, prediction=prediction_value)

            return redirect('success_page', pk=instance.pk)

    else:
        form = DataForm()
        

    return render(request, 'heart_data.html', {'form': form})


def success_page(request, pk):
    data_instance = get_object_or_404(Data, pk=pk)
    prediction_instance = Prediction.objects.get(data=data_instance)
    return render(request, 'success_page.html', {'data_instance': data_instance,'prediction_instance': prediction_instance.prediction})