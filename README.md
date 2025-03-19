### 📌 **AI-TOETATUD ÜLESANNETE HALDUSSÜSTEEM – `ai_todo`**
> **Django + AI põhine süsteem, mis prioriseerib ülesandeid automaatselt**  

---

## **📌 1. Projekti Ülevaade**
**`ai_todo`** on **tehisintellektiga varustatud ülesannete haldamise süsteem**, mis aitab kasutajatel organiseerida oma tööd, andes igale ülesandele **dünaamilise prioriteedi**. AI arvutab **tähtsuse taseme** lähtudes **tähtajast, keerukusest ja sagedusest**.

**Peamised võimalused:**
- **Automaatne prioriseerimine AI-ga** (Kõrge, Keskmine, Madal)
- **Interaktiivne ülesannete nimekiri** (otsing, sorteerimine)
- **Kasutaja autentimine** (registreerimine, sisselogimine, väljalogimine)
- **Bootstrap 4 kujundus** (mobiilisõbralik ja stiilne UI)
- **Tume/hele režiimi vahetamine**
- **Django-admin** kaudu andmete haldamine

---

## **📌 2. Kasutatud Tehnoloogiad**
| Tehnoloogia | Kasutus |
|-------------|--------|
| **Python (venv)** | Põhikeel |
| **Django** | Raamistik |
| **Django-admin** | Adminpaneeli jaoks |
| **Bootstrap 4** | Kujundus ja responsiivsus |
| **JavaScript** | Reaalajas prioriteedi arvutamine |
| **SQLite/PostgreSQL** | Andmebaas |
| **jQuery + AJAX** | Tume režiimi vahetamine |
| **CSRF + Sessioonid** | Turvalisus |

---

## **📌 3. Põhifunktsioonid**
### 🔹 **Kasutaja funktsioonid**
✔ Registreerimine ja sisselogimine  
✔ Ülesannete loomine ja muutmine  
✔ AI-põhine prioriteedi määramine  
✔ Sortimine ja otsing ülesannete hulgas  
✔ Tume/hele režiimi vahetamine  

### 🔹 **Admin funktsioonid**
✔ Kõikide ülesannete haldamine  
✔ Kasutajate juhtimine Django adminis  
✔ AI soovituste analüüsimine  

### 🔹 **AI prioriseerimine**
AI arvutab ülesannete prioriteedi, kasutades:  
- **Tähtaeg** (mida lähemal, seda kõrgem prioriteet)  
- **Keerukus** (raske ülesanne saab kõrgema prioriteedi)  
- **Sagedus** (harvem tehtavad ülesanded on tähtsamad)  

Koodinäide AI prioriteedi määramiseks:
```python
def calculate_priority(task):
    days_left = (task.due_date - datetime.date.today()).days
    urgency_score = max(1, 10 - days_left)
    complexity_score = task.complexity * 2
    frequency_score = max(1, 7 - task.frequency)

    total_score = urgency_score + complexity_score + frequency_score

    if total_score > 15:
        return 'High'
    elif total_score > 8:
        return 'Medium'
    else:
        return 'Low'
```

---

## **📌 4. Installatsioon**
### **1️⃣ Samm: Klooni projekt**
```bash
git clone https://github.com/username/ai_todo.git
cd ai_todo
```

### **2️⃣ Samm: Loo virtuaalkeskkond ja paigalda sõltuvused**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **3️⃣ Samm: Konfigureeri andmebaas**
```bash
python manage.py migrate
python manage.py createsuperuser  # Admini kasutaja loomiseks
```

### **4️⃣ Samm: Käivita server**
```bash
python manage.py runserver
```
Ava veebilehitsejas:
```
http://127.0.0.1:8000/
```

---

## **📌 5. Kasutajaliidese pildid (screenshots)**
✅ **Minu ülesannete leht**  
✅ **AI põhine prioriteedi määramine**  
✅ **Tume ja hele režiim**  
✅ **Adminpaneel ülesannete ja kasutajate haldamiseks**  

(*Lisa siia pildid kasutajaliidesest!*)  

---

## **📌 6. API ja Täiendavad Funktsioonid**
Lisaks tavakasutajatele on võimalik **API kaudu ülesandeid luua ja küsida**.

**API kasutamine (JSON vastused)**:
```bash
curl -X GET http://127.0.0.1:8000/api/tasks/
```
(*Lisada vajadusel Django REST framework integratsioon!*)

---

## **📌 7. Kokkuvõte**
✔ **AI-toega ülesannete prioritiseerimine**  
✔ **Kasutajasõbralik disain Bootstrapiga**  
✔ **Tume ja hele režiim**  
✔ **Django-admin haldus**  

✨ **Tulevikus võiks lisada rohkem AI optimeerimist ja meeldetuletuste süsteemi!** 🚀  

---

**📌 Arendaja:** *Arno Punnar - Arvutionu*  
**📌 Repo:** *GitHub või Bitbucket link*  
**📌 Kontakt:** *arnopps@gmail.com*  
