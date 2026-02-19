# main.py

from src.predict import run_prediction

if __name__ == "__main__":
    data_directory = "data"   # path to dataset folder

    accuracy, preds, labels = run_prediction(data_directory)

    print("\nMini GeoCLIP Results")
    print("----------------------")
    print(f"Accuracy: {accuracy * 100:.2f}%")