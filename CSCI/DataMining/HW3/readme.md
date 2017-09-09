Q1) model.py file takes the filepath of the input data as an argument and then produces a file called 'model.txt' in the current directory. It additionally accepts an argument toggling whether to create a naive model or not. If the second parameter == "true", a naive model will be generated.

Q2) classify.py file looks for 'model.txt' in current directory, loads the model, then classifies the data found in a 'test' input data file, who's filepath is passed in by command line argument. It displays a confusion matrix after classification. This classifier works for both full and naive models.

