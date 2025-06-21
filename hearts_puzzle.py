#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Игра Пятнашки с Сердечками
Классическая игра пятнашки, но вместо цифр используются сердечки разных цветов
"""

import tkinter as tk
from tkinter import messagebox
import random

class HeartsPuzzleGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Пятнашки с Сердечками 💖")
        self.root.geometry("500x600")
        self.root.configure(bg='#FFE4E1')
        self.root.resizable(False, False)
        
        # Размер игрового поля 4x4
        self.size = 4
        self.tile_size = 100
        
        # Цвета сердечек (15 разных цветов + пустая клетка)
        self.heart_colors = [
            '#FF1493',  # Розовый
            '#FF69B4',  # Горячий розовый
            '#FFB6C1',  # Светло-розовый
            '#FFC0CB',  # Розовый
            '#DC143C',  # Малиновый
            '#B22222',  # Огненно-красный
            '#CD5C5C',  # Индийский красный
            '#F08080',  # Светло-коралловый
            '#FA8072',  # Лососевый
            '#E9967A',  # Темно-лососевый
            '#FFA07A',  # Светло-лососевый
            '#FF7F50',  # Коралловый
            '#FF6347',  # Томатный
            '#FF4500',  # Оранжево-красный
            '#FF8C00',  # Темно-оранжевый
        ]
        
        # Инициализация игрового поля
        self.board = list(range(1, 16)) + [0]  # 1-15 и пустая клетка (0)
        self.solution = self.board.copy()
        
        # Перемешиваем поле
        self.shuffle_board()
        
        # Создаем интерфейс
        self.create_widgets()
        
    def create_widgets(self):
        """Создание интерфейса игры"""
        # Заголовок
        title_label = tk.Label(
            self.root, 
            text="💝 Пятнашки с Сердечками 💝", 
            font=("Arial", 18, "bold"),
            bg='#FFE4E1',
            fg='#8B0000'
        )
        title_label.pack(pady=10)
        
        # Счетчик ходов
        self.moves_label = tk.Label(
            self.root,
            text="Ходов: 0",
            font=("Arial", 14),
            bg='#FFE4E1',
            fg='#8B0000'
        )
        self.moves_label.pack(pady=5)
        self.moves_count = 0
        
        # Игровое поле
        self.game_frame = tk.Frame(self.root, bg='#FFE4E1')
        self.game_frame.pack(pady=20)
        
        # Создаем кнопки для каждой клетки
        self.buttons = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                btn = tk.Button(
                    self.game_frame,
                    width=6,
                    height=3,
                    font=("Arial", 20, "bold"),
                    command=lambda r=i, c=j: self.move_tile(r, c),
                    relief="raised",
                    bd=3
                )
                btn.grid(row=i, column=j, padx=2, pady=2)
                row.append(btn)
            self.buttons.append(row)
        
        # Кнопки управления
        control_frame = tk.Frame(self.root, bg='#FFE4E1')
        control_frame.pack(pady=20)
        
        new_game_btn = tk.Button(
            control_frame,
            text="🔄 Новая игра",
            font=("Arial", 12, "bold"),
            command=self.new_game,
            bg='#FF69B4',
            fg='white',
            relief="raised",
            bd=3,
            padx=20
        )
        new_game_btn.pack(side=tk.LEFT, padx=10)
        
        solve_btn = tk.Button(
            control_frame,
            text="💡 Подсказка",
            font=("Arial", 12, "bold"),
            command=self.show_hint,
            bg='#FFA07A',
            fg='white',
            relief="raised",
            bd=3,
            padx=20
        )
        solve_btn.pack(side=tk.LEFT, padx=10)
        
        # Обновляем отображение
        self.update_display()
        
    def shuffle_board(self):
        """Перемешивание игрового поля"""
        # Убеждаемся, что есть решение
        while True:
            random.shuffle(self.board)
            if self.is_solvable():
                break
                
    def is_solvable(self):
        """Проверка, можно ли решить головоломку"""
        inversions = 0
        flat_board = [x for x in self.board if x != 0]
        
        for i in range(len(flat_board)):
            for j in range(i + 1, len(flat_board)):
                if flat_board[i] > flat_board[j]:
                    inversions += 1
        
        # Для 4x4 поля: если пустая клетка на четной строке снизу,
        # количество инверсий должно быть нечетным
        empty_row = self.board.index(0) // self.size
        if (self.size - empty_row) % 2 == 0:
            return inversions % 2 == 1
        else:
            return inversions % 2 == 0
            
    def update_display(self):
        """Обновление отображения игрового поля"""
        for i in range(self.size):
            for j in range(self.size):
                index = i * self.size + j
                value = self.board[index]
                
                if value == 0:
                    # Пустая клетка
                    self.buttons[i][j].config(
                        text="",
                        bg='#F0F0F0',
                        state='disabled',
                        relief="sunken"
                    )
                else:
                    # Клетка с сердечком
                    color = self.heart_colors[value - 1]
                    self.buttons[i][j].config(
                        text="💖",
                        bg=color,
                        fg='white',
                        state='normal',
                        relief="raised",
                        activebackground=color,
                        disabledforeground='white'
                    )
                    
    def move_tile(self, row, col):
        """Перемещение плитки"""
        index = row * self.size + col
        value = self.board[index]
        
        if value == 0:  # Нельзя двигать пустую клетку
            return
            
        # Ищем пустую клетку
        empty_index = self.board.index(0)
        empty_row = empty_index // self.size
        empty_col = empty_index % self.size
        
        # Проверяем, можно ли сделать ход
        if (abs(row - empty_row) == 1 and col == empty_col) or \
           (abs(col - empty_col) == 1 and row == empty_row):
            # Меняем местами
            self.board[index], self.board[empty_index] = self.board[empty_index], self.board[index]
            
            # Увеличиваем счетчик ходов
            self.moves_count += 1
            self.moves_label.config(text=f"Ходов: {self.moves_count}")
            
            # Обновляем отображение
            self.update_display()
            
            # Проверяем победу
            if self.check_win():
                self.show_win_message()
                
    def check_win(self):
        """Проверка победы"""
        return self.board == self.solution
        
    def show_win_message(self):
        """Показ сообщения о победе"""
        messagebox.showinfo(
            "Поздравляем! 🎉",
            f"Вы решили головоломку за {self.moves_count} ходов!\n\n"
            "Все сердечки на своих местах! 💖💖💖"
        )
        
    def new_game(self):
        """Начать новую игру"""
        self.board = list(range(1, 16)) + [0]
        self.shuffle_board()
        self.moves_count = 0
        self.moves_label.config(text="Ходов: 0")
        self.update_display()
        
    def show_hint(self):
        """Показ подсказки"""
        # Ищем первую неправильно размещенную плитку
        for i, value in enumerate(self.board):
            if value != 0 and value != self.solution[i]:
                correct_pos = value - 1
                correct_row = correct_pos // self.size
                correct_col = correct_pos % self.size
                current_row = i // self.size
                current_col = i % self.size
                
                messagebox.showinfo(
                    "💡 Подсказка",
                    f"Сердечко {value} (💖) сейчас в позиции ({current_row + 1}, {current_col + 1}),\n"
                    f"а должно быть в позиции ({correct_row + 1}, {correct_col + 1})"
                )
                return
                
        messagebox.showinfo("💡 Подсказка", "Все сердечки уже на правильных местах! 🎉")
        
    def run(self):
        """Запуск игры"""
        self.root.mainloop()

def main():
    """Главная функция"""
    print("🎮 Запуск игры 'Пятнашки с Сердечками'...")
    print("📝 Правила:")
    print("   - Нажимайте на сердечки рядом с пустой клеткой")
    print("   - Цель: расставить все сердечки по порядку")
    print("   - Используйте кнопки для новой игры и подсказок")
    print("💖 Удачи!\n")
    
    game = HeartsPuzzleGame()
    game.run()

if __name__ == "__main__":
    main()