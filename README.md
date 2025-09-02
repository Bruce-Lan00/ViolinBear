# ViolinBear 🎻

ViolinBear is an experimental iPad + backend app that helps violin learners and players by **recognizing sheet music** and **automatically generating fingering suggestions**.

- **Frontend**: SwiftUI iPad app – upload a photo of sheet music and visualize fingerings on top of the score.
- **Backend**: Python Flask API – handles recognition, communicates with Audiveris, and returns fingering JSON.
- **OMR Engine**: [Audiveris](https://audiveris.org/) (not included in repo).

---

## Features (Current & Planned)
- Upload sheet music (image/PDF).
- Convert to MusicXML using Audiveris.
- Generate structured fingering JSON.
- Overlay fingerings (color + number) on the score.
- Future plans: position shifts, tape-assist for beginners, Apple Pencil annotations, offline cache.

---
