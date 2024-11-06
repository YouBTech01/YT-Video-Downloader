# YouTube Video Downloader 🌐📥

A simple yet powerful web application built using **Flask** and **yt-dlp** (a fork of youtube-dl) to download YouTube videos in various formats. With a user-friendly interface featuring **Tailwind CSS** and **Material Icons**, the app allows users to easily select and download videos from YouTube by providing a URL.

This application is designed to work seamlessly on both mobile and desktop devices, mimicking an **Android-like UI** for a smooth and intuitive user experience. 🎬📱

---

## Features 🌟

- **Fetch Available Formats**: Get a list of available formats and resolutions for the provided YouTube video URL.
- **Select Video Quality**: Choose from multiple available formats like MP4, WEBM, MP3, and others.
- **Download Videos**: After selecting the preferred format, you can directly download the video to a specified location on your system.
- **Sleek, Responsive UI**: Built using **Tailwind CSS**, this web app features a modern, mobile-first, responsive design.
- **Material Icons**: Utilizes **Material Design Icons** to enhance the user interface with easily recognizable icons for actions like download, link, and folder selection.
- **Save Location**: Customize the location where the video will be saved on your device.
  
---

## Technologies Used ⚙️

This project integrates the following technologies to create a seamless video downloading experience:

- **Flask**: A lightweight Python web framework that serves the app and handles requests.
- **yt-dlp**: A Python package to extract video formats and download videos from YouTube (and other platforms) with high customization.
- **Tailwind CSS**: A utility-first CSS framework used for building the clean and responsive layout.
- **Material Icons**: Google’s icon library used for enhancing the visual interface with modern, clear icons.
  
---

## Screenshots 📸

Here’s how the app looks in action:

- **Main Page**: Input the YouTube video URL and select the save location.
  
  [App Screenshot 1](https://github.com/user-attachments/assets/d6292ff1-bd40-4a71-8db5-ffe0f16d24c6)

---

## How It Works 🔍

1. **Home Page**: When you open the application, you'll see a simple form where you can enter a YouTube video URL. Along with the URL, you can specify a path on your computer where the downloaded video will be saved. The save path has a default value set to `/storage/emulated/0/Download/Seal` for convenience (particularly if you’re testing on an Android device).

2. **Fetching Video Formats**: After entering the video URL and save path, clicking on the **"Fetch Formats"** button will query YouTube for available download formats (e.g., different resolutions, file types like MP4, MP3, and more). The server (using `yt-dlp`) retrieves these formats and presents them to the user for selection.

3. **Select Format and Download**: Once the formats are displayed, the user can select the preferred quality/format for the video. After selecting the format, they can click on **"Download Video"** to begin the download process.

4. **Download**: The video is downloaded to the specified location on the system. The video is retrieved using the selected format (resolution, file type, etc.) and saved to the local directory.

---

## Installation 🔧

### Prerequisites:
Before you run the app, ensure you have the following tools and libraries installed:

- **Python 3.x**: This app is built using Python 3, so you'll need a working Python environment.
- **yt-dlp**: The core package for downloading YouTube videos. This package is based on the well-known youtube-dl.
- **Flask**: The web framework that powers the application.

### Step-by-Step Installation:
1. **Clone the Repository**:
   Clone this repository to your local machine:

