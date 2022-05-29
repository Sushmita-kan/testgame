from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.sessions.models import Session
import itertools
#import enchant 
from english_words import english_words_set
import random
# from django.forms.models import model_to_dict

# Create your views here.
def home(request):
	return render(request,'home.html',{})

def base(request):
	return render(request,'base.html',{})

def UserLogin(request):
    if request.method == "POST":
        C_name = request.POST['U_name']
        C_password = request.POST['U_pwds']
        if UserDetails.objects.filter(Username=C_name, Password=C_password).exists():
            user = UserDetails.objects.all().filter(Username=C_name, Password=C_password)
            messages.info(request, 'logged in')
            request.session['UserId'] = user[0].id
            request.session['type_id'] = 'User'
            request.session['UserType'] = C_name
            request.session['login'] = "Yes"
            return redirect("/")
        else:
            messages.info(request, 'Please Register')
            return redirect("/UserRegisteration")
    else:
        return render(request,'UserLogin.html',{})
    return render(request,'UserLogin.html',{})

def UserRegisteration(request):
    if request.method == "POST":
        F_name = request.POST['fname']
        L_name = request.POST['lname']
        U_mobile = request.POST['phone']
        U_email = request.POST['Eid']
        U_username = request.POST['uname']
        U_password = request.POST['pwd']
        if  UserDetails.objects.filter(Email = U_email ,Username = U_username).exists():
            myObjects = UserDetails.objects.all().filter(Email = U_email ,Username = U_username )
            name = myObjects[0].Username
            messages.error(request,'Already Registered Please Login')
            return render(request,'UserLogin.html',{})
        else:
            users = UserDetails(Firstname = F_name, Lastname= L_name, Phone =  U_mobile, Email =  U_email, Username = U_username, Password= U_password)
            users.save()
            messages.info(request,'Registered Sucessfully')
            return render(request,'UserLogin.html',{})
    else:
        return render(request,'UserRegisteration.html',{})
    

def Logout(request):
    Session.objects.all().delete()
    return redirect("/")

def WordScrabble(request):
    if request.method == "POST":
        meaningful = []
        nonmeaningful = []
        # d = enchant.Dict("en_US")
        s = request.POST['Word']
        print(s)
        lent = len(s)
        print('length:',lent)
        value = lent 

        while value>1:
            t = list(itertools.permutations(s,value))
            for i in range(0,len(t)):
                    data = ''.join(t[i])
                    if data in english_words_set:
                        meaningful.append(data)
                    else:
                        nonmeaningful.append(data)
            value-=1













        # while value<=lent:
        #     print(value)
        #     if value == 12:
        #         t=list(itertools.permutations(s,value))
        #         for i in range(0,len(t)):
        #             data = ''.join(t[i])
        #             if d.check(data)==True:
        #                 meaningful.append(data)
        #             else:
        #                 nonmeaningful.append(data)
        #     if value == 11:
        #         t=list(itertools.permutations(s,value))
        #         for i in range(0,len(t)):
        #             data = ''.join(t[i])
        #             if d.check(data)==True:
        #                 meaningful.append(data)
        #             else:
        #                 nonmeaningful.append(data)
        #     if value == 10:
        #         t=list(itertools.permutations(s,value))
        #         for i in range(0,len(t)):
        #             data = ''.join(t[i])
        #             if d.check(data)==True:
        #                 meaningful.append(data)
        #             else:
        #                 nonmeaningful.append(data)
        #     if value == 9:
        #         t=list(itertools.permutations(s,value))
        #         for i in range(0,len(t)):

        #             data = ''.join(t[i])
        #             if d.check(data)==True:
        #                 meaningful.append(data)
        #             else:
        #                 nonmeaningful.append(data)

        #     if value == 8:
        #         t=list(itertools.permutations(s,value))
        #         for i in range(0,len(t)):
        #             data = ''.join(t[i])
        #             if d.check(data)==True:
        #                 meaningful.append(data)
        #             else:
        #                 nonmeaningful.append(data)
        #     if value == 7:
        #         t=list(itertools.permutations(s,value))
        #         for i in range(0,len(t)):
        #             data = ''.join(t[i])
        #             if d.check(data)==True:
        #                 meaningful.append(data)
        #             else:
        #                 nonmeaningful.append(data)
        #     if value == 6:
        #         t=list(itertools.permutations(s,value))
        #         for i in range(0,len(t)):
        #             data = ''.join(t[i])
        #             if d.check(data)==True:
        #                 meaningful.append(data)
        #             else:
        #                 nonmeaningful.append(data)
        #     if value == 5:
        #         t=list(itertools.permutations(s,value))
        #         for i in range(0,len(t)):

        #             data = ''.join(t[i])
        #             if d.check(data)==True:
        #                 meaningful.append(data)
        #             else:
        #                 nonmeaningful.append(data)
        #     if value == 4:
        #         t=list(itertools.permutations(s,value))
        #         for i in range(0,len(t)):
        #             data = ''.join(t[i])
        #             if d.check(data)==True:
        #                 meaningful.append(data)
        #             else:
        #                 nonmeaningful.append(data)
        #     if value == 3:
        #         t=list(itertools.permutations(s,value))
        #         for i in range(0,len(t)):
        #             data = ''.join(t[i])
        #             if d.check(data)==True:
        #                 meaningful.append(data)
        #             else:
        #                 nonmeaningful.append(data)
        #     if value == 2:
        #         t=list(itertools.permutations(s,value))
        #         for i in range(0,len(t)):

        #             data = ''.join(t[i])
        #             if d.check(data)==True:
        #                 meaningful.append(data)
        #             else:
        #                 nonmeaningful.append(data)
            
        #     if value==1:
        #         break
        #     value -=1
        print(meaningful)
        print(nonmeaningful)   
        test_list = list(set(meaningful)) 
        test_list1 = list(set(nonmeaningful))
        print(test_list)
        print(test_list1)
        
        return render(request,'ScrabbleWords.html',{'test_list':test_list,'test_list1':test_list1})
    else:
        return render(request,'WordScrabble.html',{})


