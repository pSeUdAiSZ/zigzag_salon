import os
import sys
import json

# Set up Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zigzag_app.settings')
import django
django.setup()

from salonmanager.models import Customer, Branch, StaffMember  # Import your models

def import_data():
    file_path = 'C:\_MyDrive\Cloned_zigzag_salon_app\zigzag_salon\dbdata.json'  # Replace with the correct path to your JSON file

    with open(file_path) as f:
        data = json.load(f)

    for obj in data:
        # Create objects for each model and save them
        model1_data = obj.get('model1_fields')
        if model1_data:
            model1 = Customer(**model1_data)
            model1.save()

        model2_data = obj.get('model2_fields')
        if model2_data:
            model2 = Branch(**model2_data)
            model2.save()

        model3_data = obj.get('model3_fields')
        if model3_data:
            model3 = StaffMember(**model3_data)
            model3.save()

    print('Data imported successfully!')

if __name__ == '__main__':
    import_data()
