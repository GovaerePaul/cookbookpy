from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from cookbook.forms import ConnexionForm, RecetteForm, EtapesForm, InscriptionForm, NoteForm
from cookbook.models import Recette, Note, Etapes_Recette, Ingredients, Liste_Ingredients


# Create your views here.
def index(request):
    return render(request, 'cookbook/index.html')


def afficher(request):
    recettes = Recette.objects.all();
    typeObjet = None
    paginator = Paginator(recettes, 10)
    page = request.GET.get('page')
    try:
        recettes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        recettes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        recettes = paginator.page(paginator.num_pages)
    contexte = {
        'typeObjet': typeObjet,
        'recettes': recettes,
    }
    return render(request, 'cookbook/afficher.html', contexte)

def ajouter(request):
    MainForm = RecetteForm()
    EtapeFormu = EtapesForm()
    if request.method == 'POST':
        MainForm = RecetteForm(request.POST)
        if MainForm.is_valid():
            recettes = MainForm.save()
            recettes.user = request.user
            recettes.save()
            EtapeFormu = EtapesForm(request.POST, instance=recettes)
            if EtapeFormu.is_valid():
                EtapeFormu.save()
            return render(request, "cookbook/nouvelle_recette.html", {
                'MainForm': MainForm,
                'EtapeForm': EtapeFormu,
                'create_success': 'success'
            })

    return render(request, "cookbook/nouvelle_recette.html", {
        'MainForm': MainForm,
        'EtapeForm': EtapeFormu,
    })

def inscription(request):
    if request.method == 'POST':
        user_form = InscriptionForm(request.POST)
        if user_form.is_valid():
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            contexte = {
                'form': AuthenticationForm,
                'success_message': 'success'
            }
            return render(request, 'cookbook/connexion.html', contexte)
    else:
        user_form = InscriptionForm()
    contexte = {
        'formulaire_user': user_form,
    }
    return render(request, 'cookbook/inscription.html', contexte)

def userLogout(request):
    logout(request)
    # Redirect to a success page.

def consulter(request, id):

    if (request.method == 'POST'):
        note_form = NoteForm(request.POST)


        if note_form.is_valid():
            note = note_form.save()
            note.id_recette = Recette.objects.get(id=id)
            note.user = request.user
            note.save()


    recette = Recette.objects.get(id=id)
    etapes = Etapes_Recette.objects.filter(id_recette=id)
    ingredients = Ingredients.objects.filter(id_recette=id)
    note = Note.objects.filter(id_recette=id).aggregate(Avg('valeur'))
    noted = 0
    if(request.user.is_authenticated()):
        noted = Note.objects.filter(id_recette=id, user=request.user).count()
    form_note = ''
    if noted == 0:
        form_note = NoteForm();

    contexte = {
        'recette'    : recette,
        'etapes'     : etapes,
        'ingredients': ingredients,
        'notes'     : note,
        'form_note': form_note,

    }
    return render(request, 'cookbook/consulter.html', contexte)