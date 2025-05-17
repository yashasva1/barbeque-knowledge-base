from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()

# 🔸 Knowledge Base with all Delhi and Bangalore outlets
knowledge_base = {
    "delhi": {
        "connaught_place": {
            "timing": "Lunch: 12:00 PM to 5:00 PM, Dinner: 6:30 PM to 12:00 AM (Monday–Sunday).",
            "address": "Munshilal Building, 2nd Floor, N-19, Block N, Connaught Place, New Delhi, 110001.",
            "phone_numbers": ["7042698057", "8130244992", "8470015488"],
            "menu": "Veg Starters: Grill Veg, Mushroom, Paneer, Cajun Potato, Pineapple. Non-Veg Starters: Chicken Tangdi, Chicken Skewer, Mutton, Fish, Prawns. Mains: Dal Makhani, Veg/Non-Veg Biryani, Chicken Curry, Noodles. Desserts: Gulab Jamun, Ice Cream, Kulfis (6 flavors), Phirni, Pastries.",
            "jain_food": "Yes, Jain food is available with limited variety. Inform the outlet team upon arrival.",
            "halal": "Yes, all meat served at Barbeque Nation is Halal certified.",
            "alcohol": "Yes, alcohol is served à la carte. Outside drinks are not allowed.",
            "drinks_menu": "View the drinks menu via the Barbeque Nation app or request by email.",
            "kulfi_flavors": "Strawberry, Malai, Chocolate, Kesar Badam, Paan, Mango."
        },
        "vasant_kunj": {
            "timing": "Lunch: 12:00 PM to 5:00 PM, Dinner: 6:00 PM to 12:00 AM (Monday–Sunday).",
            "address": "Plot No. 11, Pocket 7, Sector C, Vasant Kunj, New Delhi, 110070.",
            "phone_numbers": ["9717455633", "9717466433", "7303094054"],
            "menu": "Same as standard Barbeque Nation veg/non-veg menu with buffet format.",
            "jain_food": "Yes, limited Jain food options are available. Inform the team on arrival.",
            "halal": "Yes, all meat is Halal certified.",
            "alcohol": "Alcohol is served à la carte. Outside drinks are not allowed.",
            "drinks_menu": "Drinks menu is available in-app or can be emailed upon request.",
            "kulfi_flavors": "Strawberry, Malai, Chocolate, Kesar Badam, Paan, Mango."
        },
        "janakpuri": {
            "timing": "Lunch: 12:00 PM to 5:00 PM, Dinner: 6:00 PM to 12:00 AM (Monday–Sunday).",
            "address": "Unity One, 2nd Floor, Narang Colony, Chander Nagar, Janakpuri, New Delhi, 110058.",
            "phone_numbers": ["9810445315", "9311177719", "7827935431"],
            "menu": "Standard buffet with vegetarian and non-vegetarian starters, mains, desserts.",
            "jain_food": "Yes, Jain options are available. Notify the team upon arrival.",
            "halal": "Yes, Halal meat is served.",
            "alcohol": "Alcohol is served à la carte. Outside alcohol is not allowed.",
            "drinks_menu": "Can be accessed via the Barbeque Nation app or shared by email.",
            "kulfi_flavors": "Strawberry, Malai, Chocolate, Kesar Badam, Paan, Mango."
        }
    },
    "bangalore": {
        "koramangala": {
            "timing": "Lunch: 12:00 PM to 5:00 PM, Dinner: 6:30 PM to 11:55 PM (Monday–Sunday).",
            "address": "1st Cross Rd, 1st Block Koramangala, Bengaluru, Karnataka 560034.",
            "phone_numbers": ["9071399811", "9071399812", "9071772467"],
            "menu": "Veg & Non-Veg Starters, Biryani, Curries, Desserts, Ice Cream, Kulfis.",
            "jain_food": "Yes, available in limited variety. Please inform staff on arrival.",
            "halal": "Yes, Halal meat is served.",
            "alcohol": "Served à la carte. Outside alcohol not allowed.",
            "drinks_menu": "Available via app or request through email.",
            "kulfi_flavors": "Strawberry, Malai, Chocolate, Kesar Badam, Paan, Mango."
        },
        "jp_nagar": {
            "timing": "Lunch: 12:00 PM to 5:00 PM, Dinner: 6:30 PM to 11:55 PM (Monday–Sunday).",
            "address": "67, 3rd Floor, 6th B Main, Phase III, JP Nagar, Bengaluru, Karnataka 560078.",
            "phone_numbers": ["7090757107", "7353535557"],
            "menu": "Same standard veg/non-veg buffet menu with wide selection of dishes and desserts.",
            "jain_food": "Available in limited options. Inform team when arriving.",
            "halal": "Yes, Halal meat is served.",
            "alcohol": "Alcohol is served. No outside drinks permitted.",
            "drinks_menu": "Request in app or via email.",
            "kulfi_flavors": "Strawberry, Malai, Chocolate, Kesar Badam, Paan, Mango."
        },
        "electronic_city": {
            "timing": "Lunch: 12:00 PM to 5:00 PM, Dinner: 6:30 PM to 11:55 PM (Monday–Sunday).",
            "address": "99, 14th Cross Rd, Neeladri Nagar, Electronics City Phase 1, Bengaluru, Karnataka 560100.",
            "phone_numbers": ["7090757126", "7090757059"],
            "menu": "Buffet with rotating menu of starters, curries, rice, desserts and ice cream.",
            "jain_food": "Yes, on request. Options may be limited.",
            "halal": "Yes, Halal-certified meat is used.",
            "alcohol": "Alcohol is served from à la carte menu.",
            "drinks_menu": "Check via mobile app or ask to email it to you.",
            "kulfi_flavors": "Strawberry, Malai, Chocolate, Kesar Badam, Paan, Mango."
        },
        "indiranagar": {
            "timing": "Lunch: 12:00 PM to 5:00 PM, Dinner: 6:30 PM to 11:55 PM (Monday–Sunday).",
            "address": "No.4005, HAL 2nd Stage, 100 Feet Road, Indiranagar, Bangalore-560038.",
            "phone_numbers": ["7892263996", "7090757068"],
            "menu": "Wide selection of buffet items including grill starters, biryani, and desserts.",
            "jain_food": "Jain food is provided in limited quantity upon request.",
            "halal": "Halal meat is served.",
            "alcohol": "Alcohol is served. Outside drinks are not allowed.",
            "drinks_menu": "Check app or email request.",
            "kulfi_flavors": "Strawberry, Malai, Chocolate, Kesar Badam, Paan, Mango."
        }
    }
}

