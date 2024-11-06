from flask import Flask, render_template_string, request, send_file
import yt_dlp
import os

app = Flask(__name__)

# HTML template with Tailwind CSS, Material Icons, and Android-like UI
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Downloader</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
        /* Container and card animation */
        .card {
            animation: slideIn 0.5s ease;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .card:hover {
            transform: translateY(-3px);
            box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.2);
        }

        /* Button animation */
        .btn {
            transition: transform 0.1s ease;
        }
        .btn:active {
            transform: scale(0.95);
        }

        /* Slide-in effect */
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">

    <!-- Card container with animated slide-in effect -->
    <div class="bg-white p-6 rounded-2xl shadow-xl w-full max-w-md card">
        <div class="flex justify-center items-center mb-6">
            <span class="material-icons text-blue-500 text-5xl">cloud_download</span>
            <h2 class="text-2xl font-bold text-gray-800 ml-2">YouTube Video Downloader</h2>
        </div>

        <!-- URL and Path Input Form -->
        <form action="/" method="post" class="space-y-6">
            <div class="flex items-center border-b-2 border-gray-300 py-2 focus-within:border-blue-500 transition-all">
                <span class="material-icons text-gray-500 mr-2">link</span>
                <input type="url" name="video_url" placeholder="Enter YouTube URL" required 
                       class="w-full outline-none text-gray-700 placeholder-gray-400 transition-colors focus:text-gray-900" />
            </div>
            <div class="flex items-center border-b-2 border-gray-300 py-2 focus-within:border-blue-500 transition-all">
                <span class="material-icons text-gray-500 mr-2">folder</span>
                <input type="text" name="save_path" placeholder="Save Location" value="/storage/emulated/0/Download/Seal" required 
                       class="w-full outline-none text-gray-700 placeholder-gray-400 transition-colors focus:text-gray-900" />
            </div>
            <div class="flex justify-center mt-6">
                <!-- Animated button -->
                <button type="submit" 
                        class="bg-blue-500 text-white w-full py-3 rounded-lg shadow btn transition-all flex items-center justify-center hover:bg-blue-600">
                    <span class="material-icons mr-2">download</span>
                    Fetch Formats
                </button>
            </div>
        </form>

        <!-- Format Selection and Download Button -->
        {% if formats %}
        <div class="mt-8">
            <h3 class="text-lg font-semibold text-gray-800 mb-3">Select Video Quality</h3>
            <form action="/download" method="post">
                <input type="hidden" name="video_url" value="{{ video_url }}">
                <input type="hidden" name="save_path" value="{{ save_path }}">
                <div class="space-y-3">
                    {% for f in formats %}
                    <!-- Animated selection card -->
                    <label class="flex items-center bg-gray-50 rounded-lg p-4 shadow-sm cursor-pointer hover:bg-blue-50 transition-all">
                        <input type="radio" name="format_id" value="{{ f['format_id'] }}" required class="mr-3">
                        <span class="text-gray-700">{{ f['format_id'] }} - {{ f['ext'] }} ({{ f.get('format_note', '') }}) - {{ f.get('height', 'N/A') }}p</span>
                    </label>
                    {% endfor %}
                </div>
                <div class="flex justify-center mt-6">
                    <!-- Animated download button -->
                    <button type="submit" 
                            class="bg-green-500 text-white w-full py-3 rounded-lg shadow btn transition-all flex items-center justify-center hover:bg-green-600">
                        <span class="material-icons mr-2">file_download</span>
                        Download Video
                    </button>
                </div>
            </form>
        </div>
        {% endif %}
    </div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form["video_url"]
        save_path = request.form["save_path"]
        
        # Fetch available formats for user to select quality
        with yt_dlp.YoutubeDL() as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            formats = info_dict.get("formats", None)
        
        return render_template_string(HTML_TEMPLATE, formats=formats, video_url=video_url, save_path=save_path)
    return render_template_string(HTML_TEMPLATE)

@app.route("/download", methods=["POST"])
def download():
    video_url = request.form["video_url"]
    save_path = request.form["save_path"]
    format_id = request.form.get("format_id", None)
    
    # Ensure the specified directory exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    ydl_opts = {
        "outtmpl": f"{save_path}/%(title)s.%(ext)s",
        "format": format_id,  # Set selected format for download
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
        video_file = ydl.prepare_filename(info_dict)
    
    return send_file(video_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)