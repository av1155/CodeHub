import time
import tkinter as tk
from math import cos, pi, sin


def update_clock():
    current_time = time.strftime("%I:%M:%S %p", time.localtime())
    current_date = time.strftime("%A, %B %d, %Y", time.localtime())
    label_time.config(text=current_time)
    label_date.config(text=current_date)
    update_analog_clock()
    root.after(
        1000, update_clock
    )  # Update the clock every 1000 milliseconds (1 second)


def update_analog_clock():
    # Clear previous drawings
    canvas.delete("all")

    # Get current time
    current_time = time.localtime()
    hours, minutes, seconds = (
        current_time.tm_hour,
        current_time.tm_min,
        current_time.tm_sec,
    )

    # Draw clock face with a subtle gradient
    canvas.create_oval(50, 50, 250, 250, outline=text_color, width=2, fill="#D8D8D8")

    # Draw hour hand
    hour_angle = pi / 2 - 2 * pi * (hours % 12) / 12 - 2 * pi * minutes / (12 * 60)
    hour_x = 150 + 60 * cos(hour_angle)
    hour_y = 150 - 60 * sin(hour_angle)
    canvas.create_line(
        150, 150, hour_x, hour_y, fill=text_color, width=8, arrow=tk.LAST
    )

    # Draw minute hand
    minute_angle = pi / 2 - 2 * pi * minutes / 60
    minute_x = 150 + 80 * cos(minute_angle)
    minute_y = 150 - 80 * sin(minute_angle)
    canvas.create_line(
        150, 150, minute_x, minute_y, fill=text_color, width=6, arrow=tk.LAST
    )

    # Draw second hand
    second_angle = pi / 2 - 2 * pi * seconds / 60
    second_x = 150 + 90 * cos(second_angle)
    second_y = 150 - 90 * sin(second_angle)
    canvas.create_line(150, 150, second_x, second_y, fill="#FF0000", width=2)

    # Draw a circle to hide the center where the hands meet
    canvas.create_oval(142, 142, 158, 158, fill=text_color, outline=text_color)


root = tk.Tk()
root.title("Digital and Analog Clock")
window_width = 400
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

font_size = 40
font_style = ("Arial", font_size, "bold")

background_color = "#F0F0F0"  # Light gray background color
text_color = "#444444"  # Dark gray text color

root.configure(bg=background_color)

label_time = tk.Label(
    root, font=font_style, text="", fg=text_color, bg=background_color
)
label_time.pack(expand=True, pady=20)

label_date = tk.Label(
    root, font=("Arial", 16), text="", fg=text_color, bg=background_color
)
label_date.pack(expand=True, pady=(0, 20))

# Create a canvas to draw the analog clock
canvas = tk.Canvas(root, width=300, height=300, bg=background_color)
canvas.pack(pady=20)

update_clock()
root.mainloop()
