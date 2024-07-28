import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Change if you have a different username
        password="password",  # Add your MySQL root password if you have set one
        database="movie_marketing"
    )

def fetch_movies():
    for row in tree.get_children():
        tree.delete(row)
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """SELECT Movie.MovieID, Movie.Title, Movie.Director, Movie.Price, Genre.Name
               FROM Movie
               JOIN Genre ON Movie.GenreID = Genre.GenreID"""
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    conn.close()

def fetch_genres():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Genre")
    genres = cursor.fetchall()
    conn.close()
    return genres

def add_movie_window():
    def add_movie():
        title = title_entry.get()
        director = director_entry.get()
        price = price_entry.get()
        genre_name = genre_combobox.get()
        
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT GenreID FROM Genre WHERE Name = %s", (genre_name,))
        genre_id = cursor.fetchone()[0]
        
        cursor.execute("INSERT INTO Movie (Title, Director, Price, GenreID) VALUES (%s, %s, %s, %s)", 
                       (title, director, price, genre_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Movie added successfully")
        add_movie_win.destroy()

    add_movie_win = tk.Toplevel(root)
    add_movie_win.title("Add Movie")
    add_movie_win.geometry("400x300")

    ttk.Label(add_movie_win, text="Title:").grid(row=0, column=0, padx=10, pady=10)
    title_entry = ttk.Entry(add_movie_win)
    title_entry.grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(add_movie_win, text="Director:").grid(row=1, column=0, padx=10, pady=10)
    director_entry = ttk.Entry(add_movie_win)
    director_entry.grid(row=1, column=1, padx=10, pady=10)

    ttk.Label(add_movie_win, text="Price:").grid(row=2, column=0, padx=10, pady=10)
    price_entry = ttk.Entry(add_movie_win)
    price_entry.grid(row=2, column=1, padx=10, pady=10)

    ttk.Label(add_movie_win, text="Genre:").grid(row=3, column=0, padx=10, pady=10)
    genres = fetch_genres()
    genre_combobox = ttk.Combobox(add_movie_win, values=[genre[1] for genre in genres])
    genre_combobox.grid(row=3, column=1, padx=10, pady=10)

    add_button = ttk.Button(add_movie_win, text="Add Movie", command=add_movie)
    add_button.grid(row=4, columnspan=2, pady=20)

def add_customer_window():
    def add_customer():
        name = name_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Customer (Name, Email, Address) VALUES (%s, %s, %s)", (name, email, address))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Customer added successfully")
        add_customer_win.destroy()

    add_customer_win = tk.Toplevel(root)
    add_customer_win.title("Add Customer")
    add_customer_win.geometry("400x300")

    ttk.Label(add_customer_win, text="Name:").grid(row=0, column=0, padx=10, pady=10)
    name_entry = ttk.Entry(add_customer_win)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(add_customer_win, text="Email:").grid(row=1, column=0, padx=10, pady=10)
    email_entry = ttk.Entry(add_customer_win)
    email_entry.grid(row=1, column=1, padx=10, pady=10)

    ttk.Label(add_customer_win, text="Address:").grid(row=2, column=0, padx=10, pady=10)
    address_entry = ttk.Entry(add_customer_win)
    address_entry.grid(row=2, column=1, padx=10, pady=10)

    add_button = ttk.Button(add_customer_win, text="Add Customer", command=add_customer)
    add_button.grid(row=3, columnspan=2, pady=20)

def add_genre_window():
    def add_genre():
        name = genre_name_entry.get()
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Genre (Name) VALUES (%s)", (name,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Genre added successfully")
        add_genre_win.destroy()

    add_genre_win = tk.Toplevel(root)
    add_genre_win.title("Add Genre")
    add_genre_win.geometry("400x200")

    ttk.Label(add_genre_win, text="Genre Name:").grid(row=0, column=0, padx=10, pady=10)
    genre_name_entry = ttk.Entry(add_genre_win)
    genre_name_entry.grid(row=0, column=1, padx=10, pady=10)

    add_button = ttk.Button(add_genre_win, text="Add Genre", command=add_genre)
    add_button.grid(row=1, columnspan=2, pady=20)

