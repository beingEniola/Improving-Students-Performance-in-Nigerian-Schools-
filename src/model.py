from catboost import CatBoostClassifier


# Define the Model class
class Model:
    
    def __init__(self):
        """
        Initialize the model class by defining the model path and loading the pre-trained CatBoost model.
        """
        # Define the path to the saved CatBoost model file.
        self.model_path = "catboost_model.cbm"
        
        # Create an instance of the CatBoostClassifier model.
        print("Creating a new instance of the CatBoost model...")
        self.model = CatBoostClassifier()
        
        # Load the model during initialization.
        self.load_model()

    def load_model(self):
        """
        Load the model from the specified path and print a confirmation message.
        """
        try:
            print(f"\nLoading the saved model from: {self.model_path}...")
            self.model.load_model(self.model_path)
            print("The saved model has been loaded successfully!\n")
            
        except Exception as e:
            print(f"An error occurred while loading the model: {e}")

    def prediction(self, input_data):
        """
        Use the loaded model to make predictions on the given input data.
        
        Args:
            input_data: The input data for making predictions.
        
        Returns:
            The predicted output based on the input data.
        """
        try:
            print("\nMaking predictions on the input data...")
            predictions = self.model.predict(data=input_data)
      
            return predictions
        
        except Exception as e:
            print(f"An error occurred while making predictions: {e}")

    def prediction_probability(self, input_data):
        """
        Use the loaded model to make prediction probability on the given input data.
        
        Args:
            input_data: The user's input data.
        
        Returns:
            The probability output based on the input data.
        """
        try:
            print("\nMaking prediction probability on the input data...")
            prediction_proba = self.model.predict_proba(input_data)
        
            return prediction_proba
        
        except Exception as e:
            print(f"An error occurred while calculating prediction probability: {e}")
