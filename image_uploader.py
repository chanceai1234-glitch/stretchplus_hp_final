import http.server
import socketserver
import json
import base64
import os
import webbrowser

PORT = 8000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_FINAL_DIR = os.path.join(BASE_DIR, "image_final")

class UploaderHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            # Get list of images
            if not os.path.exists(IMAGE_FINAL_DIR):
                os.makedirs(IMAGE_FINAL_DIR)
            images = sorted([f for f in os.listdir(IMAGE_FINAL_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.svg'))])
            options = "".join([f"<option value='{img}'>{img}</option>" for img in images])
            
            html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>HP画像 かんたん差し替えアップローダー</title>
    <style>
        body {{ font-family: sans-serif; max-width: 600px; margin: 40px auto; padding: 20px; background: #f9f9f9; }}
        h1 {{ color: #333; }}
        .box {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        select, input {{ display: block; width: 100%; margin: 10px 0 20px; padding: 10px; font-size: 16px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box; }}
        button {{ background: #5fb4d4; color: white; border: none; padding: 15px 20px; font-size: 18px; border-radius: 4px; cursor: pointer; width: 100%; font-weight: bold; }}
        button:hover {{ background: #4a9ebc; }}
        #status {{ margin-top: 20px; font-weight: bold; color: green; text-align: center; white-space: pre-wrap; }}
    </style>
</head>
<body>
    <h1>画像かんたん差し替えツール</h1>
    <div class="box">
        <p>1. 差し替えたい対象を選択:</p>
        <select id="targetImage">
            {options}
        </select>
        
        <p>2. 新しい画像ファイルを選択:</p>
        <input type="file" id="fileInput" accept=".png,.jpg,.jpeg,.svg">
        
        <button onclick="upload()">画像を上書きする</button>
        <div id="status"></div>
    </div>

    <script>
        function upload() {{
            const targetImage = document.getElementById('targetImage').value;
            const fileInput = document.getElementById('fileInput');
            const statusDiv = document.getElementById('status');
            
            if (!targetImage) {{
                alert('差し替え対象を選択してください');
                return;
            }}
            if (!fileInput.files.length) {{
                alert('新しい画像ファイルを選択してください');
                return;
            }}
            
            const file = fileInput.files[0];
            const reader = new FileReader();
            reader.onload = function(e) {{
                const base64Data = e.target.result.split(',')[1];
                
                statusDiv.innerText = "アップロード中...";
                
                fetch('/upload', {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{ filename: targetImage, data: base64Data }})
                }}).then(res => res.json()).then(data => {{
                    if (data.success) {{
                        statusDiv.style.color = 'green';
                        statusDiv.innerText = "成功！ " + targetImage + " を上書きしました。\\n※HPの確認画面でスーパーリロードをお試しください。";
                        
                        // Clear file input
                        fileInput.value = "";
                    }} else {{
                        statusDiv.style.color = 'red';
                        statusDiv.innerText = "エラー: " + data.error;
                    }}
                }}).catch(err => {{
                    statusDiv.style.color = 'red';
                    statusDiv.innerText = "通信エラー: " + err;
                }});
            }};
            reader.readAsDataURL(file);
        }}
    </script>
</body>
</html>"""
            self.wfile.write(html.encode('utf-8'))
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/upload':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                filename = data.get('filename')
                base64_data = data.get('data')
                
                if not filename or not base64_data:
                    raise ValueError("不正なデータ")
                
                # Security check
                if '/' in filename or '\\' in filename or filename.startswith('.'):
                    raise ValueError("不正なファイル名")
                
                filepath = os.path.join(IMAGE_FINAL_DIR, filename)
                
                # Write file
                with open(filepath, 'wb') as f:
                    f.write(base64.b64decode(base64_data))
                
                response = {"success": True}
            except Exception as e:
                response = {"success": False, "error": str(e)}
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == "__main__":
    try:
        with ReusableTCPServer(("", PORT), UploaderHandler) as httpd:
            print(f"Server started at http://localhost:{PORT}/")
            print("ブラウザを開いています...")
            webbrowser.open(f'http://localhost:{PORT}/')
            print("この黒い画面は開いたままにしてください。終了する場合は Ctrl+C を押してください。")
            httpd.serve_forever()
    except OSError as e:
        if e.errno == 48:
            print(f"エラー: ポート {PORT} はすでに使用されています。")
            print("すでにこのツールが開かれているか、別のプログラムが使用しています。")
            webbrowser.open(f'http://localhost:{PORT}/')
        else:
            print(f"エラーが発生しました: {e}")
