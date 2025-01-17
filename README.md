
# Discord Bot for Book Search

This is a Discord bot that allows users to search for books by **title**, **author**, or **ISBN** using the Google Books API. The bot returns book information such as the **title**, **authors**, **published date**, and **ISBN**.

## Features

- Search for books by title
- Search for books by author
- Search for books by ISBN
- Fetches book details including title, authors, published date, and ISBN

## Requirements

- Python 3.12+
- [Discord.py](https://pypi.org/project/discord.py/) library
- [Google Books API](https://developers.google.com/books/docs/v1/getting_started)

## Setup

1. **Clone this repository** to your local machine or to Replit.
   ```
   git clone https://github.com/xcodingnani/Discord-Bot-Buddy-Read.git
   cd Discord-Bot-Buddy-Read/src
   ```

2. **Set up your environment variables** for the bot's credentials and API keys:
   - `DISCORD_BOT_TOKEN`: Your Discord bot token (you can get this from the [Discord Developer Portal](https://discord.com/developers/applications)).
   - `DISCORD_SERVER_ID`: Your Discord server's ID where the bot will be active.
   - `GOOGLE_BOOK_API_URL`: The base URL for the Google Books API (`https://www.googleapis.com/books/v1/volumes`).

   You can set these up as **environment variables** or create a `.env` file to load them.

3. **Replace any placeholder values** for secrets and credentials with actual values:
   - Update `DISCORD_BOT_TOKEN` with your Discord bot token.
   - Update `DISCORD_SERVER_ID` with your Discord server ID.
   - Update `GOOGLE_BOOK_API_URL` with the correct Google Books API URL.

4. **Run the bot**

## Commands

Once the bot is up and running, you can use the following commands in your Discord server:

- `/searchbook <title>`: Search for books by title.
- `/searchauthor <author>`: Search for books by author.
- `/searchisbn <isbn>`: Search for a book by ISBN.

## Google Books API

This bot uses the [Google Books API](https://developers.google.com/books) to fetch book details. Make sure to follow the Google Books API documentation if you need more advanced features or if you run into any issues.

## Development

This bot was primarily developed on [**Replit**](https://replit.com/) (an online development environment) and should work across other platforms as long as the necessary dependencies are installed and the correct environment variables are set.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
