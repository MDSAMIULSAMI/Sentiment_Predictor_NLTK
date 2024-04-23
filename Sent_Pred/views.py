from django.shortcuts import render,HttpResponse
import nltk
nltk.downloader.download('vader_lexicon')
# Create your views here.
def Sentiment_Predictor(request):
    from nltk.sentiment.vader import SentimentIntensityAnalyzer as SiD
    result = ''
    if request.method == "POST":
        sentence = request.POST['sent']
        print(sentence)
        sid = SiD()
        ss = sid.polarity_scores(sentence)
        ss.items()
        print(ss['compound'])
        if ss['compound'] > 0 and ss['compound']  != 0:
            print("Positive Sent")
            result = 'Positive Sentence'
        if ss['compound'] < 0 and ss['compound'] != 0:
            print("Negetive Sent")
            result = 'Negetive Sentence'
        if ss['compound'] == 0:
            print("Neutral Sent")
            result = 'Neutral Sentence'
        print(ss)
        return render(request, 'index.html', {'result':result , 'sents':sentence})
    return render(request, 'index.html')