def ScrabbleWords(request):
    return render(request,'ScrabbleWords.html',{})






# BS

def generate_random_view(request):

    question_list = ['metsi','ayzcr','mbouj','defirg','raihsc','ltaebs','aenspl']
    s = random.choice(question_list)
    request.session['word_chosen'] = s

    return render(request,'startgame.html',{})



def scramble_game_view(request):
    
    # d = enchant.Dict("en_US")
    # question_list = ['metsi','ayzcr','mbouj','defirg','raihsc','ltaebs','aenspl']
    # meaningful_list = []
    # l2 = []


    s = request.session['word_chosen']
    # print("*"*30)
    # print(s)
    # print("%"*30)


    # lent = len(s)
    # print('length:',lent)
    # value = lent 

    # while value>1:
    #     t = list(itertools.permutations(s,value))
    #     for i in range(0,len(t)):
    #             data = ''.join(t[i])
    #             if d.check(data)==True:
    #                 meaningful_list.append(data)
                
    #     value-=1
    # meaningful_list = list(set(meaningful_list))
    # print(meaningful_list)

    # dict_context = {}
    # high_score = 0
    # score = 0
    # for j in range(3):
    #     high_score = high_score + len(meaningful_list[j])
    # print('Possible Highscore is {}'.format(high_score))

    # if request.method == "POST":

    #     userinput1 = request.POST['U_input1']
    #     userinput2 = request.POST['U_input2']
    #     userinput3 = request.POST['U_input3']

    #     print(s)


    
    #     uilist = [userinput1,userinput2,userinput3]
    #     # userinput = input('Create a meaningful word using \'WORD\'. Chance Left {}: '.format(i))
    #     print(uilist)
    #     counter_repeated_correct = 1
    #     counter_repeated_incorrect = 1
    #     print(meaningful_list)
    #     for data in uilist:
            
    #         if (data.lower() in meaningful_list and data.lower() not in l2) :
    #             l2.append(data.lower())
    #             score = score + len(data)
    #             dict_context[data] = 'Correct Answer'

    #         elif (data.lower() in meaningful_list and data.lower() in l2) :
    #             dict_context[data + str(counter_repeated_correct)] = 'Correct Answer : Repeated'
    #             counter_repeated_correct = counter_repeated_correct + 1
    #             score = score - 1

                

    #         else:
    #             if (data.lower() not in meaningful_list and data.lower() not in l2) :

    #                 score = score - 1
    #                 dict_context[data] = 'Incorrect Answer'
    #             elif (data.lower() not in meaningful_list and data.lower() in l2):
    #                 dict_context[data] = 'Incorrect Answer : Repeated'
    #                 dict_context[data + str(counter_repeated_incorrect)] = 'Incorrect Answer : Repeated'
    #                 counter_repeated_incorrect = counter_repeated_incorrect + 1
    #                 score = score - 1

    #     print(dict_context)

    #     del request.session['word_chosen']



    #     context = {
    #         'resultdata':dict_context,
    #         'score':score,
    #         'high_score':high_score
    #     }
    #     return render(request,'game_result.html',context)

    # else:
    s_upper = s.upper()
    context_start = {
        's' : s_upper,
        
    }
    return render(request, 'game.html',context_start)
    # return render(request, 'startgame.html',{})








