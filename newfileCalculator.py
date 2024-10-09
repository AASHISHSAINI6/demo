import tkinter as tk

LARGE_FONT_STYAL = ("Arial", 40, "bold")
SMALL_FONT_STYAL = ("Arial", 16)
DIGITS_FONT_STYAL = ("Arial", 24, "bold")
DEFAULT_FONT_STYAL = ("Arial", 20)

OFF_WHITE = "#cdd1d7"
WHITE = "#ebeff2"
LIGHT_BLUE = "#f79225"
LIGHT_GRAY = "#262434"
LABEL_COLOR = "#000000"


class Calculater:
    def __init__(self):
        self.display = None
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("CALCULATER")
        
        # creating the Labels
        self.total_expression = ""
        self.current_expression = ""
        # Creating Frame
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        # Adding digits Buttons
        self.digits = {
            7: (1, 1),
            8: (1, 2),
            9: (1, 3),
            4: (2, 1),
            5: (2, 2),
            6: (2, 3),
            1: (3, 1),
            2: (3, 2),
            3: (3, 3),
            0: (4, 2),
        }
        # Adding operations
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+", ".": "."}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
       
        # Using for-loop for fit the buttons in window
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        # Adding digit buttons
        self.create_digit_buttons()
        self.create_operation_frame()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    # Function for Special button
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_one_by_one_clear_button()
        self.create_equal_button()
        self.create_square_button()
        self.create_dot_button()
        self.create_sqrt_button()

    # Function of Labels =>
    def create_display_labels(self):
        total_label = tk.Label(
            self.display_frame,
            text=self.total_expression,
            anchor=tk.E,
            bg=LIGHT_GRAY,
            fg=LABEL_COLOR,
            padx=24,
            font=SMALL_FONT_STYAL,
        )
        total_label.pack(expand=True, fill="both")
        label = tk.Label(
            self.display_frame,
            text=self.current_expression,
            anchor=tk.E,
            bg=LIGHT_GRAY,
            fg=LABEL_COLOR,
            padx=24,
            font=LARGE_FONT_STYAL,
        )
        label.pack(expand=True, fill="both")
        return total_label, label

    # Functions of the frames =>
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    # Function of digits
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(
                self.buttons_frame,
                text=str(digit),
                bg=WHITE,
                fg=LABEL_COLOR,
                font=DIGITS_FONT_STYAL,
                borderwidth=0,
                command=lambda x=digit: self.add_to_expression(x),
            )
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    # Functions of operation
    def create_operation_frame(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(
                self.buttons_frame,
                text=symbol,
                bg=OFF_WHITE,
                fg=LABEL_COLOR,
                font=DEFAULT_FONT_STYAL,
                borderwidth=0,
                command=lambda x=operator: self.append_operator(x),
            )
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    # Functions of clear button
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(
            self.buttons_frame,
            text="C",
            bg=OFF_WHITE,
            fg=LABEL_COLOR,
            font=DEFAULT_FONT_STYAL,
            borderwidth=0,
            command=self.clear,
        )
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def clear1(self):
        self.current_expression = self.current_expression[:-1]
        
        self.update_label()
        #self.update_total_label()

    def create_one_by_one_clear_button(self):
        if self.current_expression == '⌫':
            # Clear button pressed
            self.clear1()
        '''elif value == '=':
            # Evaluate the expression
            try:
                result = str(eval(self.current_expression))
                self.current_expression = result
            except Exception as e:
                self.current_expression = "Error"
        else:
            # Append the clicked button value to the current expression
            self.current_expression += value'''
        button = tk.Button(
            self.buttons_frame,
            text=" ⌫ ",
            bg=WHITE,
            fg=LABEL_COLOR,
            font=DEFAULT_FONT_STYAL,
            borderwidth=0,
            command=self.clear1,
        )
        button.grid(row=4, column=3, sticky=tk.NSEW)
        # Update the display
         #   self.display.delete(0, tk.END)
         #    self.display.insert(tk.END, self.current_expression)
    '''def one_by_one(self):
        # Clear one element at a time from the current expression
        self.current_expression = self.current_expression[:-1]
        self.update_label()

    def on_button_click(self, value):
        if value == '⌫':
            # Clear button pressed
            self.one_by_one()
        elif value == '=':
            # Evaluate the expression
            try:
                result = str(eval(self.current_expression))
                self.current_expression = result
            except Exception as e:
                self.current_expression = "Error"
        else:
            # Append the clicked button value to the current expression
            self.current_expression += value

        # Update the display
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.current_expression)

        button = tk.Button(
        self.buttons_frame,
        text='⌫',
        bg=OFF_WHITE,
        fg=LABEL_COLOR,
        font=DEFAULT_FONT_STYAL,
        borderwidth=0,
        command=self.one_by_one
    )
        button.grid(row=4, column=3, sticky=tk.NSEW)'''

    # Function of square
    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button = tk.Button(
            self.buttons_frame,
            text="x\u00b2",
            bg=OFF_WHITE,
            fg=LABEL_COLOR,
            font=DEFAULT_FONT_STYAL,
            borderwidth=0,
            command=self.square,
        )
        button.grid(row=0, column=2, sticky=tk.NSEW)

    # Function of square root
    def dot(self):
        # Check if the current expression already ends with a dot
        if not self.current_expression.endswith('.'):
            # If not, append a dot to the current expression
            self.current_expression += '.'
            self.update_label()

    def create_dot_button(self):
        button = tk.Button(
            self.buttons_frame,
            text=".",
            bg=WHITE,
            fg=LABEL_COLOR,
            font=DEFAULT_FONT_STYAL,
            borderwidth=0,
            command=self.dot,
        )
        button.grid(row=4, column=1, sticky=tk.NSEW)

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(
            self.buttons_frame,
            text="\u221ax",
            bg=OFF_WHITE,
            fg=LABEL_COLOR,
            font=DEFAULT_FONT_STYAL,
            borderwidth=0,
            command=self.sqrt,
        )
        button.grid(row=0, column=3, sticky=tk.NSEW)

    # Function for Equal button
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equal_button(self):
        button = tk.Button(
            self.buttons_frame,
            text="=",
            bg=LIGHT_BLUE,
            fg=LABEL_COLOR,
            font=DEFAULT_FONT_STYAL,
            borderwidth=0,
            command=self.evaluate,
        )
        button.grid(row=4, column=4, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    # Additional Functionality of Buttons
    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f'{symbol}')
        self.total_label.config(text=expression)
    def update_label(self):
        # Update the display
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.current_expression)
    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    cal = Calculater()
    cal.run()
