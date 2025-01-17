import os
import requests
import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=';', intents=intents)

GUILD_ID = discord.Object(id=os.environ['DISCORD_SERVER_ID'])

def search_books(query, search_type="title"):
    """
    Searches for books using the Google Books API by title, author, or ISBN.

    Args:
        query (str): Search term (e.g., title, author, or ISBN).
        search_type (str): "title" for title search, "author" for author search, or "isbn" for ISBN search.

    Returns:
        list: A list of found books with basic information.
    """

    base_url = os.environ['GOOGLE_BOOK_API_URL']
    if search_type == "title":
        params = {"q": f"intitle:{query}"}
    elif search_type == "author":
        params = {"q": f"inauthor:{query}"}
    elif search_type == "isbn":
        params = {"q": f"isbn:{query}"}
    else:
        return []

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        books = []
        for item in data.get("items", []):
            volume_info = item.get("volumeInfo", {})

            isbn = None
            identifiers = volume_info.get("industryIdentifiers", [])
            for identifier in identifiers:
                if identifier["type"] == "ISBN_13":
                    isbn = identifier["identifier"]
                    break
                elif identifier["type"] == "ISBN_10" and not isbn:
                    isbn = identifier["identifier"]

            books.append({
                "title":
                volume_info.get("title", "Not available"),
                "authors":
                volume_info.get("authors", ["Not available"]),
                "publishedDate":
                volume_info.get("publishedDate", "Not available"),
                "isbn":
                isbn if isbn else "Not available"
            })
        return books
    else:
        return []

@bot.event
async def on_ready():
    try:
        guild = discord.Object(id=int(os.environ['DISCORD_SERVER_ID']))
        await bot.tree.sync(guild=guild)
        print(f"Bot is ready. Logged in as {bot.user}")
    except Exception as e:
        print(f"Error synchronizing commands: {e}")

@bot.tree.command(name="searchbook",
                  description="Search for books by title",
                  guild=GUILD_ID)
async def search_book(interaction: discord.Interaction, title: str):
    books = search_books(title, search_type="title")
    if books:
        response = "\n\n".join([
            f"**Title:** {book['title']}\n**Authors:** {', '.join(book['authors'])}\n**Published Date:** {book['publishedDate']}\n**ISBN:** {book['isbn']}"
            for book in books[:5]
        ])
    else:
        response = "No books found."
    await interaction.response.send_message(response)

@bot.tree.command(name="searchauthor",
                  description="Search for books by author",
                  guild=GUILD_ID)
async def search_author(interaction: discord.Interaction, author: str):
    books = search_books(author, search_type="author")
    if books:
        response = "\n\n".join([
            f"**Title:** {book['title']}\n**Authors:** {', '.join(book['authors'])}\n**Published Date:** {book['publishedDate']}\n**ISBN:** {book['isbn']}"
            for book in books[:5]
        ])
    else:
        response = "No books found."
    await interaction.response.send_message(response)

@bot.tree.command(name="searchisbn",
                  description="Search for a book by ISBN",
                  guild=GUILD_ID)
async def search_isbn(interaction: discord.Interaction, isbn: str):
    books = search_books(isbn, search_type="isbn")
    if books:
        book = books[0]
        response = (
            f"**Title:** {book['title']}\n**Authors:** {', '.join(book['authors'])}\n"
            f"**Published Date:** {book['publishedDate']}\n**ISBN:** {book['isbn']}"
        )
    else:
        response = "No book found."
    await interaction.response.send_message(response)

bot.run(os.environ['DISCORD_BOT_TOKEN'])