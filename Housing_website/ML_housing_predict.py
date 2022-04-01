import sklearn


def housing_precict_model(bedrooms,bathrooms,toilets,parking_space,title,town,state):
    import pickle
    x=[[bedrooms,bathrooms,toilets,parking_space,title,town,state]]
    randomforst=pickle.load(open('housing_model.sav','rb'))
    predictions=randomforst.predict(x)
    print(predictions)
    prediction=predictions.tolist()
    print(prediction)
    for numbers in prediction:
        number=int(numbers)


        return number