def scramble_game_result_view(request):
    if request.method == "POST":
        #d = enchant.Dict("en_US")
        question_list = ['metsi','ayzcr','mbouj','defirg','raihsc','ltaebs','aenspl']
        meaningful_list_b = []
        l2 = []
        s = request.session['word_chosen']
        print("*"*30)
        print(s)
        print("%"*30)


        lent = len(s)
        print('length:',lent)
        value = lent 

        while value>1:
            t = list(itertools.permutations(s,value))
            for i in range(0,len(t)):
                    data = ''.join(t[i])
                    if data in english_words_set:
                        meaningful_list_b.append(data)
                    
            value-=1
        meaningful_list_b = list(set(meaningful_list_b))
        print(meaningful_list_b)

        dict_context = {}
        high_score = 0
        score = 0
        for j in range(3):
            high_score = high_score + len(meaningful_list_b[j])
        print('Possible Highscore is {}'.format(high_score))

        userinput1 = request.POST['U_input1']
        userinput2 = request.POST['U_input2']
        userinput3 = request.POST['U_input3']

        print(s)


    
        uilist = [userinput1,userinput2,userinput3]
        # userinput = input('Create a meaningful word using \'WORD\'. Chance Left {}: '.format(i))
        print(uilist)
        counter_repeated_correct = 1
        counter_repeated_incorrect = 1
        print(meaningful_list_b)

        for data in uilist:
            
            if (data.lower() in meaningful_list_b and data.lower() not in l2) :
                l2.append(data.lower())
                score = score + len(data)
                dict_context[data] = 'Correct Answer'

            elif (data.lower() in meaningful_list_b and data.lower() in l2) :
                dict_context[data + str(counter_repeated_correct)] = 'Correct Answer : Repeated'
                counter_repeated_correct = counter_repeated_correct + 1
                score = score - 1

                

            else:
                if (data.lower() not in meaningful_list_b and data.lower() not in l2) :

                    score = score - 1
                    dict_context[data] = 'Incorrect Answer'
                elif (data.lower() not in meaningful_list_b and data.lower() in l2):
                    dict_context[data] = 'Incorrect Answer : Repeated'
                    dict_context[data + str(counter_repeated_incorrect)] = 'Incorrect Answer : Repeated'
                    counter_repeated_incorrect = counter_repeated_incorrect + 1
                    score = score - 1

        print(dict_context)
        del request.session['word_chosen']



        context = {
            'resultdata':dict_context,
            'score':score,
            'high_score':high_score
        }
        return render(request,'game_result.html',context)



















def challengetab_view(request):


    return render(request,'challengetab.html',{})

def givechallenge_view(request):
    if request.method == "POST":

        wordtoplay = request.POST['WordToPlay'].lower()
        gc_meaningfull = []

        print("*"*30)
        print(wordtoplay)
        print("%"*30)


        lent = len(wordtoplay)
        print('length:',lent)
        value = lent 
        #d = enchant.Dict("en_US")
        while value>1:
            t = list(itertools.permutations(wordtoplay,value))
            for i in range(0,len(t)):
                data = ''.join(t[i])
                if data in english_words_set:
                    gc_meaningfull.append(data)
            value-=1
        
        gc_meaningfull = list(set(gc_meaningfull))
        print(gc_meaningfull)
        if wordtoplay in gc_meaningfull:
            gc_meaningfull.remove(wordtoplay)
        # return render(request,'home.html',{})
        # # value-=1

        if len(gc_meaningfull) >2 :
            maxScorePossible = 0 
            for j in range(3):
                maxScorePossible = maxScorePossible + len(gc_meaningfull[j])
            print('maxScorePossible is {}'.format(maxScorePossible))
            challengedBy = request.session['UserType']
            print('Challenge posted by :',challengedBy)

            if  GameDetails.objects.filter(WordToPlay = wordtoplay).exists():
                myObjects = GameDetails.objects.all().filter(WordToPlay = wordtoplay)
                # name = myObjects[0].Username
                messages.error(request,'Word Already Exist in Database. Please try new word.')
                return redirect("/")
            else:
                gd = GameDetails(ChallengedBy = challengedBy, WordToPlay= wordtoplay, )
                gd.save()
                messages.info(request,'Successfully Posted Your Challenge')
                return redirect("/")
            
            # messages.info(request, 'Successfully Posted Your Challenge')
            # return redirect("/")
        else:
            messages.info(request, 'Failed to post your challenge. Generated Words are very Few. Please try new word')
            return redirect("/")

    
    else:
        return render(request,'givechallenge.html',{})

