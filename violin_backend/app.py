from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import uuid
from call_audiveris import run_audiveris
from parse_musicxml import parse_musicxml

app = Flask(__name__)
CORS(app)  # 允许来自 iOS 前端的跨域访问

BASE_UPLOAD_FOLDER = "/Users/brucelan/Desktop/violin_uploads"
BASE_OUTPUT_FOLDER = "/Users/brucelan/Desktop/violin_output"
os.makedirs(BASE_UPLOAD_FOLDER, exist_ok=True)
os.makedirs(BASE_OUTPUT_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"status": "error", "message": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"status": "error", "message": "No selected file"}), 400

    # ✅ 为每个请求生成唯一 session 文件夹
    session_id = str(uuid.uuid4())
    upload_folder = os.path.join(BASE_UPLOAD_FOLDER, session_id)
    output_folder = os.path.join(BASE_OUTPUT_FOLDER, session_id)
    os.makedirs(upload_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    # ✅ 使用原始文件名保存，防止冲突
    image_path = os.path.join(upload_folder, file.filename)
    file.save(image_path)
    print(f"✅ [{session_id}] 已保存上传图片: {image_path}")

    try:
        # ✅ 调用 Audiveris
        xml_path = run_audiveris(image_path, output_folder)
        print(f"🎼 [{session_id}] Audiveris 生成文件: {xml_path}")

        # ✅ 解析结果
        parent_dir = os.path.dirname(xml_path)
        result = parse_musicxml(parent_dir)
        print(f"🎻 [{session_id}] 指法识别结果: {result}")

        return jsonify({
            "status": "success",
            "data": result,
            "xml_file": xml_path,
            "session": session_id  # 可选，前端调试用
        })

    except Exception as e:
        print(f"❌ [{session_id}] 处理失败: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)  # 支持局域网访问