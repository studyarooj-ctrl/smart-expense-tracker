# Project Requirements & Tech Stack

## 1. Frontend Development

- **HTML5:** App ka basic structure aur skeleton pages (Dashboard, Forms, Tables).
- **CSS3:** Styling, responsive layouts, responsive cards, aur UI design.
- **JavaScript (Vanilla JS):** Dynamic behavior, client-side validation, UI updates.
- **Chart.js:** Visual data depiction (Pie charts, Bar charts, monthly spending trends).

---

## 2. Backend Development & API

- **Python:** Core language for logic, calculations, and data processing.
- **Flask Framework:** Lightweight web server to route pages and handle backend requests.
- **Internal REST APIs:** Flask routes (`/api/monthly-summary`, `/api/category-breakdown`) for frontend-backend data exchange.

---

## 3. Database & Storage

- **SQLite:** Lightweight, local file-based database (Privacy-first design).
- **SQLAlchemy (ORM):** Manages DB operations in Python without writing raw SQL.
- **CSV Data Handling:** Module for importing/exporting user data backups.

---

## 4. Data Analysis & Processing

- **pandas:** Data manipulation, aggregation, and monthly financial summary calculations.
- **python-dateutil:** Smart date handling for recurring expenses and monthly filtering.

---

## 5. Advanced Features (Post-MVP / Phase 2)

> _Note: Yeh technologies MVP implementation ke baad add hongi._

- **scikit-learn:** Transaction descriptions se auto-category suggestion ML model.
- **Tesseract OCR + pytesseract:** Receipt photos se text reading capability.
- **Pillow (PIL):** Image pre-processing for better OCR results.

---

## 6. Testing & Quality Assurance

- **pytest:** Automated test runner for backend functions, calculations, and routes.

---

## 7. Tooling, Version Control & Deployment

- **VS Code:** Primary IDE for full-stack code development.
- **Git & GitHub:** Version control, backup, and public portfolio repository.
- **Local Server:** Built-in Flask server (`http://127.0.0.1:5000`) for development.
- **Deployment (Optional):** Render / PythonAnywhere free-tier (Future deployment).
