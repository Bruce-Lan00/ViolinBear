# 🎻 ViolinBear – Automatic Fingering App

🌏 Languages: [English](README.md) | [中文](README.zh.md)

## Introduction
ViolinBear is an open-source project for **automatic violin sheet music recognition and fingering suggestion**.  
It integrates **[Audiveris OMR](https://github.com/Audiveris/audiveris)**, a **Python backend**, and a **SwiftUI frontend app**, to help learners and players get instant fingering annotations on scores.  

---

## Architecture
- **Frontend (Swift + SwiftUI)**:  
  UI, annotations, score upload  
- **Backend (Flask / FastAPI)**:  
  Calls Audiveris, manages results & caching  
- **OMR Engine (Docker + Java)**:  
  Converts score images → MusicXML/JSON  
- **Middleware (Python)**:  
  Format conversion & fingering logic  
- **Database (PostgreSQL / MongoDB)**:  
  Stores scores, user data, recognition results  

---

## Feature Roadmap
### Phase 1: Basic Validation
- Hard-coded 1st position notes (D4–A4, etc.)  
- Parse MusicXML, check if playable in 1st position  
- Return JSON with string & fingering  

### Phase 2: Multi-Position Fingering
- Multi-position mapping + heuristics (minimize shifts, avoid crossings)  
- Output optimal fingering route for whole melody  

### Phase 3 (Optional): Machine Learning
- Use Suzuki / IMSLP datasets  
- Train models to suggest stylistic fingerings  

---

## Roadmap
- **MVP (Now)**: Backend OMR + App display (requires internet)  
- **2.0**: JSON caching + offline display (after initial sync)  
- **3.0**: On-device Swift ML inference → fully offline  

---

## 🤝 Contributing
This project is still in an early stage, with many features incomplete.  
We welcome contributions from developers and musicians alike:  

- Open issues (feature requests / bug reports)  
- Submit PRs (code, algorithms, UI improvements)  
- Share your ideas and experiences  

Let’s build ViolinBear into a truly useful tool! 
