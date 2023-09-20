
# File Organizer

**File Organizer** is a Python script that helps you automatically organize files in a directory by moving them to specific subdirectories based on their file types. It uses the Watchdog library to monitor changes in the specified directory and performs file sorting accordingly.

## Features

- Organize files into the following categories:
  - Pictures
  - Videos
  - Music
  - Documents
  - Sound Effects
  - Torrents
  - 3D Printer Files
- Supported file types:
  - Images: jpg, jpeg, png, gif, and more
  - Videos: mp4, avi, mov, and more
  - Audio: mp3, wav, m4a, and more
  - Documents: doc, pdf, xls, txt, and more
  - 3D Printer Files: stl, f3d
- Automatically creates destination subdirectories if they don't exist.
- Logs file movements for easy tracking.

## Getting Started

To get started with **File Organizer**, follow these steps:

1. Clone this repository or download the script.

2. Install the required Python packages if not already installed:

   ```bash
   pip install watchdog
   ```

3. Open the script and modify the `srcDirectory` variable to specify the directory you want to monitor.

4. Run the script:

   ```bash
   python file_organizer.py
   ```

5. The script will continuously monitor the specified directory for file changes and organize them into the appropriate subdirectories based on their types.

## Configuration

You can customize the script by modifying the following variables:

- `srcDirectory`: The directory to monitor for file changes.
- `image_extensions`, `video_extensions`, `audio_extensions`, `document_extensions`, `printer3d_extensions`: Lists of supported file extensions for each category.
- Destination directories: You can change the names of the destination subdirectories (e.g., `picDir`, `videoDir`) to match your preferences.

## Contributions

Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- Mert Demirezen

---

