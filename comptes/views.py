from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import render, redirect

Utilisateur = get_user_model()
def inscription(request):
    if request.method == "POST":
        """Traitement du formulaire"""
        # Récupèrons les information du formulaire
        nom_utilisateur = request.POST.get("username")
        mot_de_passe = request.POST.get("password")
        utilisateur = Utilisateur.objects.create_user(username=nom_utilisateur, password=mot_de_passe)
        login(request, utilisateur)
        return redirect('connexion')
    return render(request, 'comptes/inscription.html')
def connexion(request):
    if request.method == "POST":
        """Traitement du formulaire"""
        # Connecter l'utilisateur
        nom_utilisateur = request.POST.get("username")
        mot_de_passe = request.POST.get("password")
        utilisateur = authenticate(username=nom_utilisateur, password=mot_de_passe)
        if utilisateur:
            login(request, utilisateur)
            return redirect('/')
    return render(request, 'comptes/connexion.html')
def deconnexion(request):
    logout(request)
    return redirect('/')