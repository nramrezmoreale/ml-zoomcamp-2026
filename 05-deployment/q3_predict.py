"""Question 3: load pipeline.bin with pickle and score one lead."""

import pickle

from model import normalize_record

lead = {
    "lead_source": "paid_ads",
    "industry": "technology",
    "employment_status": "employed",
    "location": "north_america",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0,
    "interaction_count": 4,
    "lead_score": 0.41,
}

with open("pipeline.bin", "rb") as f:
    pipeline = pickle.load(f)

# This lead has no missing values, so normalize_record leaves it unchanged;
# it's kept here to match exactly what the API does.
probability = pipeline.predict_proba([normalize_record(lead)])[0, 1]

print("pipeline steps:", [name for name, _ in pipeline.steps])
print(f"conversion probability: {probability:.6f}")
print(f"rounded (3 dp):         {probability:.3f}")
