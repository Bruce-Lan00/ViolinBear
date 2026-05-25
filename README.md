# 🎻 ViolinBear – Automatic Fingering App

🌏 Languages: [English](README.md) | [中文](README.zh.md)

## 📝 Introduction
**ViolinBear** is an open-source project designed for **automatic violin sheet music recognition and fingering suggestion**. 

By leveraging Optical Music Recognition (OMR) and custom algorithmic heuristics, it allows violin learners and players to take a photo or upload an image of any sheet music and instantly receive annotated string and fingering guidance on their scores.

📺 **Watch the Live Project Demo (YouTube Shorts)**: [ViolinBear Run Demo](https://www.youtube.com/shorts/TlUFP1Flaps)

---

## 🏗 Architecture
The system is built as a decoupled, client-server ecosystem:

- **Frontend (Swift + SwiftUI)**: A native iOS/iPadOS application handling camera/photo capturing, seamless rendering, and interactive visual fingering overlays.
- **Backend (Flask)**: A lightweight Python microservice responsible for orchestrating the OMR pipeline, data processing, and handling requests.
- **OMR Engine (Java / Audiveris)**: A fully local `audiveris.jar` wrapper that processes raw score images and transcribes them into digital structured format (`MusicXML`).
- **Core Middleware (Python Algorithm)**: The brain of the project. It parses parsed XML structures and computes the optimal fingering trajectories based on violin physics.

---

## 🛠 Setup & Installation

Follow these steps to configure your local environment and get both the backend server and frontend client up and running.

### Prerequisites
Before diving in, ensure you have the following core dependencies installed on your Mac:
- **Python 3.10+**
- **Java JDK 17+** (Required to execute the local `audiveris.jar`)
- **Xcode** (With iOS/iPadOS 17+ SDK for frontend development)

---

### 1. Backend Configuration (Python + OMR)

#### Step 1: Navigate to the backend directory
Open your terminal and step into the backend workspace:
```bash
cd violin_backend
```

#### Step 2: Set up dependencies
To ensure clean dynamic library linkage (such as `pyexpat`) without system python conflicts, install the required framework packages directly using the following execution path:
```bash
/usr/bin/python3 -m pip install flask flask-cors requests
```

#### Step 3: Verify the Java Environment
Ensure the terminal can successfully call the Java Virtual Machine for Audiveris:
```bash
java -version
```
*(If this command fails or returns an error, please download and install a standard macOS JDK from Oracle or adoptium.net).*

#### Step 4: Boot the Server
Run the Flask server instance:
```bash
/usr/bin/python3 app.py
```
Upon a successful initialization, the console will output your server's access endpoints:
```text
* Serving Flask app 'app'
* Debug mode: on
* Running on all addresses (0.0.0.0)
* Running on [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Running on [http://172.28.96.34:8000](http://172.28.96.34:8000) (Your Local LAN IP)
```
*Keep this terminal window running in the background.*

---

### 2. Frontend Configuration (iOS / iPadOS)

#### Step 1: Open the Project
Launch Finder, navigate to `Frontend/ViolinBear`, and double-click **`ViolinBear.xcodeproj`** to load the complete project bundle inside Xcode.

#### Step 2: Configure Server Endpoint
In Xcode, use `Cmd + Shift + F` to globally locate the API server variable (e.g., `baseURL`). 
- **If debugging on an iPad/iPhone device (Recommended)**: Point the URL to your Mac's active Local LAN IP shown by your terminal (e.g., `http://172.28.96.34:8000`). Make sure your Mac and iOS device are connected to the same Wi-Fi network.
- **If debugging via Simulator**: Keep the endpoint as `http://127.0.0.1:8000`.

#### Step 3: Deployment & Code-Signing
1. Go to the project properties under **Signing & Capabilities**.
2. Select your personal Apple ID under the **Team** dropdown menu to clear code-signing warnings.
3. If deploying to physical hardware, ensure you toggle **Developer Mode** to **ON** directly inside your iPhone or iPad's *Settings -> Privacy & Security*.

#### Step 4: Run the Application
Select your connected target hardware platform from Xcode's device selector dropdown at the top, and hit **`Cmd + R`** (or click the **🔼 Play** button) to compile and flash the app.

---

## 🗺 Feature Roadmap

### Phase 1: Basic Validation (MVP - Current)
- [x] Cloud-based microservice orchestrating a local Audiveris pipeline.
- [x] Hard-coded 1st position mapping logic constraint models (D4–A4 string boundaries).
- [x] Structured JSON payloads parsing outputting accurate notation coordinate metrics.
- [x] Dynamic high-fidelity rendering overlays within the SwiftUI view state canvas.

### Phase 2: Multi-Position Fingering (Next Up)
- [ ] Implement robust multi-position matrix maps (shifting to 3rd, 5th, and higher positions).
- [ ] Design heuristic graph-search pathfinders aimed at minimizing rapid string crossings and unnecessary shift friction.
- [ ] Support complex rhythmic syncopation structures and custom accidental symbols.

### Phase 3: Edge-AI Inference (Long-term)
- [ ] Migrate the core OMR processing pipeline from server-side modules down to local assets using Swift-native CoreML architectures.
- [ ] Establish dataset pipelines leveraging Suzuki & IMSLP corpus repositories to fine-tune generative finger-placement profiles.

---

## 🤝 Contributing
ViolinBear is currently in its early incubation phase, and the codebase is rapidly evolving. We deeply appreciate active collaborations from software developers, ML scientists, UX experts, and classical musicians alike!

- **Encountered an anomaly?** Open an [Issue](https://github.com/Bruce-Lan00/ViolinBear/issues) detailing the stack logs or sheet layout.
- **Have an algorithmic optimization?** Refine our Python middleware heuristics and drop a Pull Request!
- **Share your experiences:** We'd love to hear how ViolinBear handles your custom repertoire sheets.

Let’s build ViolinBear into a truly useful tool for the global violin community! 🎻
