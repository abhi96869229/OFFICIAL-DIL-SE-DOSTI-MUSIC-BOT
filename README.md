<p align="center">

[![Dil-se-Dosti](https://telegra.ph/file/5c38e2df8dd48b7c89067.jpg)](https://t.me/XD-Deepak)


<h1 align="center">
  <b>🇳🇪 Official-Dil-se-Dosti-music-bot🇳🇪</b>
</h1>


<details><summary> <h1 align="center">⚡DEPLOY⚡</h1> </summary>

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/XD-Deepak/OFFICIAL-DIL-SE-DOSTI-MUSIC-BOT)

</details>

<details><summary> <h1 align="center">string_session</h1> </summary>

Generate From here

 [![GenerateStringName](https://img.shields.io/badge/repl.it-generateStringName-yellowgreen)](https://replit.com/@XDDeepak/DilseDosti?v=1)

</details>

<details><summary> <h1 align="center">license</h1> </summary>

(C) @XD-Deepak
Copyright permission under MIT License
License -> https://github.com/XD-Deepak/OFFICIAL-DIL-SE-DOSTI-MUSIC-BOT/blob/master/LICENSE

NOTE: Make sure you have started a VoiceChat in your Group before deploying.
</details>
<details><summary> <h1 align="center">VARS</h1> </summary>

1. `API_ID` : Get From my.telegram.org
2. `API_HASH` : Get from my.telegram.org
3. `BOT_TOKEN` : @Botfather
4. `SESSION_STRING` : Generate From here [![GenerateStringName](https://img.shields.io/badge/repl.it-generateStringName-yellowgreen)](https://replit.com/@XDDeepak/DilseDosti?v=1)
5. `CHAT` : ID of Channel/Group where the bot plays Music.
6. `LOG_GROUP` : Group to send Playlist, if CHAT is a Group
7. `ADMINS` : ID of users who can use admin commands.
8. `ARQ_API` : Get it for free from [@ARQRobot](https://telegram.dog/ARQRobot), This is required for /dplay to work.
9. `STREAM_URL` : Stream URL of radio station or a youtube live video to stream when the bot starts or with /radio command.
10. `MAXIMUM_DURATION` : Maximum duration of song to play.(Optional)
11. `REPLY_MESSAGE` : A reply to those who message the USER account in PM. Leave it blank if you do not need this feature. 
12. `ADMIN_ONLY` : Pass `Y` If you want to make /play and /dplay commands only for admins of `CHAT`. By default /play and /dplay is available for all.

- Enable the worker after deploy the project to Heroku
- Bot will starts radio automatically in given `CHAT` with given `STREAM_URL` after deploy.(24*7 Music even if heroku restarts, radio stream restarts automatically.)  
- To play a song use /play as a reply to audio file or a youtube link.
- Use /play <song name> to play song from youtube and /dplay <song name> to play from Deezer.
- Use /help to know about other commands.
</details>

<details><summary> <h1 align="center">FEATURES</h1> </summary>

- Playlist, queue
- Supports Live streaming from youtube
- Supports both deezer and youtube to search songs.
- Play from telegram file supported.
- Starts Radio after if no songs in playlist.
- Automatically downloads audio for the first two tracks in the playlist to ensure smooth playing
- Automatic restart even if heroku restarts.


</details>