# 🔹 Search Endpoint
@app.get("/api/faq")
def get_info(location: str, outlet: str, question: str):
    location = location.lower()
    outlet = outlet.lower()
    question = question.lower()

    if location not in knowledge_base or outlet not in knowledge_base[location]:
        return JSONResponse(status_code=404, content={"answer": "Sorry, outlet not found."})

    outlet_info = knowledge_base[location][outlet]

    # Keyword-based search logic
    if "timing" in question or "open" in question or "close" in question:
        return {"answer": outlet_info.get("timing")}
    elif "address" in question or "location" in question:
        return {"answer": outlet_info.get("address")}
    elif "menu" in question:
        return {"answer": outlet_info.get("menu")}
    elif "jain" in question:
        return {"answer": outlet_info.get("jain_food")}
    elif "halal" in question:
        return {"answer": outlet_info.get("halal")}
    elif "alcohol" in question or "beer" in question or "drink" in question:
        return {"answer": outlet_info.get("alcohol")}
    elif "kulfi" in question or "ice cream" in question:
        return {"answer": outlet_info.get("kulfi_flavors")}
    elif "drinks menu" in question or "cocktail" in question:
        return {"answer": outlet_info.get("drinks_menu")}
    elif "phone" in question or "contact" in question:
        return {"answer": ", ".join(outlet_info.get("phone_numbers", []))}

    return {"answer": "Sorry, I couldn’t find the specific information you're looking for."}
