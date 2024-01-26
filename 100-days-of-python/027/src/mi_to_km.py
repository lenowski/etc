"""
Converts miles to kilometres
"""


import tkinter as tk

MILE_FACTOR = 1.609344


def mi_to_km(mi_input, km_value):
    mi = float(mi_input.get())
    km = round(mi * MILE_FACTOR, 2)
    km_value.config(text=f"{km}")


def main():
    # Window
    window = tk.Tk()
    window.title("Convert: mi => km")
    window.config(padx=50, pady=50)

    # Labels
    mile_label = tk.Label(text="mi")
    mile_label.grid(column=2, row=0)

    is_equal_label = tk.Label(text="is equal to")
    is_equal_label.grid(column=0, row=1)

    km_label = tk.Label(text="km")
    km_label.grid(column=2, row=1)

    km_value = tk.Label(text="0")
    km_value.grid(column=1, row=1)

    # Entry
    mi_input = tk.Entry(width=10)
    mi_input.grid(column=1, row=0)

    # Button
    button = tk.Button(
        window, text="Calculate", command=lambda: mi_to_km(mi_input, km_value)
    )
    button.grid(column=1, row=2)

    window.mainloop()


if __name__ == "__main__":
    main()
