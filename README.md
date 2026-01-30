# Lost Item Register

A modern, sleek web application for registering and searching for lost items. This project is designed with a premium SaaS-like UI, featuring smooth animations and a clean user experience.

## Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML5, TailwindCSS (CDN)
- **Animations:** GSAP (GreenSock Animation Platform)
- **Data Storage:** JSON-based persistence

## Core Features
- **Create Entry:** A comprehensive form to register lost items with details like category, location, date, and contact information. Includes a dynamic reward toggle.
- **Search Entries:** A powerful search and filter interface to browse through lost items. Features real-time filtering, category badges, and a detailed view modal.

## Project Structure
```
/lost-item-register/
  ├── app.py              # Flask application & API routes
  ├── README.md           # Project documentation
  ├── data/
  │   ├── lost-items.json       # Active data storage
  │   └── lost-items.seed.json  # Initial seed data
  ├── templates/
  │   └── index.html      # Main SPA template
  └── static/             # Static assets (CSS/JS)
```
kashanabbas checking
## How to Run Locally
1. Ensure you have Python installed.
2. Install Flask:
   ```bash
   pip install flask
   ```
3. Navigate to the project directory:
   ```bash
   cd lost-item-register
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and visit `http://127.0.0.1:5000`.

## Credits
**Group Project by:**
- Syed Kashan Abbas Naqvi
- Asghar Abbas
