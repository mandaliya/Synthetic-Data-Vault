from sdv.lite import SingleTablePreset
from sdv.metadata import SingleTableMetadata
from flask import Flask, jsonify

app = Flask(__name__)

# Define a sample metadata and synthesizer
def create_synthesizer():
    # Example metadata
    metadata = SingleTableMetadata()
    metadata.add_column(name='age', sdtype='numerical')
    metadata.add_column(name='gender', sdtype='categorical')
    metadata.add_column(name='income', sdtype='numerical')
    
    # Create a synthesizer
    synthesizer = SingleTablePreset(metadata, name='FAST_ML')
    synthesizer.fit(data={
        'age': [25, 30, 35, 40, 45],
        'gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
        'income': [50000, 60000, 80000, 70000, 90000]
    })
    
    return synthesizer

# Endpoint to generate synthetic data
@app.route('/generate', methods=['GET'])
def generate_data():
    synthesizer = create_synthesizer()
    synthetic_data = synthesizer.sample(num_rows=10)  # Generate 10 rows of synthetic data
    return jsonify(synthetic_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)