import tkinter as tk

def convert_temp():
    fahrenheit = entry_fahrenheit.get()
    if fahrenheit.replace('.', '', 1).isdigit() or (fahrenheit.startswith('-') and fahrenheit[1:].replace('.', '', 1).isdigit()):
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5 / 9
        label_celsius.config(text=f"{celsius:.2f} °C")
    else:
        label_celsius.config(text="Invalid Input")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create and place widgets
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Fahrenheit input
label_fahrenheit = tk.Label(frame, text="Fahrenheit (°F):")
label_fahrenheit.grid(row=0, column=0, padx=10, pady=5)
entry_fahrenheit = tk.Entry(frame, width=10)
entry_fahrenheit.grid(row=0, column=1, padx=10, pady=5)

# Convert button
button_convert = tk.Button(frame, text="Convert", command=convert_temp)
button_convert.grid(row=0, column=2, padx=10, pady=5)

# Celsius output
label_result = tk.Label(frame, text="Celsius (°C):")
label_result.grid(row=0, column=3, padx=10, pady=5)
label_celsius = tk.Label(frame, text="0.00 °C", width=10)
label_celsius.grid(row=0, column=4, padx=10, pady=5)

# Run the application
root.mainloop()