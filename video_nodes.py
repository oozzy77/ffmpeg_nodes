from datetime import datetime
import subprocess
import os
from typing import Literal
from nozyio.config_utils import nz_config

VIDEO_FORMATS = [".mov", ".mp4", ".avi", ".mkv", ".webm", ".flv", ".wmv", ".mpeg", ".mpg", ".m4v", ".3gp", ".3g2", ".ogg", ".ogv"]
def video_to_gif(
    video: str, output_width: int = 512, fps: int = 30, output_name: str = "output") -> str:
    """
    Converts a video file to a GIF using ffmpeg with customizable scale and fps.
    """
    output_folder = nz_config.get("output_path", "output")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_file = os.path.join(output_folder, f"{output_name}_{timestamp}.gif")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    try:
        # Build the ffmpeg command
        command = [
            'ffmpeg',
            '-i', video,  # Input file
            '-vf', f"fps={fps},scale={output_width}:-1",  # Apply fps and scale filters
            output_file  # Output GIF file
        ]
        
        # Run the ffmpeg command
        subprocess.run(command, check=True)
        
        # Return the output file path
        return os.path.abspath(output_file)
    
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        return None

video_to_gif.NOZY_NODE_DEF = {
    "node_title": "Video to GIF",
    "description": "Converts a video file to a GIF using ffmpeg with customizable scale and fps.",
    "inputs": {
        "video": {
            "type": "filepath",
            "accept": [".mov", ".mp4", ".avi", ".mkv", ".webm", ".flv", ".wmv", ".mpeg", ".mpg", ".m4v", ".3gp", ".3g2", ".ogg", ".ogv"],
            # "hide_handle": True,
            "description": "The input video file."
        },
        "output_width": {
            "type": "int",
            "description": "The width of the output GIF."
        },
        "fps": {
            "type": "int",
            "description": "The frame rate of the output GIF."
        }
    }
}


def convert_video_format(
    video: str, output_width: int = 512, fps: int = 30, output_name: str = "output",
    output_format: Literal[".mov", ".mp4", ".avi", ".mkv", ".webm", ".flv", ".wmv", ".mpeg", ".mpg", ".m4v", ".3gp", ".3g2", ".ogg", ".ogv", ".gif"] = ".mp4") -> str:
    output_folder = nz_config.get("output_path", "output")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_file = os.path.join(output_folder, f"{output_name}_{timestamp}{output_format}")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    try:
        # Build the ffmpeg command
        command = [
            'ffmpeg',
            '-i', video,  # Input file
            '-vf', f"fps={fps},scale={output_width}:-1",  # Apply fps and scale filters
            output_file  # Output GIF file
        ]
        
        # Run the ffmpeg command
        subprocess.run(command, check=True)
        
        # Return the output file path
        return os.path.abspath(output_file)
    
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        return None

convert_video_format.NOZY_NODE_DEF = {
    "node_title": "Convert Video Format",
    "description": "Converts a video file format using ffmpeg with customizable scale and fps.",
    "inputs": {
        "video": {
            "type": "filepath",
            "accept": [".mov", ".mp4", ".avi", ".mkv", ".webm", ".flv", ".wmv", ".mpeg", ".mpg", ".m4v", ".3gp", ".3g2", ".ogg", ".ogv"],
            # "hide_handle": True,
            "description": "The input video file."
        },
        "output_width": {
            "type": "int",
            "description": "The width of the output GIF."
        },
        "fps": {
            "type": "int",
            "description": "The frame rate of the output GIF."
        }
    }
}