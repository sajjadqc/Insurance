import pickle
import numpy as np

__model = None

def load_saved_model():
    print("Model loading Started.....")

    global __model
    with open('model_pkl', 'rb') as f:
        __model = pickle.load(f)

    print('Model Loading Completed.')


def predict_charge(age, sex, bmi, children, smoker, region):
    columns = ['age', 'sex', 'bmi', 'children', 'smoker', 'northeast', 'northwest',
       'southeast', 'southwest']
    location_col = columns[5:]
    location_index = location_col.index(region)
    
    x = np.zeros(len(columns))
    x[0] = age
    if sex=='male':
        x[1] = 1
    else:
        x[1] = 0
    x[2] = bmi
    x[3] = children
    if smoker=='yes':
        x[4] = 1
    else:
        x[4] = 0
    x[location_index] = 1
    
    result =  __model.predict([x])[0]
    return int(result)


if __name__ == "__main__":
    load_saved_model()
    print(predict_charge(23, 'male', 28, 3, 'yes', 'southeast'))