def takechallenge_view(request):
    challengesq=GameDetails.objects.all()
    currentplayer = request.session['UserType']
    print(currentplayer)
    # test1 = model_to_dict(challengesq)
    # for obj in challengesq:
    #     print(obj['WordToPlay'])
    # print(test1)
    # for obj in challengesq:
    #     print(obj.WordToPlay)


    return render(request,'takechallenge.html',{'challengesq':challengesq,'cplayer':currentplayer})

def viewscore_view(request):
    challengesscore=GameDetails.objects.all()
    # test1 = model_to_dict(challengesq)
    # for obj in challengesq:
    #     print(obj['WordToPlay'])
    # print(test1)
    for obj in challengesscore:
        print(obj.WordToPlay)


    return render(request,'viewscore.html',{'challengesq':challengesscore})

def playchallenge_view(request,tid):
    print(tid)
    word_dict = {}
    word = GameDetails.objects.all().filter(id=tid)
    for obj in word:
        word_dict['wordchallenged'] = obj.WordToPlay.upper()
    print(word_dict)
    return render(request,'playchallenge.html',word_dict)

def challengecheck_view(request):

    if request.method == "POST":
        # d = enchant.Dict("en_US")
        meaningful_list_c = []
        l2c =[]

        userinput1 = request.POST['U_input1'].lower()
        userinput2 = request.POST['U_input2'].lower()
        userinput3 = request.POST['U_input3'].lower()
        s = request.POST['wordchallenged'].lower()
    
        uilist = [userinput1,userinput2,userinput3]

        lent = len(s)
        print('length:',lent)
        value = lent 

        while value>1:
            t = list(itertools.permutations(s,value))
            for i in range(0,len(t)):
                    data = ''.join(t[i])
                    if data in english_words_set:
                        meaningful_list_c.append(data)
                
            value-=1
        meaningful_list_c = list(set(meaningful_list_c))
        if s in meaningful_list_c:
            meaningful_list_c.remove(s)
        print(meaningful_list_c)

        dict_context = {}
        score = 0
        print(uilist)
        counter_repeated_correct = 1
        counter_repeated_incorrect = 1
        print(meaningful_list_c)
        for data in uilist:
            
            if (data.lower() in meaningful_list_c and data.lower() not in l2c) :
                l2c.append(data.lower())
                score = score + len(data)
                dict_context[data] = 'Correct Answer'

            elif (data.lower() in meaningful_list_c and data.lower() in l2c) :
                dict_context[data + str(counter_repeated_correct)] = 'Correct Answer : Repeated'
                counter_repeated_correct = counter_repeated_correct + 1
                score = score - 1
            else:
                if (data.lower() not in meaningful_list_c and data.lower() not in l2c) :

                    score = score - 1
                    dict_context[data] = 'Incorrect Answer'
                elif (data.lower() not in meaningful_list_c and data.lower() in l2c):
                    dict_context[data] = 'Incorrect Answer : Repeated'
                    dict_context[data + str(counter_repeated_incorrect)] = 'Incorrect Answer : Repeated'
                    counter_repeated_incorrect = counter_repeated_incorrect + 1
                    score = score - 1
        print('%^&'*40)
        print(dict_context)
        print(score)
        print('%^&'*40)

        dbdata = GameDetails.objects.all().filter(WordToPlay=s)
        word_dict_c = {}
        for obj in dbdata:
            word_dict_c['dbscore'] = obj.ScoreGained
            word_dict_c['id'] = obj.id
        print(word_dict_c)
        dbscore = word_dict_c['dbscore']
        dbid = word_dict_c['id']
        print(dbscore)
        print(GameDetails)
        flag_c = False
        print
        context = {}
        currentplayer_c = request.session['UserType']
        if score > dbscore:
            GameDetails.objects.filter(id=dbid).update(ScoreGained=score,PlayedBy= currentplayer_c)
            flag_c = True
        if flag_c:
            context = {
                'congrats' : 'Congratulations!! You got the high score among your friends',
                'resultdata':dict_context,
                'score':score,
                
            }
        else:


            context = {
                'sorry' : 'Sorry!! You score is low compared to your friends',
                'resultdata':dict_context,
                'score':score,
                
            }
        return render(request,'playchallenge_result.html',context)
        
    return render(request,'home.html',{})

