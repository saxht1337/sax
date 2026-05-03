from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

print("Sistem başarıyla başlatıldı ve veritabanına bağlanmaya çalışıyor...")

# Frontend'den erişim izni
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Kopyaladığın URI'yi buraya yapıştır (Şifreni yazmayı unutma!)
DATABASE_URL = "postgresql://postgres:[Alitutus133.]@db.fqdjyqdqppscsrgtvruw.supabase.co:5432/postgres"

def get_db_connection():
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)

@app.get("/formalar")
async def get_jerseys():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE status = 'satista'")
        jerseys = cur.fetchall()
        cur.close()
        conn.close()
        return jerseys
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/odeme-yap")
async def create_payment(order: dict):
    # PayTR entegrasyonu buraya gelecek
    # Şimdilik simüle ediyoruz
    return {"status": "success", "message": "PayTR iFrame oluşturuldu"}