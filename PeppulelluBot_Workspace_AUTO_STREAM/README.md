# YouTube Chat Bot

Questo progetto è un bot di chat per YouTube che interagisce con gli utenti durante le trasmissioni in diretta. Utilizza l'API di YouTube per leggere i messaggi della chat in tempo reale e inviare risposte automatiche.

## Struttura del Progetto

```
youtube-chat-bot
├── src
│   ├── bot.py          # Logica principale del bot di chat
│   └── __init__.py     # Pacchetto Python
├── .env                # Variabili d'ambiente
├── client_secret.json  # Credenziali per l'autenticazione API
├── requirements.txt    # Dipendenze del progetto
└── README.md           # Documentazione del progetto
```

## Requisiti

Assicurati di avere Python 3.6 o superiore installato. Puoi installare le dipendenze necessarie eseguendo:

```
pip install -r requirements.txt
```

## Configurazione

1. Crea un progetto su Google Cloud Console e abilita l'API di YouTube Data.
2. Scarica il file `client_secret.json` e posizionalo nella directory principale del progetto.
3. Crea un file `.env` nella directory principale e aggiungi la seguente riga, sostituendo `YOUR_CHANNEL_ID` con l'ID del tuo canale YouTube:

```
CHANNEL_ID=YOUR_CHANNEL_ID
```

## Avvio del Bot

Per avviare il bot, esegui il seguente comando:

```
python src/bot.py
```

Il bot si autenticherà con l'API di YouTube e inizierà a leggere i messaggi della chat in tempo reale. Risponderà automaticamente ai messaggi che contengono "ciao".