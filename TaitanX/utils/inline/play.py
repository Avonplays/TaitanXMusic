import math

from pyrogram.types import InlineKeyboardButton

from TaitanX.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < TaitanX <= 10:
        bar = "⚪─────────"
    elif 10 < TaitanX < 20:
        bar = "━⚪────────"
    elif 20 <= TaitanX < 30:
        bar = "━━⚪───────"
    elif 30 <= TaitanX < 40:
        bar = "━━━⚪──────"
    elif 40 <= TaitanX < 50:
        bar = "━━━━⚪─────"
    elif 50 <= TaitanX < 60:
        bar = "━━━━━⚪────"
    elif 60 <= TaitanX < 70:
        bar = "━━━━━━⚪───"
    elif 70 <= TaitanX < 80:
        bar = "━━━━━━━⚪──"
    elif 80 <= TaitanX < 95:
        bar = "━━━━━━━━⚪─"
    else:
        bar = "━━━━━━━━━⚪"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="𝗦𝘂𝗽𝗽𝗼𝗿𝘁 💭", url=f"t.me/TaitanXSupport"),
            InlineKeyboardButton(text="𝗨𝗽𝗱𝗮𝘁𝗲𝘀 💬", url=f"t.me/TaitanXBot"),
            )
        ],
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")
            )
        ],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="𝗦𝘂𝗽𝗽𝗼𝗿𝘁 💭", url=f"t.me/TaitanXSupport"),
            InlineKeyboardButton(text="𝗨𝗽𝗱𝗮𝘁𝗲𝘀 💬", url=f"t.me/TaitanXBot"),
            )
        ],
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")
            )
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="𝗦𝘂𝗽𝗽𝗼𝗿𝘁 💭", url=f"t.me/TaitanXSupport"),
            InlineKeyboardButton(text="𝗨𝗽𝗱𝗮𝘁𝗲𝘀 💬", url=f"t.me/TaitanXBot"),
            )
        ],
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")
            )
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
