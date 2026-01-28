import google.generativeai as genai

API_KEY = "AIzaSyCJb_loDx_uCgKcRmS5o5Eh7G7frKv5Ibo"
genai.configure(api_key=API_KEY)

print("--- BUSCANDO MODELOS DISPONIBLES ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ NOMBRE EXACTO: {m.name}")
except Exception as e:
    print(f"❌ Error: {e}")