def buy_movie_window():
    def buy_movie():
        customer_id = customer_id_entry.get()
        movie_id = movie_id_entry.get()
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO CanBuy (CustomerID, MovieID) VALUES (%s, %s)", (customer_id, movie_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Movie purchased successfully")
        buy_movie_win.destroy()

    buy_movie_win = tk.Toplevel(root)
    buy_movie_win.title("Buy Movie")
    buy_movie_win.geometry("400x200")

    ttk.Label(buy_movie_win, text="Customer ID:").grid(row=0, column=0, padx=10, pady=10)
    customer_id_entry = ttk.Entry(buy_movie_win)
    customer_id_entry.grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(buy_movie_win, text="Movie ID:").grid(row=1, column=0, padx=10, pady=10)
    movie_id_entry = ttk.Entry(buy_movie_win)
    movie_id_entry.grid(row=1, column=1, padx=10, pady=10)

    buy_button = ttk.Button(buy_movie_win, text="Buy Movie", command=buy_movie)
    buy_button.grid(row=2, columnspan=2, pady=20)

def categorize_movie_window():
    def categorize_movie():
        genre_id = genre_id_entry.get()
        movie_id = movie_id_entry.get()
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Has (GenreID, MovieID) VALUES (%s, %s)", (genre_id, movie_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Movie categorized successfully")
        categorize_movie_win.destroy()

    categorize_movie_win = tk.Toplevel(root)
    categorize_movie_win.title("Categorize Movie")
    categorize_movie_win.geometry("400x200")

    ttk.Label(categorize_movie_win, text="Genre ID:").grid(row=0, column=0, padx=10, pady=10)
    genre_id_entry = ttk.Entry(categorize_movie_win)
    genre_id_entry.grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(categorize_movie_win, text="Movie ID:").grid(row=1, column=0, padx=10, pady=10)
    movie_id_entry = ttk.Entry(categorize_movie_win)
    movie_id_entry.grid(row=1, column=1, padx=10, pady=10)

    categorize_button = ttk.Button(categorize_movie_win, text="Categorize Movie", command=categorize_movie)
    categorize_button.grid(row=2, columnspan=2, pady=20)

def filter_movies_by_genre():
    selected_genre = genre_combobox.get()
    for row in tree.get_children():
        tree.delete(row)
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """SELECT Movie.MovieID, Movie.Title, Movie.Director, Movie.Price, Genre.Name
               FROM Movie
               JOIN Genre ON Movie.GenreID = Genre.GenreID
               WHERE Genre.Name = %s"""
    cursor.execute(query, (selected_genre,))
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    conn.close()

def view_user_purchases_window():
    def view_purchases():
        user_id = user_id_entry.get()
        for row in purchase_tree.get_children():
            purchase_tree.delete(row)
        conn = connect_to_db()
        cursor = conn.cursor()
        query = """SELECT Customer.Name, Movie.MovieID, Movie.Title, Movie.Director, Movie.Price, Genre.Name
                   FROM Movie
                   JOIN CanBuy ON Movie.MovieID = CanBuy.MovieID
                   JOIN Customer ON CanBuy.CustomerID = Customer.CustomerID
                   JOIN Genre ON Movie.GenreID = Genre.GenreID
                   WHERE CanBuy.CustomerID = %s"""
        cursor.execute(query, (user_id,))
        rows = cursor.fetchall()
        for row in rows:
            purchase_tree.insert("", tk.END, values=row)
        conn.close()

    view_purchases_win = tk.Toplevel(root)
    view_purchases_win.title("View User Purchases")
    view_purchases_win.geometry("600x400")

    ttk.Label(view_purchases_win, text="User ID:").grid(row=0, column=0, padx=10, pady=10)
    user_id_entry = ttk.Entry(view_purchases_win)
    user_id_entry.grid(row=0, column=1, padx=10, pady=10)

    view_button = ttk.Button(view_purchases_win, text="View Purchases", command=view_purchases)
    view_button.grid(row=1, columnspan=2, pady=20)

    purchase_tree = ttk.Treeview(view_purchases_win, columns=("CustomerName", "MovieID", "Title", "Director", "Price", "Genre"), show='headings')
    purchase_tree.heading("CustomerName", text="Customer Name")
    purchase_tree.heading("MovieID", text="MovieID")
    purchase_tree.heading("Title", text="Title")
    purchase_tree.heading("Director", text="Director")
    purchase_tree.heading("Price", text="Price")
    purchase_tree.heading("Genre", text="Genre")
    purchase_tree.grid(row=2, columnspan=2, padx=10, pady=10, sticky="nsew")

    view_purchases_win.grid_rowconfigure(2, weight=1)
    view_purchases_win.grid_columnconfigure(1, weight=1)

