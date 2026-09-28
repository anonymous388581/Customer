<p align="center">
  <img src="https://github.com/NBBotz/Images/blob/main/Lucia.jpg">
</p>

<h1 align="center">Lucia Filter Bot</h1>

<p align="center">
  <a href="https://t.me/SilentXBotz_Support">
    <img src="https://img.shields.io/badge/Join-Support%20Group-blue?style=for-the-badge&logo=telegram">
  </a>
  <a href="http://t.me/Lucia_Filter_Bot">
    <img src="https://img.shields.io/badge/Demo%20Bot-Click%20Here-green?style=for-the-badge&logo=telegram">
  </a>
</p>

---

## Features  

- ✅ Supports Double Databases (Auto-Switch When Primary DB Is Running Low.)  
- 🔍 Fast And Efficient File Searching With Pagination  
- 📂 Saves And Retrieves Files.  
- 🚀 Optimized For Performance And Low Resource Usage  
- 🛡️ 3 Verification Method 
- 🤖 Custom Force Subscription For Group Owners
- 📊 Full Customisable. 
- 🔄 Latest Features.
- 📺 Best Streaming Site.
- 📥 Top Trending & Refer Feature.
- 👑 Premium Subscription Funtion.
- 📌 Premium Expired Reminder.
- 🔥 Telegram Star Payment Method

# New Version Released - V4.2
- Now Group Owners Change There All Settings From Callback Button ✅
- Group Owners Can Manage Groups From Bot PM.
- Added /reload Command 
- UI Change
- New Channel Update Theme
- Added Support Of Streming Only For Premium Users
- Now Owner Can Reset All Connect Groups Settings 


## Configuration

Set these required environment variables in your deployment platform:

| Variable | Purpose |
| --- | --- |
| `BOT_TOKEN` | Telegram bot token from BotFather |
| `API_ID` | Telegram API ID from [my.telegram.org](https://my.telegram.org/apps) |
| `API_HASH` | Telegram API hash from [my.telegram.org](https://my.telegram.org/apps) |
| `DATABASE_URI` | MongoDB connection URI |

Optional variables include `DATABASE_NAME` (defaults to `Cluster0`), `COLLECTION_NAME` (defaults to `SilentXBotz_files`), and `MULTIPLE_DB` (defaults to `False`). Set `DATABASE_URI2` only when `MULTIPLE_DB=True`. Configure `ADMINS`, `CHANNELS`, `LOG_CHANNEL`, `BIN_CHANNEL`, `MOVIE_UPDATE_CHANNEL`, `INDEX_REQ_CHANNEL`, and `AUTH_CHANNEL` for your Telegram setup. `INDEX_REQ_CHANNEL` defaults to the existing configured channel. `FQDN` may be set to the public hostname, with or without `https://`.

`SHORTENER_API`, `SHORTENER_API2`, and `SHORTENER_API3` are optional credentials for their corresponding shortener services. Their values, like all Telegram and MongoDB credentials, must be supplied through environment variables and must not be committed. Optional boolean settings accept `true`/`false`, `1`/`0`, `yes`/`no`, or `on`/`off`.

### Render Web Service

Use one service and one bot process:

- Service type: **Web Service**
- Runtime: **Docker**, using the repository `Dockerfile`
- Build: Dockerfile installs requirements with `pip install --no-cache-dir -r requirements.txt`
- Start command: `python3 bot.py` (also the Dockerfile command)
- Port: Render supplies `PORT`; the server binds to `0.0.0.0:$PORT`. Do not hardcode a public IP or port.
- Health check path: `/health` (returns `OK` without Telegram authentication)

Set the four required variables above in Render's Environment settings. Set `FQDN` to the service's public hostname if another feature needs the public URL; HTTPS is normalized automatically. Do not configure a second worker running `bot.py` alongside the Web Service.

For a native Python Render runtime instead of Docker, use build command `pip install -r requirements.txt` and start command `python3 bot.py`.

## 🚀 Deployment Methods

Choose A Deployment Method Below And Get Your Bot Running Instantly!  

<details>
  <summary><b>Heroku</b></summary>  

Click The Button Below To Instantly Deploy Your Bot On **Heroku**.  

<p align="center">
  <a href="https://heroku.com/deploy?template=https://github.com/NBBotz/Auto_Filter_Bot">
    <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy on Heroku">
  </a>
</p>

</details>

<details>
  <summary><b>Koyeb</b></summary>  

Deploy On **Koyeb** In One Click!  

<p align="center">
  <a href="https://app.koyeb.com/deploy?type=git&repository=https://github.com/NBBotz/Auto_Filter_Bot&branch=SilentXBotz &name=LuciaFilterBot">
    <img src="https://www.koyeb.com/static/images/deploy/button.svg" alt="Deploy to Koyeb">
  </a>
</p>


</details>

<details>
  <summary><b>VPS</b></summary>  

Run The Following Commands To Deploy The Bot On A **VPS**:  

```bash
mkdir SilentXBotz && cd SilentXBotz
git clone https://github.com/NBBotz/Auto_Filter_Bot
cd Auto_Filter_Bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 bot.py
```
</details>


# ! Errors 
- This Repository May Contain Some Errors. If You Encounter Any Issues, Please Let Us Know, And We Will Do Our Best To Resolve Them.
<p align="center">
  <a href="https://t.me/SilentXBotz_Support">
    <img src="https://img.shields.io/badge/Report-Error-red?style=for-the-badge&logo=telegram" alt="Report Error">
  </a>
</p>
  

# 📌 Credits  

- **Base Repository:** [ᴅʀᴇᴀᴍxʙᴏᴛᴢ](https://github.com/DreamXBotz/Auto_Filter_Bot.git)
- **Thank You To All [Contributors](https://github.com/NBBotz/Auto_Filter_Bot/graphs/contributors) For Your Valuable Contributions To This Repository!**


# Bugs & Fixes  

**If You Find Any Bugs Or Errors In This Project, Feel Free To Fix Them And Submit A Pull Request. Contributions Are Always Welcome!**  

## Disclaimer

This Repository Is Provided For Educational Purposes Only. It Is Not Intended For Personal Or Commercial Gain. Use Of This Repository And The Code Within Is At Your Own Risk. The Authors And Contributors Are Not Responsible For Any Misuse Or Damage Caused By The Use Of This Project.

## License

This Project Is Licensed Under The [GNU General Public License v3.0](https://github.com/NBBotz/Auto_Filter_Bot/blob/SilentXBotz/LICENSE)

