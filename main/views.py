from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot=ChatBot('chatbot',read_only=False,
                        logic_adapters=[
                            {

                                'import_path':'chatterbot.logic.BestMatch',
                                # 'default_response':"I'm Sorry I dont know what that means",
                                # 'maximum_similarity_threshold':0.90


                             }])


list_to_train = [
    "hi",
    "hi, there",
    "What's your name?",
    "I'm just a ChatBot",
    "What's is your favourite food",
    "I like Burger",
]

ChatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)
list = ['russian','english']
ChatterbotCorpusTrainer.train("chatterbot.corpus.english")
# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)


@login_required(login_url='/acc/login')
def index(request):
    return render(request,'main/index.html')
def specific(request):
    number = 55
    return HttpResponse(number)

def getResponce(request):
    userMessage = request.GET.get('userMessage')
    ChatResponse = str(bot.get_response(userMessage))
    return HttpResponse(ChatResponse)
# def article(request,article_id):
#     ctx={
#         'article_id':article_id
#     }
#     return render(request,'main/index.html',ctx)


