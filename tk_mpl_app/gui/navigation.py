from tkinter import ttk


def make_navigation_buttons(root, buttons_info):
    top_frame = ttk.Frame(root, padding=5)
    top_frame.pack(side="top", fill="x")

    buttons = {}
    for info in buttons_info:
        btn = ttk.Button(top_frame, text=info['text'], command=info['command'])
        btn.pack(side=info.get('side', 'left'), padx=5)
        buttons[info['text']] = btn

    return buttons