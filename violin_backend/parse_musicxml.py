import zipfile
import xml.etree.ElementTree as ET
import os

def parse_musicxml(input_dir):
    multi_position_notes = {
    # G string (blue)
    'G3':   [('G string', '0', '1st position', 'blue')],
    'G#3':  [('G string', '1+', '1st position', 'blue')],
    'Ab3':  [('G string', '1+', '1st position', 'blue')],
    'A3':   [('G string', '1', '1st position', 'blue')],
    'A#3':  [('G string', '1-', '1st position', 'blue')],
    'Bb3':  [('G string', '1-', '1st position', 'blue')],
    'B3':   [('G string', '2', '1st position', 'blue')],
    'C4':   [('G string', '2-', '1st position', 'blue')],
    'C#4':  [('G string', '3', '1st position', 'blue')],
    'Db4':  [('G string', '3+', '1st position', 'blue')],
    'D4':   [
        ('G string', '4', '1st position', 'blue'),
        ('D string', '0', '1st position', 'orange')
    ],

    # D string (orange)
    'D#4':  [('D string', '1+', '1st position', 'orange')],
    'Eb4':  [('D string', '1+', '1st position', 'orange')],
    'E4':   [('D string', '1', '1st position', 'orange')],
    'F4':   [('D string', '1-', '1st position', 'orange')],
    'F#4':  [('D string', '2', '1st position', 'orange')],
    'Gb4':  [('D string', '2-', '1st position', 'orange')],
    'G4':   [
        ('D string', '3', '1st position', 'orange'),
        ('A string', '0', '1st position', 'green')
    ],
    'G#4':  [('D string', '3-', '1st position', 'orange')],
    'Ab4':  [('D string', '3-', '1st position', 'orange')],
    'A4':   [
        ('D string', '4', '1st position', 'orange'),
        ('A string', '0', '1st position', 'green')
    ],

    # A string (green)
    'A#4':  [('A string', '1+', '1st position', 'green')],
    'Bb4':  [('A string', '1+', '1st position', 'green')],
    'B4':   [('A string', '1', '1st position', 'green')],
    'C5':   [('A string', '1-', '1st position', 'green')],
    'C#5':  [('A string', '2', '1st position', 'green')],
    'Db5':  [('A string', '3+', '1st position', 'green')],
    'D5':   [('A string', '3', '1st position', 'green')],
    'D#5':  [('A string', '3-', '1st position', 'green')],
    'Eb5':  [('A string', '3-', '1st position', 'green')],
    'E5':   [
        ('A string', '4', '1st position', 'green'),
        ('E string', '0', '1st position', 'red')
    ],

    # E string (red)
    'F5':   [('E string', '1+', '1st position', 'red')],
    'F#5':  [('E string', '1', '1st position', 'red')],
    'G5':   [('E string', '1-', '1st position', 'red')],
    'G#5':  [('E string', '2', '1st position', 'red')],
    'Ab5':  [('E string', '2', '1st position', 'red')],
    'A5':   [('E string', '2-', '1st position', 'red')],
    'A#5':  [('E string', '3', '1st position', 'red')],
    'Bb5':  [('E string', '3', '1st position', 'red')],
    'B5':   [('E string', '3-', '1st position', 'red')],
    'C6':   [('E string', '4', '1st position', 'red')]
    }

    omr_file = None
    mxl_file = None
    for f in os.listdir(input_dir):
        if f.endswith(".omr"):
            omr_file = os.path.join(input_dir, f)
        elif f.endswith(".mxl"):
            mxl_file = os.path.join(input_dir, f)

    if not omr_file or not mxl_file:
        return {"status": "error", "message": "Missing .omr or .mxl file"}

    with zipfile.ZipFile(omr_file, 'r') as zip_ref:
        extract_dir = omr_file.replace('.omr', '_extracted')
        zip_ref.extractall(extract_dir)
        sheet_path = os.path.join(extract_dir, "sheet#1", "sheet#1.xml")
        tree = ET.parse(sheet_path)
        root = tree.getroot()

        lines = []
        for inters in root.iter("inters"):
            current_line = []
            for head in inters.findall("head"):
                bounds = head.find("bounds")
                if bounds is not None:
                    try:
                        x = float(bounds.attrib.get("x"))
                        y = float(bounds.attrib.get("y"))
                        current_line.append((x, y))
                    except:
                        continue
            current_line.sort(key=lambda p: p[0])
            if current_line:
                lines.append(current_line)

        positions = [pos for line in lines for pos in line]

    with zipfile.ZipFile(mxl_file, 'r') as z:
        xml_files = [name for name in z.namelist() if name.endswith('.xml')]
        with z.open(xml_files[0]) as f:
            tree = ET.parse(f)

    root = tree.getroot()
    for elem in root.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]

    notes = []
    prev_string = None
    for note in root.iter('note'):
        pitch = note.find('pitch')
        if pitch is None:
            continue
        step = pitch.find('step').text
        octave = pitch.find('octave').text
        alter_tag = pitch.find('alter')
        alter = ''
        if alter_tag is not None:
            alter_val = int(alter_tag.text)
            alter = '#' if alter_val == 1 else 'b' if alter_val == -1 else ''
        full_note = f"{step}{alter}{octave}"

        if full_note not in multi_position_notes:
            print(f"⚠️ Skipped note (not in fingering map): {full_note}")
            continue

        # ✅ 根据前一个音符的弦优先选择同一弦指法
        options = multi_position_notes[full_note]
        selected = options[0]
        for opt in options:
            if opt[0] == prev_string:
                selected = opt
                break

        prev_string = selected[0]  # 更新当前弦
        string, finger, position, color = selected
        note_dict = {
            "note": full_note,
            "string": string,
            "finger": finger,
            "position": position,
            "color": color
        }
        notes.append(note_dict)

    if len(notes) != len(positions):
        print(f"⚠️ Warning: Notes ({len(notes)}) != Positions ({len(positions)}). Truncating to match.")

    min_len = min(len(notes), len(positions))
    for i in range(min_len):
        notes[i]["x"] = positions[i][0]
        notes[i]["y"] = positions[i][1]

    return {
        "status": "parsed with truncation" if len(notes) != len(positions) else "parsed successfully",
        "notes": notes[:min_len]
    }
