import n2w
from django.shortcuts import render
from . import ML_housing_predict
import num2word

def home(request):
    return render (request,'index.html')

def result(request):
    bedrooms=int(request.GET['bedrooms'])
    bathrooms=int(request.GET['bathrooms'])
    toilets = int(request.GET['toilets'])
    parking_space = int(request.GET['parking_space'])
    title = int(request.GET['title'])
    town = int(request.GET['town'])
    state = int(request.GET['state'])

    prediction=ML_housing_predict.housing_precict_model(bedrooms,bathrooms,toilets,parking_space,title,town,state)
    currency = "₦{:,.2f}".format(prediction)
    currency_words=n2w.convert(prediction).title()+" {}".format('Naira').title()
    dollar=prediction/500
    dollars = "${:,.2f}.".format(dollar)
    dollars_words=n2w.convert(dollar).title()+" {}".format('dollars').title()
    return render(request,'result.html', {'prediction':prediction,
                                          'amount_naira':currency,
                                          'amount_dollar':dollars,
                                          'naira_word':currency_words,
                                          'dollar_word':dollars_words})




