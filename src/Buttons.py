from InitialValues import *

New_Game = {
    "left": Margin,
    "top": Height
    - Margin
    - Button_Border * 4
    - Button_Height * 2
    - Vertical_Space_Between_Buttons,
    "width": Button_Width,
    "height": Button_Height,
    "border": Button_Border,
    "color_inactive": "#7678ed",
    "color_active": "#3d348b",
    "border_color": background_color,
    "text": "New Game",
    "text_color_inactive": "#000000",
    "text_color_active": "#ffffff",
    "font": "../resources/FORTE.ttf",
    "font_size": 30,
}

Restart_Game = {
    "left": Margin,
    "top": Height - Margin - Button_Border * 2 - Button_Height,
    "width": Button_Width,
    "height": Button_Height,
    "border": Button_Border,
    "color_inactive": "#ff4d6d",
    "color_active": "#800f2f",
    "border_color": background_color,
    "text": "Restart",
    "text_color_inactive": "#000000",
    "text_color_active": "#ffffff",
    "font": "../resources/FORTE.ttf",
    "font_size": 30,
}

Hint = {
    "left": Margin
    + Button_Border * 2
    + Button_Width
    + Horizontal_Space_Between_Buttons,
    "top": Height
    - Margin
    - Button_Border * 4
    - Button_Height * 2
    - Vertical_Space_Between_Buttons,
    "width": Button_Width,
    "height": Button_Height,
    "border": Button_Border,
    "color_inactive": "#06d6a0",
    "color_active": "#2c6e49",
    "border_color": background_color,
    "text": "Hint",
    "text_color_inactive": "#000000",
    "text_color_active": "#ffffff",
    "font": "../resources/FORTE.ttf",
    "font_size": 30,
}

Screen_Shot = {
    "left": Margin
    + Button_Border * 2
    + Button_Width
    + Horizontal_Space_Between_Buttons,
    "top": Height - Margin - Button_Border * 2 - Button_Height,
    "width": Button_Width,
    "height": Button_Height,
    "border": Button_Border,
    "color_inactive": "#ffb700",
    "color_active": "#eb5e28",
    "border_color": background_color,
    "text": "Screen Shot",
    "text_color_inactive": "#000000",
    "text_color_active": "#ffffff",
    "font": "../resources/FORTE.ttf",
    "font_size": 30,
}

Time_Elapsed = {
    "left":  Margin,
    "top": Height
    - Margin
    - Button_Border * 6
    - Button_Height * 3
    - Vertical_Space_Between_Buttons * 2,
    "width": 2 * Button_Width + Horizontal_Space_Between_Buttons,
    "height": Button_Height,
    "border": Button_Border,
    "color_inactive": "#6c757d",
    "color_active": "#",
    "border_color": background_color,
    "text": "",
    "text_color_inactive": "#fefee3",
    "text_color_active": "#",
    "font": "../resources/FORTE.ttf",
    "font_size": 30,
}

Remaining_Hints = {
    "left": Width - Margin - 4 * Button_Border - 2*Button_Width - Horizontal_Space_Between_Buttons,
    "top": Height
    - Margin
    - Button_Border * 6
    - Button_Height * 3
    - Vertical_Space_Between_Buttons * 2,
    "width": 2 * Button_Width + Horizontal_Space_Between_Buttons,
    "height": Button_Height,
    "border": Button_Border,
    "color_inactive": "#adc178",
    "color_active": "#",
    "border_color": background_color,
    "text": f"Remaining Hints: {Remaining_Hints_Num}",
    "text_color_inactive": "#003566",
    "text_color_active": "#",
    "font": "../resources/FORTE.ttf",
    "font_size": 30,
}

Errors_Happened = {
    "left": Width
    - Margin
    - 4 * Button_Border
    - 2 * Button_Width
    - Horizontal_Space_Between_Buttons,
    "top": Height
    - Margin
    - Button_Border * 4
    - Button_Height * 2
    - Vertical_Space_Between_Buttons * 1,
    "width": 2 * Button_Width + Horizontal_Space_Between_Buttons,
    "height": Button_Height,
    "border": Button_Border,
    "color_inactive": "#bbd0ff",
    "color_active": "#",
    "border_color": background_color,
    "text": f"Remaining Hints: {Remaining_Hints_Num}",
    "text_color_inactive": RED,
    "text_color_active": "#",
    "font": "../resources/FORTE.ttf",
    "font_size": 30,
}

Mute = {
    "left": Width
    - Margin
    - 4 * Button_Border
    - 2 * Button_Width
    - Horizontal_Space_Between_Buttons,
    "top": Height - Margin - Button_Border * 2 - Button_Height * 1,
    "width": 2 * Button_Width + Horizontal_Space_Between_Buttons,
    "height": Button_Height,
    "border": Button_Border,
    "color_inactive": "#bbd0ff",
    "color_active": "#",
    "border_color": background_color,
    "text": "Unmuted",
    "text_color_inactive": "#003566",
    "text_color_active": "#",
    "font": "../resources/FORTE.ttf",
    "font_size": 30,
}
