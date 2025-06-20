**Discord Twitter Link Scraper**

A simple, configurable Python script that leverages the Discord API (via Discum) to fetch members of a channel with specified roles and extract their linked Twitter (X) profiles. Save your results automatically to a file for further processing or analysis.

---

## 🚀 Features

- **Role-based filtering**: Only users with specified Discord roles are processed.
- **Configurable cooldown**: Control request rate to avoid hitting rate limits.
- **Background saving**: URLs are saved incrementally in a background thread.
- **Minimal dependencies**: Built on top of [Discum](https://github.com/Merubokkusu/Discum).

---

## 📋 Prerequisites

- Python 3.8+
- A valid Discord user token (not a bot token).
- Access to the target server and channel.

---

## 🔧 Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/TishkaPon/FindTwwiterUrlDiscord.git
   cd FindTwwiterUrlDiscord
   ```

2. **Install dependencies**

   ```bash
   pip install discum
   ```

3. **Project structure**

   ```
   .
   ├── config.py       # Configuration file (token, IDs, roles, cooldown)
   ├── main.py         # Entry point
   ├── utils.py        # Helper functions (role fetching, URL saving)
   └── requirements.txt
   ```

---

## ⚙️ Configuration

Rename or edit `config.py` with your settings:

```python
# config.py
TOKEN = "YOUR_DISCORD_TOKEN"        # Find in network requests or cookies
GUILD_ID = "123456789012345678"     # Server (guild) ID
CHANNEL_ID = "987654321098765432"   # Channel ID to fetch members from

# Roles to include (by name). Only users with these roles will be parsed.
ROLES = ["Member", "VIP", "Subscriber"]

# Delay between profile requests (in seconds)
TIMEOUT_ACCOUNT = 2.0
```

> **Tip:** To get IDs, enable Developer Mode in Discord, then right-click on server or channel and select *Copy ID*.

---

## 🏃‍♂️ Usage

Run the scraper:

```bash
python main.py
```

Sample output:

```
Вход в Дискорд аккаунт успешно выполнен!
Получаем пользователей канала...
['1111111111', '2222222222']   # Roles mapped to IDs
Пользователи успешно найдены (42 шт.)
0/42 (0 ссылок)
15/42 (10 ссылок)
...
42/42 (28 ссылок)
Process complete. Links saved to `twitter_urls.txt`.
```

Collected URLs will be appended to `twitter_urls.txt` by default.

---

## 📂 Output

- **twitter\_urls.txt**: A list of `https://x.com/username` entries, one per line.

---

## 🤝 Contributing

Feel free to open issues or submit pull requests for bug fixes, new features, or improvements!

1. Fork the repository
2. Create a new branch (`git checkout -b feature/add-xyz`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push to the branch (`git push origin feature/add-xyz`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> *Happy scraping!*

