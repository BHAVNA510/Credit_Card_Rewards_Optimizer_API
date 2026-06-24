# Credit Card Rewards Optimizer API

A RESTful backend service that recommends the optimal credit card and estimates cashback for user transactions based on configurable reward rules.

## Problem Statement

Users often own multiple credit cards, each with different cashback rates and reward policies. Choosing the best card for every purchase can be confusing. This API analyzes transaction details and recommends the most rewarding credit card while estimating cashback.

## Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python |
| Backend Framework | FastAPI |
| ORM | SQLAlchemy |
| Database | SQLite |
| Validation | Pydantic |
| Server | Uvicorn |

## Live API

**Production:** https://credit-card-rewards-optimizer-api.vercel.app

Interactive docs: https://credit-card-rewards-optimizer-api.vercel.app/docs

## Local Setup

```bash
cd Credit_Card_Rewards_Optimizer_API
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Endpoints

### Credit Card Management

**Create Card** — `POST /cards`

```bash
curl -X POST http://127.0.0.1:8000/cards \
  -H "Content-Type: application/json" \
  -d '{
    "card_name": "HDFC Millennia",
    "issuer": "HDFC",
    "category": "Shopping",
    "reward_rate": 5,
    "max_cashback": 1000
  }'
```

**View All Cards** — `GET /cards`

```bash
curl http://127.0.0.1:8000/cards
```

**Update Card** — `PUT /cards/{id}`

```bash
curl -X PUT http://127.0.0.1:8000/cards/1 \
  -H "Content-Type: application/json" \
  -d '{
    "card_name": "HDFC Millennia",
    "issuer": "HDFC",
    "category": "Shopping",
    "reward_rate": 5.5,
    "max_cashback": 1000
  }'
```

**Delete Card** — `DELETE /cards/{id}`

```bash
curl -X DELETE http://127.0.0.1:8000/cards/1
```

### Reward Recommendation

**Recommend Best Card** — `POST /recommend`

```bash
curl -X POST http://127.0.0.1:8000/recommend \
  -H "Content-Type: application/json" \
  -d '{
    "merchant": "Amazon",
    "category": "Shopping",
    "amount": 3000
  }'
```

Example response:

```json
{
  "recommended_card": "HDFC Millennia",
  "reward_rate": 5.0,
  "estimated_cashback": 150.0
}
```

### Transaction History

**View Transactions** — `GET /transactions`

```bash
curl http://127.0.0.1:8000/transactions
```

## Recommendation Algorithm

1. Filter cards by transaction category (case-insensitive)
2. Compare reward rates and pick the highest
3. Calculate cashback: `min(amount × reward_rate / 100, max_cashback)`
4. Save the transaction
5. Return the recommendation

## Project Structure

```
Credit_Card_Rewards_Optimizer_API/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── requirements.txt
├── README.md
├── .gitignore
└── rewards.db          # created locally on first run
```

## Deploy to Vercel

```bash
npm i -g vercel   # if not installed
vercel login
vercel deploy --prod
```

Vercel auto-detects `main.py` with the `app` FastAPI instance. On Vercel, SQLite uses `/tmp/rewards.db` and sample cards are seeded on startup.

> **Note:** Vercel serverless functions use ephemeral storage. Data may reset on cold starts. For production persistence, migrate to PostgreSQL or another managed database.
