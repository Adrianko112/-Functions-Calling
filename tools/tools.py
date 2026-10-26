from typing import Optional


class CourseInfoTool:
    def __init__(self):
        # Simulazione di un database dei corsi della palestra
        self.courses = {
            "yoga": {
                "name": "Yoga",
                "description": "Posture, respirazione e rilassamento per migliorare flessibilita' e concentrazione",
                "duration": "8 settimane",
                "price": 89.90
            },
            "crossfit": {
                "name": "CrossFit",
                "description": "Allenamento funzionale ad alta intensita'",
                "duration": "12 settimane",
                "price": 149.90
            },
            "pilates": {
                "name": "Pilates",
                "description": "Rafforzamento del core e miglioramento della postura",
                "duration": "8 settimane",
                "price": 99.90
            },
            "spinning": {
                "name": "Spinning",
                "description": "Allenamento cardio in sella a ritmo di musica",
                "duration": "6 settimane",
                "price": 69.90
            },
            "boxe_fitness": {
                "name": "Boxe Fitness",
                "description": "Tecniche di boxe non da contatto per tonificare e scaricare lo stress",
                "duration": "10 settimane",
                "price": 119.90
            }
        }

    def get_info(self, course_name: str) -> str:
        course = self.courses.get(course_name.lower().replace(" ", "_"))
        if not course:
            return f"Corso non trovato con tale nome. Ecco i corsi disponibili: {self.courses}"
        return (f"Corso: {course['name']}\n"
                f"Descrizione: {course['description']}\n"
                f"Durata: {course['duration']}\n"
                f"Prezzo: €{course['price']}")


class ScheduleTool:
    def __init__(self):
        # Simulazione di un database dei corsi in partenza
        self.classes = [
            {"course_name": "Yoga", "start_date": "2025-06-10", "end_date": "2025-08-05", "spots_available": 14},
            {"course_name": "CrossFit", "start_date": "2025-06-03", "end_date": "2025-08-26", "spots_available": 9},
            {"course_name": "Pilates", "start_date": "2025-06-17", "end_date": "2025-08-12", "spots_available": 11},
            {"course_name": "Spinning", "start_date": "2025-07-01", "end_date": "2025-08-12", "spots_available": 20},
            {"course_name": "Boxe Fitness", "start_date": "2025-09-02", "end_date": "2025-11-11", "spots_available": 12},
        ]

    def get_classes(self, course_name: Optional[str] = None,
                    start_date: Optional[str] = None) -> str:
        filtered_classes = self.classes
        if course_name:
            filtered_classes = [c for c in filtered_classes
                                if c["course_name"].lower() == course_name.lower()]
        if start_date:
            filtered_classes = [c for c in filtered_classes
                                if c["start_date"] >= start_date]

        if not filtered_classes:
            return f"Nessun corso trovato per i criteri specificati. Ecco i corsi in partenza: {self.classes}"

        result = "Prossimi corsi in partenza:\n"
        for c in filtered_classes:
            result += (f"- {c['course_name']}: {c['start_date']} - {c['end_date']}, "
                       f"Posti disponibili: {c['spots_available']}\n")
        return result


class BookingTool:
    def __init__(self):
        # Simulazione di un database delle disponibilita' dei personal trainer
        self.available_slots = [
            {"trainer_id": "P001", "trainer_name": "Marco", "date": "2025-06-02", "time": "09:00"},
            {"trainer_id": "P002", "trainer_name": "Giulia", "date": "2025-06-02", "time": "18:30"},
            {"trainer_id": "P003", "trainer_name": "Luca", "date": "2025-06-04", "time": "17:00"},
            {"trainer_id": "P004", "trainer_name": "Sara", "date": "2025-06-05", "time": "10:30"},
            {"trainer_id": "P005", "trainer_name": "Davide", "date": "2025-06-05", "time": "10:30"},
            {"trainer_id": "P006", "trainer_name": "Elena", "date": "2025-06-09", "time": "19:00"},
            {"trainer_id": "P007", "trainer_name": "Andrea", "date": "2025-06-12", "time": "08:00"},
            {"trainer_id": "P008", "trainer_name": "Chiara", "date": "2025-06-16", "time": "16:30"},
            {"trainer_id": "P009", "trainer_name": "Matteo", "date": "2025-06-20", "time": "11:00"},
            {"trainer_id": "P010", "trainer_name": "Francesca", "date": "2025-06-24", "time": "18:00"},
        ]

    def book_trial(self, date: str, time: str,
                   trainer_id: Optional[str] = None) -> str:
        available = [slot for slot in self.available_slots
                     if slot["date"] == date and slot["time"] == time]

        if trainer_id:
            available = [slot for slot in available
                         if slot["trainer_id"] == trainer_id]

        if not available:
            return (f"Mi dispiace, nessuna disponibilita' per la data e l'ora specificate. "
                    f"Ecco tutte le disponibilita' al momento: {self.available_slots}")

        # Simulazione della prenotazione
        slot = available[0]
        self.available_slots.remove(slot)
        return (f"Lezione di prova confermata con {slot['trainer_name']} "
                f"per il {slot['date']} alle {slot['time']}")
