document.getElementById('prediction-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Get form data
    const formData = {
        Type: document.getElementById('type').value,
        'Air temperature [K]': document.getElementById('air_temp').value,
        'Process temperature [K]': document.getElementById('process_temp').value,
        'Rotational speed [rpm]': document.getElementById('rotational_speed').value,
        'Torque [Nm]': document.getElementById('torque').value,
        'Vibration Levels': document.getElementById('vibration').value,
        'Operational Hours': document.getElementById('operational_hours').value
    };

    // Make API request
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        resultDiv.textContent = `Prediction: ${data.prediction}`;
        resultDiv.classList.add('visible');
    })
    .catch(error => {
        console.error('Error:', error);
        const resultDiv = document.getElementById('result');
        resultDiv.textContent = 'Error making prediction. Please try again.';
        resultDiv.classList.add('visible');
    });
});

// Random value generator
document.getElementById('random-values').addEventListener('click', function() {
    const randomData = {
        type: (Math.random() * 2).toFixed(2),
        air_temp: (295 + Math.random() * 15).toFixed(2),
        process_temp: (305 + Math.random() * 10).toFixed(2),
        rotational_speed: (1000 + Math.random() * 2000).toFixed(2),
        torque: (10 + Math.random() * 70).toFixed(2),
        vibration: (1 + Math.random() * 9).toFixed(2),
        operational_hours: (Math.random() * 10000).toFixed(2)
    };
    
    document.getElementById('type').value = randomData.type;
    document.getElementById('air_temp').value = randomData.air_temp;
    document.getElementById('process_temp').value = randomData.process_temp;
    document.getElementById('rotational_speed').value = randomData.rotational_speed;
    document.getElementById('torque').value = randomData.torque;
    document.getElementById('vibration').value = randomData.vibration;
    document.getElementById('operational_hours').value = randomData.operational_hours;
});
