# 🌳 Kijani Kinga

Kijani Kinga is a **mobile-friendly Django web application** that empowers local residents, rangers, and administrators to report, track, and analyze incidents of illegal logging.  
The system supports geotagged reports with photos or audio evidence, sends alerts to authorities, and provides an interactive map and analytics dashboard for better decision making.


## 🚀 Features

- **Role-based access** - Residents, Rangers, and Admins have tailored permissions.
- **Report submission** - Users can submit incidents with images, audio, and GPS coordinates.
- **Report moderation** - Rangers/Admins can verify, approve, or close reports.
- **Geolocation capture** - Location auto-captured via GPS or manual map input.
- **Interactive map** - Incidents visualized on OpenStreetMap.
- **Media handling** - Secure storage of images and audio with Cloudinary.
- **Notifications** - SMS (Twilio) and Email (SendGrid) alerts for urgent reports.
- **Analytics dashboard** - Track trends by location, time, and status.


## 🛠 Tech Stack

- **Backend Framework:** Django + Django REST Framework  
- **Database:** PostgreSQL (+ PostGIS for spatial queries)  
- **Maps & Geocoding:** OpenStreetMap + Nominatim  
- **Media Storage:** Cloudinary  
- **Notifications:** Twilio (SMS), SendGrid (Email)  
- **Task Queue:** Celery + Redis  
- **Frontend Integration:** Leaflet.js for maps (future React/Next.js support)  


## 📡 API Endpoints

| Endpoint                              | Method | Description                       |
|---------------------------------------|--------|-----------------------------------|
| `/api/reports/`                       | GET, POST | Submit or list reports           |
| `/api/reports/<id>/verify/`           | POST   | Verify a report                  |
| `/api/reports/<id>/close/`            | POST   | Close a report                   |
| `/api/media/upload/`                  | POST   | Upload media to Cloudinary       |
| `/api/geocoding/reverse-lookup/`      | GET    | Get address from coordinates     |
| `/api/stats/summary/`                 | GET    | Fetch analytics summary          |



## 🔐 User Roles

- **Resident** - Submit reports, view own submissions.  
- **Ranger** - Verify/close reports, receive notifications.  
- **Admin** - Full access to manage users, reports, and analytics.  


## ⚡ Setup Instructions

### Prerequisites
- Python 3.10+
- PostgreSQL (with PostGIS if using spatial queries)
- Redis (for Celery tasks)
- Cloudinary, Twilio, and SendGrid accounts (API keys)

### Installation

```bash
# Clone the repo
git clone https://github.com/Samuel-Njoroge/kijani-kinga.git
cd kijani-kinga/backend

# Create virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run initial migrations
python manage.py migrate

# Start development server
python manage.py 
```


## 🤝 Contributing

Contributions are welcome!:

1. Create a feature branch **(git checkout -b feature/xyz)**

2. Commit changes **(git commit -m "Add xyz feature")**

3. Push to branch **(git push origin feature/xyz)**

4. Open a Pull Request into **develop**