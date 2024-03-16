# Importation des bibliothèques nécessaires
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

# Paramètres de l'API YouTube
api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "./client_secret_608786903130-al1jeiku8hfs5rhuccvrbvuc7luv13hg.apps.googleusercontent.com.json"

# Scopes pour l'authentification OAuth2
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# Fonction pour obtenir les credentials et créer le service API
def get_authenticated_service():
    credentials = None
    # Token pickle file stocke les tokens d'accès et de rafraîchissement de l'utilisateur, et est
    # créé automatiquement lorsque le flux d'autorisation est complété pour la première fois
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)
    # Si les credentials ne sont pas valides ou n'existent pas, demandez à l'utilisateur de se connecter.
    if not credentials or not credentials.valid:
      if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
        credentials = flow.run_local_server()
    # Sauvegarde des credentials pour le prochain lancement
    with open("token.pickle", "wb") as token:
        pickle.dump(credentials, token)
    return build(api_service_name, api_version, credentials=credentials)

# Fonction pour poster un commentaire
def comment_on_video(youtube, video_id, text):
    request = youtube.commentThreads().insert(
        part="snippet",
        body={
            "snippet": {
                "videoId": video_id,
                "topLevelComment": {
                    "snippet": {
                        "textOriginal": text
                    }
                }
            }
        }
    )
    response = request.execute()
    print(response)

# Utilisation des fonctions
if __name__ == "__main__":
    # Obtenez le service API authentifié
    youtube = get_authenticated_service()
    # ID de la vidéo sur laquelle vous voulez commenter
    video_id = "nohSJpzrAUM"
    # Texte du commentaire
    # Postez le commentaire
        # Boucle pour poster le commentaire 100 fois
    # for i in range(20):
comment_text = "Commentaire Automatisé mn 3end Yassine Elmouss ... Kemmel ha 7na khdamin m3ak... ❤❤❤"
comment_on_video(youtube, video_id, comment_text)