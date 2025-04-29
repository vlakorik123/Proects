import tkinter as tk
import random

# список з грами
games = [
    {"title": "Roblox", "genre": "Sandbox", "release_year": 2006, "developer": "Roblox Corporation"},
    {"title": "Minecraft", "genre": "Sandbox", "release_year": 2011, "developer": "Mojang"},
    {"title": "Terraria", "genre": "Action-adventure", "release_year": 2011, "developer": "Re-Logic"},
    {"title": "Risk of Rain 2", "genre": "Rogue-like", "release_year": 2019, "developer": "Hopoo Games"},
    {"title": "Deep Rock Galactic", "genre": "Co-op FPS", "release_year": 2020, "developer": "Ghost Ship Games"},
    {"title": "The Binding of Isaac", "genre": "Rogue-like", "release_year": 2011, "developer": "Edmund McMillen"},
    {"title": "Rust", "genre": "Survival", "release_year": 2013, "developer": "Facepunch Studios"}
]

# основне вікно
root = tk.Tk()
root.title("Окно с кнопкой")
root.geometry("400x400")

# поля для вводу інформации про ігру
title_label = tk.Label(root, text="Назва гры: ", font=("Arial", 14))
title_label.pack(pady=5)

id_label = tk.Label(root, text="ID гри: ", font=("Arial", 14))
id_label.pack(pady=5)

genre_label = tk.Label(root, text="Жанр гры: ", font=("Arial", 14))
genre_label.pack(pady=5)

release_year_label = tk.Label(root, text="Рік випуска: ", font=("Arial", 14))
release_year_label.pack(pady=5)

developer_label = tk.Label(root, text="Студія розробник: ", font=("Arial", 14))
developer_label.pack(pady=5)

# функція яка віконую дію на натискання кнопки
def on_button_click():
    # вібир рандомної гри
    game = random.choice(games)
    # айді гри
    game_id = games.index(game)
    # жанр гри
    game_genre = game["genre"]
    #реліз гри
    game_release_year = game["release_year"]
    #студія гри
    game_developer = game["developer"]
    
    # оновлє текст
    title_label.config(text=f"Назва гры: {game['title']}")
    id_label.config(text=f"ID гры: {game_id}")
    genre_label.config(text=f"Жанр гры: {game_genre}")
    release_year_label.config(text=f"Рік випуска: {game_release_year}")
    developer_label.config(text=f"Студія розробник: {game_developer}")

# кнопка яка видає гру 
button = tk.Button(root, text="Выдать игру", command=on_button_click)
button.pack(pady=20)

# запуск основного циклу
root.mainloop()
