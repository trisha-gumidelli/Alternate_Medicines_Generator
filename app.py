from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)

df = pd.read_csv('my_data.csv')
df['Merged_Compo'] = df['Merged_Compo'].fillna('')
df['Compo_1'] = df['Compo_1'].fillna('')
df['Compo_2'] = df['Compo_2'].fillna('')
df['Cost'] = df['price(₹)'].fillna('N/A')  

vectorizer_merged = CountVectorizer()
x_merged = vectorizer_merged.fit_transform(df['Merged_Compo'])

model_merged = NearestNeighbors(n_neighbors=5, metric='cosine')
model_merged.fit(x_merged)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        user_med = request.json.get('medicine').strip().lower()
        matches = df[df['name'].str.strip().str.lower() == user_med]
        if matches.empty:
            return jsonify({"error": "Medicine not found."})

        first_match = matches.iloc[0]
        user_index = matches.index[0]

        compo1 = first_match['Compo_1'] if pd.notnull(first_match['Compo_1']) else "N/A"
        quantity1 = first_match['Quantity_1'] if pd.notnull(first_match['Quantity_1']) else "N/A"
        compo2 = first_match['Compo_2'] if pd.notnull(first_match['Compo_2']) else "N/A"
        quantity2 = first_match['Quantity_2'] if pd.notnull(first_match['Quantity_2']) else "N/A"
        cost = first_match['Cost'] if pd.notnull(first_match['Cost']) else "N/A"

        if first_match['Merged_Compo'].strip():
            distances, indices = model_merged.kneighbors(x_merged[user_index])
        else:
            compo1_vectorized = vectorizer_merged.transform([first_match['Compo_1']])
            distances, indices = model_merged.kneighbors(compo1_vectorized)
        similar_meds_info = []
        for idx in indices[0]:
            med_name = df.iloc[idx]['name'].capitalize()
            if med_name.strip().lower() != user_med:
                med_compo1 = df.iloc[idx]['Compo_1'] if pd.notnull(df.iloc[idx]['Compo_1']) else "N/A"
                med_quantity1 = df.iloc[idx]['Quantity_1'] if pd.notnull(df.iloc[idx]['Quantity_1']) else "N/A"
                med_compo2 = df.iloc[idx]['Compo_2'] if pd.notnull(df.iloc[idx]['Compo_2']) else "N/A"
                med_quantity2 = df.iloc[idx]['Quantity_2'] if pd.notnull(df.iloc[idx]['Quantity_2']) else "N/A"
                med_cost = df.iloc[idx]['Cost'] if pd.notnull(df.iloc[idx]['Cost']) else "N/A"
                similar_meds_info.append({
                    "name": med_name,
                    "composition": {
                        "compo1": med_compo1,
                        "quantity1": med_quantity1,
                        "compo2": med_compo2,
                        "quantity2": med_quantity2
                    },
                    "cost": med_cost
                })
        response = {
            "medicine": first_match['name'].capitalize(),
            "composition": {
                "compo1": compo1,
                "quantity1": quantity1,
                "compo2": compo2,
                "quantity2": quantity2
            },
            "cost": cost,
            "alternatives": similar_meds_info
        }
        return jsonify(response)
    except Exception as e:
        print("Error during generation:", e)
        return jsonify({"error": "An error occurred during processing."})

if __name__ == '__main__':
    app.run(debug=True)
