# 💳 Credit Card Rewards Optimizer API

A RESTful backend service built with **FastAPI** that recommends the most rewarding credit card for a transaction based on configurable reward rules and estimates potential cashback. The project demonstrates modern backend development practices, including API design, data validation, and relational database management.

---

## 🚀 Features

- 🔹 Recommend the best credit card for a transaction
- 🔹 Calculate estimated cashback based on reward rates
- 🔹 CRUD operations for managing credit card information
- 🔹 Store and manage transaction records
- 🔹 Request and response validation using Pydantic
- 🔹 Interactive API documentation with Swagger UI
- 🔹 Modular and scalable project structure

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **SQLAlchemy**
- **SQLite**
- **Pydantic**
- **Uvicorn**

---

## 📂 Project Structure

```
Credit_Card_Rewards_Optimizer_API/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   └── routes.py
│
├── requirements.txt
├── README.md
└── rewards.db
```

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|----------|---------------------------|--------------------------------|
| POST | `/cards` | Add a new credit card |
| GET | `/cards` | Retrieve all credit cards |
| GET | `/cards/{id}` | Retrieve a specific card |
| PUT | `/cards/{id}` | Update card information |
| DELETE | `/cards/{id}` | Delete a credit card |
| POST | `/recommend` | Recommend the best card and estimate rewards |
| GET | `/transactions` | Retrieve transaction history |

---

## 📥 Sample Recommendation Request

```json
{
  "merchant": "Amazon",
  "category": "Shopping",
  "amount": 3000
}
```

## 📤 Sample Response

```json
{
  "recommended_card": "HDFC Millennia",
  "reward_rate": 5,
  "estimated_cashback": 150
}
```

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/BHAVNA510/Credit_Card_Rewards_Optimizer_API.git
cd Credit_Card_Rewards_Optimizer_API
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**macOS/Linux**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the server

```bash
uvicorn app.main:app --reload
```

---

## 📖 Interactive API Documentation

After starting the server, open:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## 🏗️ Design Highlights

- Built using RESTful API principles
- Modular backend architecture for maintainability
- Schema validation with Pydantic
- Relational data modeling with SQLAlchemy
- SQLite-backed persistence for lightweight deployment
- Easily extensible to support authentication, user-specific cards, and advanced reward rules

---

## 🔮 Future Enhancements

- JWT-based user authentication
- OAuth login support
- PostgreSQL integration
- Personalized reward optimization
- Spending analytics dashboard
- Rule engine for rotating and merchant-specific offers
- Docker deployment
- Unit and integration testing

---

## 📚 Learning Outcomes

This project strengthened my understanding of:

- FastAPI application development
- REST API design
- CRUD operations
- SQLAlchemy ORM
- SQLite database management
- Pydantic validation
- Backend architecture and API documentation

---

## 👩‍💻 Author

**Bhavna**

If you found this project interesting or have suggestions for improvement, feel free to connect or contribute!
