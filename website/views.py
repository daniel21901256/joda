from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from matplotlib import pyplot as plt

from website.forms import *
from .models import *


def index_page_view(request):
    return render(request, 'website/index.html')


def carnes_page_view(request):
    return render(request, 'website/carnes.html')


def doces_page_view(request):
    return render(request, 'website/doces.html')

def funcao_post():
    post_get = Post.objects.all()
    avaliacoes = [0, 0, 0, 0, 0]

    for i in post_get:
        if i.avaliacao == "1":
            avaliacoes[0] += 1
        elif i.avaliacao == "2":
            avaliacoes[1] += 1
        elif i.avaliacao == "3":
            avaliacoes[2] += 1
        elif i.avaliacao == "4":
            avaliacoes[3] += 1
        elif i.avaliacao == "5":
            avaliacoes[4] += 1

    plt.title("Avaliações do Website")
    plt.bar([1, 2, 3, 4, 5], avaliacoes)
    plt.xlabel('★ Rating ★')
    plt.ylabel('N º Avaliações')
    plt.savefig('website/static/website/images/quizz2.png')



def opiniao_page_view(request):

    funcao_post()
    context = {
        'imagem': plt
    }
    plt.close()


    if request.method == 'POST' is not None:
        if request.POST.get('avaliacao', "0") is not None:
            post = Post()
            post.avaliacao = request.POST.get('avaliacao', "0")
            post.save()
            funcao_post()
            context = {
                'imagem': plt
            }
            plt.close()

            return render(request, 'website/opiniao.html', context=context)
    else:
        return render(request, 'website/opiniao.html', context=context)


def peixe_page_view(request):
    return render(request, 'website/peixe.html')


def veggie_page_view(request):
    return render(request, 'website/veggie.html')


def veggieR_page_view(request):
    return render(request, 'website/veggieReceita.html')


def carnesR_page_view(request):
    return render(request, 'website/carneReceita.html')


def peixeR_page_view(request):
    return render(request, 'website/peixeReceita.html')


def docesR_page_view(request):
    return render(request, 'website/doceReceita.html')


def videos_page_view(request):
    return render(request, 'website/videos.html')


def quemSomos_page_view(request):
    return render(request, 'website/quemSomos.html')


def receitaNova_page_view(request):
    return render(request, 'website/receitaNova.html')


def quizz_page_view(request):
    form = quizzForm(request.POST or None)
    if form.is_valid():
        form_fields = form.save()
        return HttpResponseRedirect('quizz_resultados/' + str(form_fields.id))

    context = {'form': form}

    return render(request, 'website/quizz.html', context=context)


def quizz_resultados(request, id):
    quizz_get = quizz.objects.get(pk=id)
    cotacao = 0
    certos = []

    if (quizz_get.pergunta_1 == '12'):
        cotacao += 10
        certos.append(1)
    else:
        certos.append(0)

    if (quizz_get.pergunta_2 == '12'):
        cotacao += 10
        certos.append(1)
    else:
        certos.append(0)

    if (quizz_get.pergunta_3 == '12'):
        cotacao += 10
        certos.append(1)
    else:
        certos.append(0)

    if (quizz_get.pergunta_4 == '18'):
        cotacao += 10
        certos.append(1)
    else:
        certos.append(0)

    if (quizz_get.pergunta_5.lower() == 'setubal'):
        cotacao += 10
        certos.append(1)
    else:
        certos.append(0)

    if (quizz_get.pergunta_6.lower() == '100 maneiras'):
        cotacao += 10
        certos.append(1)
    else:
        certos.append(0)

    if (quizz_get.pergunta_7.lower() == 'alentejo'):
        cotacao += 10
        certos.append(1)
    else:
        certos.append(0)

    if (quizz_get.pergunta_8 == '1'):
        cotacao += 10
        certos.append(1)
    else:
        certos.append(0)

    if (quizz_get.pergunta_9 == '1'):
        cotacao += 10
        certos.append(1)
    else:
        certos.append(0)

    if (quizz_get.pergunta_10 == '2'):
        cotacao += 10
        certos.append(1)
    else:
        certos.append(0)

    labels = ['Certos', 'Errados']
    sizes = [cotacao, 100 - cotacao]
    fig1, ax1 = plt.subplots()
    colors = ['#F8D167', '#987456']
    explode = (0.01, 0.01)
    ax1.pie(sizes, autopct='%1.1f%%', startangle=90, colors=colors, pctdistance=0.80, explode=explode)
    centre_circle = plt.Circle((0, 0), 0.60, fc='white')
    sumstr = str(int(cotacao / 10)) + "/10"
    ax1.text(0., 0., sumstr, horizontalalignment='center', verticalalignment='center', fontsize=30)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    ax1.axis('equal')
    plt.legend(title="Resultados:", labels=labels)
    plt.tight_layout()
    plt.savefig('website/static/website/images/quizz.png')

    context = {
        'quizz': quizz_get,
        'resultado': cotacao,
        'imagem': plt
    }

    return render(request, 'website/quizz_resultado.html', context)


def contactos_page_view(request):
    form = contactoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:contactos'))

    context = {'form': form, 'contactos': contacto.objects.all()}

    return render(request, 'website/contactos.html', context)


def edita_contactos_view(request, contacto_id):
    contactoEditar = contacto.objects.get(pk=contacto_id)
    form = contactoForm(request.POST or None, instance=contactoEditar)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:contactos'))

    context = {'form': form, 'contacto_id': contacto_id}
    return render(request, 'website/edita.html', context)


def apaga_contactos_view(request, contacto_id):
    contacto.objects.get(id=contacto_id).delete()
    return HttpResponseRedirect(reverse('website:contactos'))


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('website:index'))
        else:
            return render(request, 'website/login.html', {
                'message': 'Credenciais inválidas.'
            })

    return render(request, 'website/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'website/index.html', {
        'message': 'Insira os Seus Dados'})