def main():
    global root
    root = tk.Tk()
    root.title("Movie Marketing Application")
    root.geometry("800x700")

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12))
    style.configure("TLabel", font=("Helvetica", 12))
    style.configure("TEntry", font=("Helvetica", 12))
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
    style.configure("Treeview", font=("Helvetica", 10))

    # Movie Table
    global tree
    tree_frame = ttk.Frame(root)
    tree_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    tree_scroll = ttk.Scrollbar(tree_frame)
    tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    tree = ttk.Treeview(tree_frame, columns=("MovieID", "Title", "Director", "Price", "Genre"), show='headings', yscrollcommand=tree_scroll.set)
    tree.heading("MovieID", text="MovieID")
    tree.heading("Title", text="Title")
    tree.heading("Director", text="Director")
    tree.heading("Price", text="Price")
    tree.heading("Genre", text="Genre")
    tree.pack(fill=tk.BOTH, expand=True)

    tree_scroll.config(command=tree.yview)

    fetch_button = ttk.Button(root, text="Fetch Movies", command=fetch_movies)
    fetch_button.pack(pady=10)

    # Filter Movies by Genre
    filter_frame = ttk.Frame(root)
    filter_frame.pack(fill="x", padx=20, pady=10)

    ttk.Label(filter_frame, text="Filter by Genre:").pack(side=tk.LEFT, padx=10)
    genres = fetch_genres()
    global genre_combobox
    genre_combobox = ttk.Combobox(filter_frame, values=[genre[1] for genre in genres])
    genre_combobox.pack(side=tk.LEFT, padx=10)
    filter_button = ttk.Button(filter_frame, text="Filter", command=filter_movies_by_genre)
    filter_button.pack(side=tk.LEFT, padx=10)

    # Buttons to open new windows
    button_frame = ttk.Frame(root)
    button_frame.pack(fill="x", padx=20, pady=10)

    add_movie_button = ttk.Button(button_frame, text="Add Movie", command=add_movie_window)
    add_movie_button.grid(row=0, column=0, padx=10, pady=10)

    add_customer_button = ttk.Button(button_frame, text="Add Customer", command=add_customer_window)
    add_customer_button.grid(row=0, column=1, padx=10, pady=10)

    add_genre_button = ttk.Button(button_frame, text="Add Genre", command=add_genre_window)
    add_genre_button.grid(row=0, column=2, padx=10, pady=10)

    buy_movie_button = ttk.Button(button_frame, text="Buy Movie", command=buy_movie_window)
    buy_movie_button.grid(row=0, column=3, padx=10, pady=10)

    categorize_movie_button = ttk.Button(button_frame, text="Categorize Movie", command=categorize_movie_window)
    categorize_movie_button.grid(row=0, column=4, padx=10, pady=10)

    view_purchases_button = ttk.Button(button_frame, text="View User Purchases", command=view_user_purchases_window)
    view_purchases_button.grid(row=0, column=5, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
