### AULAB HACKADEMY - Specializzazione Coding AI

# Applicazione didattica: 
# Chatbot Palestra con Function Calling

## Competenze Didattiche Acquisibili

Questo progetto permette di capire come un modello linguistico possa chiamare funzioni Python tramite il function calling di OpenAI, combinando programmazione tradizionale e AI.


## Descrizione Generale dell'Applicazione

L'applicazione è un chatbot per una palestra, sviluppato con le API di OpenAI (modello `gpt-4o-mini`) e il framework Chainlit. L'assistente risponde alle domande sui corsi, sulle date di partenza e prenota lezioni di prova con i personal trainer. I dati sono simulati in memoria.

## Descrizione Dettagliata del Funzionamento

### 1. Struttura dell'Applicazione
L'applicazione è organizzata in due file principali:
- `tools/__init__.py`: punto di ingresso; definisce gli schemi dei tool, il ciclo di chat e la gestione delle chiamate a funzione
- `tools/tools.py`: contiene le classi che implementano i tool

### 2. Tool Disponibili

- `get_course_info` (`CourseInfoTool`): descrizione, durata e prezzo di un corso (Yoga, CrossFit, Pilates, Spinning, Boxe Fitness)
- `get_upcoming_classes` (`ScheduleTool`): corsi in partenza, filtrabili per nome e data di inizio
- `book_trial` (`BookingTool`): prenota una lezione di prova con un personal trainer in una data e ora precise

### 3. Flusso di una richiesta
1. Il messaggio dell'utente viene inviato al modello insieme agli schemi dei tool
2. Se il modello richiede una funzione, l'applicazione la esegue e rimanda il risultato al modello
3. Quando il modello risponde con del testo, la risposta viene mostrata all'utente
